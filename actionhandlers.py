import tornado.web
import json
import logging
import os


class BaseAction(tornado.web.RequestHandler):
    def get_login_url(self):
        return u"/login"

    def get_current_user(self):
        # return self.get_secure_cookie("username")
        user_json = self.get_secure_cookie("user")
        if user_json:
            return tornado.escape.json_decode(user_json)
        else:
            return None
            # self.redirect("/login")
            # return
        # if not self.current_user:
        #     self.redirect("/login")
        #     return


class StaticFileAction(tornado.web.StaticFileHandler):
    def initialize(self, path):
        self.path = path


class FileAction(BaseAction):
    def initialize(self, kargs):
        self.kargs = kargs

    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        print(self.kargs['file'])
        file = os.path.join("views", self.kargs['file'])
        self.render(file)


class AuthAction(BaseAction):
    def initialize(self, kargs):
        self.kargs = kargs

    def get(self):
        print(self.kargs['file'])
        file = os.path.join("views", self.kargs['file'])
        self.render(file, next=self.get_argument("next", "/"))

    def post(self):
        email = self.get_argument("username", "")
        password = self.get_argument("password", "")
        if email == "gurudevk@techprofuse.com" and password == "admin123":
            self.set_current_user(email)
            self.redirect(self.get_argument("next", u"/"))
        else:
            error_msg = u"?error=" + \
                tornado.escape.url_escape("Login incorrect.")
            self.redirect(u"/login" + error_msg)

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user", tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")


class LogoutAction(BaseAction):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument('next', u'/login'))


class JsonAction(BaseAction):
    def initialize(self, data):
        self.data = data()

    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        # self.write(self.data)
        self.finish(self.data)


# class AuthAction(BaseAction):
#     # @NaagFilters.naagauth
#     def get(self):
#         self.render("views/login.html")

#     def post(self):
#         uname = self.get_argument("uname")
#         pwd = self.get_argument("pwd")
#         if uname == "gurudevkumar51" and pwd == "Hyderabad51#":
#             self.set_secure_cookie("username", uname)
#             # self.set_secure_cookie("password", pwd)
#             self.redirect("/dashboard")
#         else:
#             self.redirect("/login")


# class HomeAction(BaseAction):
#     def get(self):
#         if not self.current_user:
#             self.redirect("/login")
#             return
#         self.render("views/home.html")

# class ViewAction(BaseAction):
#     def __init__(self):
#         print (self)


# class PartialViewHandler(BaseAction):
#     def get(self):
#         pth = self.request.path
#         r = self.request.uri
#         pth = pth.replace("/", "")
#         self.write(f"Hi Buddy, I am PartialViewHandler with {r} url {pth}")
