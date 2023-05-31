from socket import socket, AF_INET, SOCK_STREAM
from backend.urls import router
from my_django.http import HttpRequest


def generate_resp(http_req):
    buff = http_req.split()
    http_method = buff[0]
    path = buff[1]
    if path in router.URLS:
        some_view = router.URLS[path] 
        return some_view(HttpRequest(http_method, path)).__str__()
    else:
        return 'HTTP/1.1 404 Not found!!!'


if __name__ == '__main__':
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('0.0.0.0', 8001))
    sock.listen()

    while True:
        try:
            conn, host = sock.accept()
            req = conn.recv(1024)
            print(f'recv from {req}')
            res = generate_resp(req.decode('utf-8')) 
            conn.send(res.encode())
            conn.close()
        except KeyboardInterrupt:
            sock.close()
            break
