class HttpRequest:
    def __init__(self, method, path):
        self.method = method
        self.path = path


class HttpResponse:
    def __init__(self, status, body) -> None:
        self.status = status
        self.body = body

    def __str__(self) -> None:
        return f'HTTP/1.1 {self.status}\n\n{self.body}'