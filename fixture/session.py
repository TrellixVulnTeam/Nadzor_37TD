from fixture.wait import WaitHelper
__author__ = 'dmitryh'

class SessionHelper:

    def __init__(self,app):
        self.app = app

    def login_admin(self, user_login, password):
        wd = self.app.wd
        self.app.open_home_page()
        # problem with filling fields, need to wait
        WaitHelper.css(self, "td.ng-isolate-scope")
        wd.find_element_by_id("loginBtn").click()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_id("username").send_keys(user_login)
        wd.find_element_by_id("loginDlgaction_saveBtn").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='tab0']/userstable/div[2]/div[2]/table/tbody/tr[1]/td[1]").click()
        wd.find_element_by_id("logoutBtn").click()
        wd.find_element_by_xpath("(//button[@type='button'])[2]").click()
