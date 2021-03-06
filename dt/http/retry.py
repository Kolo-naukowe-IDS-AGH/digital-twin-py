from http import HTTPStatus
from typing import Iterable

from urllib3 import Retry

DEFAULT_STATUS_FORCE_LIST: Iterable[int] = (
    HTTPStatus.TOO_MANY_REQUESTS,
    HTTPStatus.INTERNAL_SERVER_ERROR,
    HTTPStatus.BAD_GATEWAY,
    HTTPStatus.SERVICE_UNAVAILABLE,
    HTTPStatus.GATEWAY_TIMEOUT,
)

DEFAULT_RETRY_ALLOWED_METHODS: Iterable[str] = ("HEAD", "GET", "OPTIONS")

DEFAULT_BACKOFF_FACTOR: float = 0.5

DEFAULT_RETRY_STRATEGY: Retry = Retry(
    total=3,
    status_forcelist=DEFAULT_STATUS_FORCE_LIST,
    allowed_methods=DEFAULT_RETRY_ALLOWED_METHODS,
    backoff_factor=DEFAULT_BACKOFF_FACTOR,
    respect_retry_after_header=True,
)
