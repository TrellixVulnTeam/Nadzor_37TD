from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
__author__ = 'dmitryh'


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicitly_wait(2)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://nadzor.comita.lan:8080/watch/")

    def login_admin(self, user_login, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_id("loginBtn").click()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_id("username").send_keys(user_login)
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

    def destroy(self):
        self.wd.quit()




