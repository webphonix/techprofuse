import actionhandlers as naag
import tornado.web


NaagRoute = [
    (r'/node_modules/(.*)', tornado.web.StaticFileHandler,
     {'path': 'node_modules/'}),
    (r'/assets/(.*)', tornado.web.StaticFileHandler, {'path': 'assets/'}),
    (r"/", naag.JsonAction, {'data': {'message': 'hello world'}}),
    (r"/home", naag.FileAction, {'kargs': {'file': 'home.html'}}),
    (r"/index", naag.FileAction, {'kargs': {'file': 'index.html'}}),
]
