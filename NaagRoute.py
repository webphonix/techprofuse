import actionhandlers as naag
import tornado.web

NaagRoute = [
    (r'/node_modules/(.*)',
     tornado.web.StaticFileHandler, {'path': 'node_modules/'}),
    (r'/assets/(.*)',
     tornado.web.StaticFileHandler, {'path': 'assets/'}),
    (r"/", naag.JsonHandler),
    (r"/home", naag.JsonHandler),
]
