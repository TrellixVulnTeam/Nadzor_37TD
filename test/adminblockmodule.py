# -*- coding: utf-8 -*-


def test_admin_check_module(app):
    app.session.login_admin("admin", "123")
    app.user_properties.open()
    app.user_properties.expand_module_zivs()
    app.user_properties.select_module("САО 407")
    app.user_properties.save_properties()
    app.session.logout()


def test_admin_uncheck_module(app):
    app.session.login_admin("admin", "123")
    app.user_properties.open()
    app.user_properties.expand_module_zivs()
    app.user_properties.deselect_module("САО 407")
    app.user_properties.save_properties()
    app.session.logout()




"""
блокирование модуля
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



