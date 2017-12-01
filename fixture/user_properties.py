from fixture.wait import WaitHelper

__author__ = 'dmitryh'

class UserPropertiesHelper:

    def __init__(self,app):
        self.app = app

    def open(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='tab0']/userstable/div[2]/div[2]/table/tbody/tr[1]/td[1]").click()
        wd.find_element_by_xpath("//div[@class='toolbarBtn cursor-cell editBtn editBtn_active']").click()

    def expand_module_zivs(self):
        wd = self.app.wd
        # expand field Модули ЗИВС
        wd.find_element_by_xpath("//div[@class='ms-options-wrap']/button").click()
        # wait form loaded
        #WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.XPATH, "//label[@for='ms-opt-14']")))
        WaitHelper.xpath(self, "//label[@for='ms-opt-14']")


    def get_modulecheckbox_locator(self, name):
        # описание имени и локатора модуля на форме редактирования
        # description module name and locator on properties form of user
        sao407 = ["САО 407", "//label[@for='ms-opt-12']"]
        b321 = ["САО Банком 321", "//label[@for='ms-opt-13']"]
        sao213 = ["САО 213", "//label[@for='ms-opt-15']"]
        saoNFO = ["САО НФО", "//label[@for='ms-opt-16']"]
        saoNKO = ["САО НRО", "//label[@for='ms-opt-17']"]
        otkaz = ["САО Отказ", "//label[@for='ms-opt-18']"]
        shema = ["САО Схема", "//label[@for='ms-opt-10']"]
        b407 = ["САО Банком 407", "//label[@for='ms-opt-11']"]
        sao321 = ["САО 321", "//label[@for='ms-opt-14']"]
        # get id of module checkbox
        if shema[0] == name:
            locator = shema[1][14:23]
        elif b407[0] == name:
            locator = b407[1][14:23]
        elif sao321[0] == name:
            locator = sao321[1][14:23]
        elif otkaz[0] == name:
            locator = otkaz[1][14:23]
        elif saoNKO[0] == name:
            locator = saoNKO[1][14:23]
        elif saoNFO[0] == name:
            locator = saoNFO[1][14:23]
        elif sao213[0] == name:
            locator = sao213[1][14:23]
        elif b321[0] == name:
            locator = b321[1][14:23]
        elif sao407[0] == name:
            locator = sao407[1][14:23]
        return locator

    def select_module(self, name):
        wd = self.app.wd
        # получаем координаты чекбокса
        locator = self.get_modulecheckbox_locator(name)
        # select module
        if not wd.find_element_by_id(locator).is_selected():
            wd.find_element_by_id(locator).click()
        else:
            pass
            # try to make uncheck module
            # self.deselect_module(name)
            # self.save_properties()
            # self.open()
            # self.expand_module_zivs()
            # wd.find_element_by_id(locator).click()

    def deselect_module(self, name):
        wd = self.app.wd
        locator = self.get_modulecheckbox_locator(name)# select module
        # deselect module
        if wd.find_element_by_id(locator).is_selected():
            wd.find_element_by_id(locator).click()
        else:
            pass

    def save_properties(self):
        wd = self.app.wd
        wd.find_element_by_id("userListaction_saveBtn").click()
        # wait to save
        WaitHelper.css(self,".ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only")
        # click close Информация сохранена
        wd.find_element_by_css_selector(".ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only").click()



