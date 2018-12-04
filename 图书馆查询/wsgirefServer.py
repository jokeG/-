from wsgiref.simple_server import make_server
from url import urls
from views import error


def run(env, response):
    print(env)
    response("200 OK", [('Content-type', 'text/html')])
    position = env['PATH_INFO']
    func = None
    for url in urls:
        if position == url[0]:
            func = url[1]
            break
    if func:
        response = func(env)
    else:
        response = error(env)

    return [response.encode('utf-8'), ]


if __name__ == '__main__':
    ser = make_server('127.0.0.1', 8000, run)
    ser.serve_forever()
