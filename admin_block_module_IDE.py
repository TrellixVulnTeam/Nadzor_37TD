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

class admin_block_module_IDE(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_admin_block_module_IDE(self):
        success = True
        wd = self.wd
        wd.get("http://nadzor.comita.lan:8080/watch/")
        wd.find_element_by_id("loginBtn").click()
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        WebDriverWait(wd,2).until(EC.presence_of_element_located((By.ID,"username")))
        wd.find_element_by_id("username").send_keys("admin")
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("123")
        wd.find_element_by_id("loginDlgaction_saveBtn").click()
        wd.find_element_by_xpath("//*[@id='tab0']/userstable/div[2]/div[2]/table/tbody/tr[1]/td[1]").click()
        wd.find_element_by_xpath("//div[@id='tab0']/userstable/div[1]/div/div[2]").click()
        wd.find_element_by_xpath("//div[@class='ms-options-wrap']/button").click()
        WebDriverWait(wd,2).until(EC.presence_of_element_located((By.XPATH,"//label[@for='ms-opt-14']")))
        wd.find_element_by_xpath("//label[@for='ms-opt-14']").click()
        if wd.find_element_by_id("ms-opt-14").is_selected():
            wd.find_element_by_id("ms-opt-14").click()
        wd.find_element_by_id("userListaction_saveBtn").click()
        WebDriverWait(wd,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,".ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only")))
        #WebDriverWait(wd,2).until(EC.presence_of_element_located((By.XPATH,"//div[@class='ui-dialog-buttonset']//button[.='Закрыть']")))
        #wd.find_element_by_xpath("//div[@class='ui-dialog-buttonset']//button[.='Закрыть']").click()
        wd.find_element_by_css_selector(".ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only").click()
        wd.find_element_by_id("modulesBlock").click()
        wd.find_element_by_xpath("//div[@id='tab1']//div[.='САО Схема']").click()
        wd.find_element_by_xpath("//div[@id='tab1']/zivstable/div[1]/div/div[2]").click()
        WebDriverWait(wd,2).until(EC.presence_of_element_located((By.ID,"moduleBlock")))
        if not wd.find_element_by_id("moduleBlock").is_selected():
            wd.find_element_by_id("moduleBlock").click()
        wd.find_element_by_id("moduleBlockReason").click()
        wd.find_element_by_id("moduleBlockReason").clear()
        wd.find_element_by_id("moduleBlockReason").send_keys("Причина блокировки №123-34213\nС переносом строки\n        И спецсимволами ,Ю/ЭЖЮЪЭ!()*\"%;(?%!!")
        wd.find_element_by_id("moduleListaction_saveBtn").click()
        wd.find_element_by_xpath("//div[@class='ui-dialog-buttonset']//button[.='Закрыть']").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
