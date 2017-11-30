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

    def open_home_page(self):
        wd = self.wd
        wd.get("http://nadzor.comita.lan:8080/watch/")

    def login_admin(self):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_id("loginBtn").click()
        WebDriverWait(wd, 3).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='tab1']/infotable/div/div[2]/table/tbody/tr[1]/td[2]/div")))
        #wd.find_element_by_id("username").click()
        #wd.find_element_by_id("username").clear()
        #wd.find_element_by_id("password").click()
        #wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("123")
        wd.find_element_by_id("username").send_keys("admin")
        #WebDriverWait(wd, 3).until(EC.text_to_be_present_in_element_value(By.XPATH, '//*[@id="username" and text() = "admin"]'))
        wd.find_element_by_id("loginDlgaction_saveBtn").click()

    def user_properties_open(self):
        wd = self.wd
        wd.find_element_by_xpath("//*[@id='tab0']/userstable/div[2]/div[2]/table/tbody/tr[1]/td[1]").click()
        wd.find_element_by_xpath("//div[@id='tab0']/userstable/div[1]/div/div[2]").click()

    def expand_module_zivs(self):
        wd = self.wd
        # expand field Модули ЗИВС
        wd.find_element_by_xpath("//div[@class='ms-options-wrap']/button").click()
        # wait form loaded
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.XPATH, "//label[@for='ms-opt-14']")))

    def select_sao321(self):
        wd = self.wd
        # select САО 321
        wd.find_element_by_xpath("//label[@for='ms-opt-14']").click()
        if wd.find_element_by_id("ms-opt-14").is_selected():
            wd.find_element_by_id("ms-opt-14").click()

    def save_properties(self):
        wd = self.wd
        wd.find_element_by_id("userListaction_saveBtn").click()
        # wait to save
        WebDriverWait(wd, 2).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only")))
        # click close Информация сохранена
        wd.find_element_by_css_selector(
            ".ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only").click()

    def test_admin_block_module(self):
        self.login_admin()
        self.user_properties_open()
        self.expand_module_zivs()
        self.select_sao321()
        self.save_properties()
        """
        #блокирование модуля
        wd.find_element_by_id("modulesBlock").click()
        wd.find_element_by_xpath("//div[@id='tab1']//div[.='САО Схема']").click()
        wd.find_element_by_xpath("//div[@id='tab1']/zivstable/div[1]/div/div[2]").click()
        WebDriverWait(wd,2).until(EC.presence_of_element_located((By.ID,"moduleBlock")))
        wd.find_element_by_id("moduleBlock").click()
        wd.find_element_by_id("moduleBlockReason").click()
        wd.find_element_by_id("moduleBlockReason").clear()
        wd.find_element_by_id("moduleBlockReason").send_keys("Причина блокировки №123-34213\nС переносом строки\n        И спецсимволами ,Ю/ЭЖЮЪЭ!()*\"%;(?%!!")
        WebDriverWait(wd,2).until(EC.element_to_be_clickable((By.ID,"moduleListaction_saveBtn")))
        # без задержки почему-то не нажимается
        wd.find_element_by_id("moduleListaction_saveBtn").click()
        WebDriverWait(wd,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,".ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only")))
        wd.find_element_by_xpath("//div[@class='ui-dialog-buttonset']//button[.='Закрыть']").click()"""

    def tearDown(self):
        self.wd.quit()


