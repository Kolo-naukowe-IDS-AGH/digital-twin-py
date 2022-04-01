from requests.adapters import HTTPAdapter

DEFAULT_TIMEOUT = 5


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs.pop("timeout")
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        if "timeout" not in kwargs:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)
