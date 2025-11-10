# src/core/base_client.py
from __future__ import annotations
import os, time, random, datetime, threading, logging
from email.utils import parsedate_to_datetime
import requests, backoff

log = logging.getLogger("api")

class BaseAPIClient:
    """Базовый HTTP-клиент: общий для любых REST API."""
    _lock = threading.Lock()
    _next_allowed_time = 0.0  # для троттлинга в CI

    def __init__(self, base_url: str, headers: dict | None = None, timeout: float = 15.0):
        self.base = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    @backoff.on_exception(backoff.expo, (requests.Timeout, requests.ConnectionError), max_time=30)
    def request(self, method: str, path: str, **kw) -> requests.Response:
        url = f"{self.base}{path}"
        max_attempts = kw.pop("max_attempts", 6)
        base_delay = float(kw.pop("base_delay", 1.0))
        cap_delay = float(kw.pop("cap_delay", 20.0))

        for attempt in range(1, max_attempts + 1):
            # CI-троттлинг (умолч. 2 запроса/сек)
            if os.getenv("CI") == "true":
                rate_qps = float(os.getenv("RATE_LIMIT_QPS", "2.0"))
                min_interval = 1.0 / max(rate_qps, 0.1)
                with BaseAPIClient._lock:
                    now = time.time()
                    if now < BaseAPIClient._next_allowed_time:
                        time.sleep(BaseAPIClient._next_allowed_time - now)
                    BaseAPIClient._next_allowed_time = time.time() + min_interval

            resp = self.session.request(method, url, timeout=self.timeout, **kw)
            log.debug("HTTP %s %s -> %s in %.3fs", method, path, resp.status_code, resp.elapsed.total_seconds())

            if resp.status_code != 429:
                return resp

            # ==== 429 handling ====
            retry_after = resp.headers.get("Retry-After")
            delay = None
            if retry_after:
                s = retry_after.strip()
                if s.isdigit():
                    delay = float(s)
                else:
                    try:
                        dt = parsedate_to_datetime(s)
                        delay = max(0.0, (dt - datetime.datetime.now(tz=dt.tzinfo)).total_seconds())
                    except Exception:
                        delay = None

            if delay is None:
                delay = min(base_delay * (2 ** (attempt - 1)), cap_delay) + random.uniform(0.0, 0.3)

            if attempt == max_attempts:
                log.warning("429 after %d attempts, giving up (last delay=%.2fs)", attempt, delay)
                return resp

            time.sleep(delay)

        return resp
