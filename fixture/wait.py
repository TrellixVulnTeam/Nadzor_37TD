from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

__author__ = 'dmitryh'


class WaitHelper:
    def __init__(self,app):
        self.app = app

    def xpath(self,locator):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.XPATH, locator)))

    def css(self,locator):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))



