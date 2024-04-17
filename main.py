# coding=utf-8
from typing import Any
from wsgiref.simple_server import make_server
import time

HELLO_WORLD = b"Hello, World\n"

class ResponseTimingMiddleware(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, env, start_response):
        start_time = time.time()
        response = self.app(env, start_response)
        response_time = (time.time() - start_time) * 1000
        timing_text = "\n记录请求耗时中间件输出\n\n本次请求耗时: {:.10f}ms\n\n\n".format(response_time)
        response.append(timing_text.encode('utf-8'))
        return response

def index(req):
    print(req)
    return req

def home(req):
    print(req)
    return req

all_url = {
    '/': home,
    '/index': index,
}

def simple_app(environ, start_response):
    print(environ.get('PATH_INFO'))

    url = environ.get('PATH_INFO')

    params = environ.get('QUERY_STRING')

    if url is None or url not in all_url.keys():
        start_response('404 NOT FOUND', [('Content-type', 'text/plain;charset=utf-8')])
        return [b'404 not Found']
    
    res = all_url.get(url)
    if res is None:
        start_response('404 NOT FOUND', [('Content-type', 'text/plain;charset=utf-8')])
        return [b'404 not Found']
    
    return_body = []
    return_body.append(res(params))

    for k, v in environ.items():
        return_body.append("{} : {}".format(k, v))

    start_response('200 OK', [('Content-type', 'text/plain;charset=utf-8')])
    return ["\n".join(return_body).encode('utf-8')]

class AppClass:
    def __call__(self, environ, start_response):
        status = '200 OK'
        response_header = [('Content-type', 'text/plain')]
        start_response(status, response_header)
        return [HELLO_WORLD]
    
application = ResponseTimingMiddleware(simple_app)

server = make_server('192.168.200.128', 9090, app=application)

server.serve_forever()
