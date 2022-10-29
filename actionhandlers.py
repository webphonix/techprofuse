import tornado.web
import json
import logging


class BaseAction(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")


class FileAction(BaseAction):
    def get(self):
        # if not self.current_user:
        #     self.redirect("/login")
        #     return
        self.render("views/index.html")


class JsonHandler(BaseAction):
    def get(self):
        self.finish({'data': "Hello Guru!"})

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


# class LogoutAction(BaseAction):
#     def get(self):
#         self.clear_cookie('username')
#         self.redirect(self.get_argument('next', '/dashboard'))


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


# class HoldingHandler(BaseAction):
#     def get(self):
#         # data = sd.get_holding_data()
#         data = hld.my_report()
#         r = data.to_json(orient='records')
#         r = json.loads(r)
#         self.finish({'data': r})
