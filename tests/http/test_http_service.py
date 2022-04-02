from dt.http import DEFAULT_HTTP_ADAPTER, HTTPService


class Service(HTTPService):
    def get_api_uri(self, path: str) -> str:
        return f"http://localhost/{path}"


def test_service_initialization():
    service = Service()

    assert service.auth is None
    assert service.adapter == DEFAULT_HTTP_ADAPTER
    assert service.get_caller() == "unknown"
    assert service.get_headers() == {
        "Content-Type": "application/json",
        "X-Caller": "unknown",
    }
