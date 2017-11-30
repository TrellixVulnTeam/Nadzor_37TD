__author__ = 'dmitryh'

class SessionHelper:

    def __init__(self,app):
        self.app = app

    def login_admin(self, user_login, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("loginBtn").click()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_id("username").send_keys(user_login)
        wd.find_element_by_id("loginDlgaction_saveBtn").click()

