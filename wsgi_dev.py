"""
This file is to run on local server (localost:8989)
"""
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
import NaagRoute as nr


from tornado.options import define, options
define("port", default=8989, help="run on the given port", type=int)


def startNaag():
    tornado.ioloop.IOLoop.instance().start()


def stopNaag():
    tornado.ioloop.IOLoop.instance().stop()
    exit()


def main():
    tornado.options.parse_command_line()
    local_app = tornado.web.Application(handlers=nr.NaagRoute)

    http_server = tornado.httpserver.HTTPServer(local_app)
    http_server.listen(options.port)
    try:
        # threading.Thread(target=startNaag).start()
        print("...Starting Naag Server...")
        startNaag()
    # signal : CTRL + BREAK on windows or CTRL + C on linux
    except KeyboardInterrupt:
        print("...Stopping Naag Server...")
        # threading.Thread(target=stopNaag).start()
        http_server.stop()
        stopNaag()


if __name__ == "__main__":
    main()
