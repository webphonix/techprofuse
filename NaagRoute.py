import actionhandlers as naag
import tornado.web
import google_invoice

data = google_invoice.get_data

NaagRoute = [
    (r'/node_modules/(.*)', tornado.web.StaticFileHandler,
     {'path': 'node_modules/'}),
    (r'/assets/(.*)', tornado.web.StaticFileHandler, {'path': 'assets/'}),
    (r'/templates/(.*)', tornado.web.StaticFileHandler,
     {'path': 'templates/'}),
    (r"/", naag.JsonAction, {'data': data}),
    (r"/home", naag.FileAction, {'kargs': {'file': 'home.html'}}),
    (r"/index", naag.FileAction, {'kargs': {'file': 'index.html'}}),
]
