from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.user_properties import UserPropertiesHelper
__author__ = 'dmitryh'


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.user_properties = UserPropertiesHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://nadzor.comita.lan:8080/watch/")

    def destroy(self):
        self.wd.quit()




