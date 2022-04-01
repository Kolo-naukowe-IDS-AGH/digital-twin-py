from abc import ABC, abstractmethod
from typing import Any

from requests import Session
from requests.adapters import HTTPAdapter

from dt.http.adapters import TimeoutHTTPAdapter
from dt.http.retry import DEFAULT_RETRY_STRATEGY

DEFAULT_HTTP_ADAPTER = TimeoutHTTPAdapter(max_retries=DEFAULT_RETRY_STRATEGY)


class HTTPService(ABC):
    adapter: HTTPAdapter
    session: Session
    caller: str | None

    api_uri: str

    def __init__(
        self,
        adapter: HTTPAdapter | None = DEFAULT_HTTP_ADAPTER,
        caller: str | None = None,
    ) -> None:
        self.session = Session()
        self.adapter = adapter
        self.caller = caller

        self._init_session()

    def _init_session(self) -> None:
        self.session.mount("https://", self.adapter)
        self.session.mount("http://", self.adapter)

    def get_caller(self) -> str:
        return self.caller or "unknown"

    def get_headers(self) -> dict:
        return {"Content-Type": "application/json", "X-Caller": self.get_caller()}

    @abstractmethod
    def get_api_uri(self, path: str) -> str:
        ...

    def get(self, path: str) -> Any:
        return self.session.get(url=self.get_api_uri(path), headers=self.get_headers())

    def post(
        self,
        path: str,
        data: dict | list | bytes | None = None,
        json: str | None = None,
    ) -> Any:
        return self.session.post(
            url=self.get_api_uri(path), data=data, json=json, headers=self.get_headers()
        )
