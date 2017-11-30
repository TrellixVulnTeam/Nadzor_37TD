# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_admin_block_module(app):
    app.login_admin("admin", "123")
    app.user_properties_open()
    app.expand_module_zivs()
    app.select_sao321()
    app.save_properties()




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



