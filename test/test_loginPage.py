import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.catalogPage import CatalogPage
from pages.itemPage import ItemPage
from pages.loginPage import LoginPage


def test_order_oldi():
    op = Options()
    op.add_experimental_option('excludeSwitches', ['enable-logging'])

    # op.add_argument("--disable-notifications")

    driver = webdriver.Chrome('\\resource\\chromedriver.exe')

    print('Starting the test')

    login = LoginPage(driver)
    login.change_location()
    login.auth()
    login.catalog_surfing()

    catalog = CatalogPage(driver)
    catalog.filter_change()

    order = ItemPage(driver)
    order.order_notebook()

