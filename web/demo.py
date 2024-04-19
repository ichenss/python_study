import web

urls = (
    '/(.*)', 'hello',
)

app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello,' + name
    
    
class MiddlewareExample(object):
    def __init__(self, app):
        self._app = app
        
    def __call__(self, environ, start_response):
        if not self._app:
            return ['Advanced return !']
        # 调用下一层
        return self._app(environ, start_response)
    
def create_example_app(app):
    return MiddlewareExample(
        MiddlewareExample(
            MiddlewareExample(
                MiddlewareExample(app)
            )
        )
    )
    
if __name__ == "__main__":
    # app.wsgifunc()
    app.run()

