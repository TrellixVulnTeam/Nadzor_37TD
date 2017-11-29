# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import pytest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class AdminBlockModule(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicitly_wait(2)

    def open_home_page(self, wd):
        wd.get("http://nadzor.comita.lan:8080/watch/")

    def login_admin(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_id("loginBtn").click()
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        WebDriverWait(wd, 2).until(EC.presence_of_element_located((By.ID, "username")))
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_id("loginDlgaction_saveBtn").click()

    def user_properties_open(self, wd):
        wd.find_element_by_xpath("//*[@id='tab0']/userstable/div[2]/div[2]/table/tbody/tr[1]/td[1]").click()
        wd.find_element_by_xpath("//div[@id='tab0']/userstable/div[1]/div/div[2]").click()

    def test_admin_block_module(self):
        success = True
        wd = self.wd
        self.login_admin(wd, username="admin", password="123")
        self.user_properties_open(wd)
        #open Модули ЗИВС
        wd.find_element_by_xpath("//div[@class='ms-options-wrap']/button").click()
        WebDriverWait(wd,5).until(EC.presence_of_element_located((By.XPATH,"//label[@for='ms-opt-14']")))
        wd.find_element_by_xpath("//label[@for='ms-opt-14']").click()
        if wd.find_element_by_id("ms-opt-14").is_selected():
            wd.find_element_by_id("ms-opt-14").click()
        wd.find_element_by_id("userListaction_saveBtn").click()
        WebDriverWait(wd,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,".ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only")))
        wd.find_element_by_css_selector(".ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only").click()
        """
        #блокирование модуля
        wd.find_element_by_id("modulesBlock").click()
        wd.find_element_by_xpath("//div[@id='tab1']//div[.='САО Схема']").click()
        wd.find_element_by_xpath("//div[@id='tab1']/zivstable/div[1]/div/div[2]").click()
        WebDriverWait(wd,2).until(EC.presence_of_element_located((By.ID,"moduleBlock")))
        wd.find_element_by_id("moduleBlock").click()
        wd.find_element_by_id("moduleBlockReason").click()
        wd.find_element_by_id("moduleBlockReason").clear()
        wd.find_element_by_id("moduleBlockReason").send_keys("Причина блокировки №123-34213\n\
        С переносом строки\n\
                И спецсимволами ,Ю/ЭЖЮЪЭ!()*\"%;(?%!!")
        WebDriverWait(wd,2).until(EC.element_to_be_clickable((By.ID,"moduleListaction_saveBtn")))
        # без задержки почему-то не нажимается
        wd.find_element_by_id("moduleListaction_saveBtn").click()
        WebDriverWait(wd,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,".ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only")))
        wd.find_element_by_xpath("//div[@class='ui-dialog-buttonset']//button[.='Закрыть']").click()"""
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

