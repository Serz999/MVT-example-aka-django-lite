class Router:
    def __init__(self) -> None:
        self.URLS = {}

    def register(self, path, view) -> None:
        self.URLS[path] = view 