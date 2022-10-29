"""
This file is to deploy application on CPANEL with WSGI supported Server
"""

import tornado.wsgi
import os
import tornado.web
import NaagRoute as nr

app = tornado.wsgi.WSGIApplication(handlers=nr.NaagRoute)
