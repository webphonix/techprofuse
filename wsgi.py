"""
This file is to deploy application on CPANEL with WSGI supported Server
"""

import tornado.wsgi
import os
import tornado.web
import NaagRoute as nr

settings = {
    "cookie_secret": "43oETHKYQDGEYRkA5BEAGDJ5F1Y#7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
}

app = tornado.wsgi.WSGIApplication(handlers=nr.NaagRoute, **settings)
