from my_django.http import HttpRequest, HttpResponse


def hello_veiw(request: HttpRequest) -> HttpResponse:
    # Model and data processing...
    res = HttpResponse('200 OK', '<h1>HELLO WORLD</h1>')
    return res


def home_veiw(request: HttpRequest) -> HttpResponse:
    # Model and data processing...
    res = HttpResponse('200 OK', '<h1>HOME</h1>')
    return res