import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.catalogPage import CatalogPage
from pages.itemPage import ItemPage
from pages.mainPage import MainPage
from pages.orderPage import OrderPage


def test_order_oldi():
    op = Options()
    op.add_experimental_option('excludeSwitches', ['enable-logging'])

    # op.add_argument("--disable-notifications")

    driver = webdriver.Chrome('\\resource\\chromedriver.exe')

    print('Starting the test')

    login = MainPage(driver)
    login.change_location()
    login.auth()
    login.catalog_surfing()

    catalog = CatalogPage(driver)
    catalog.filter_change()

    order = ItemPage(driver)
    order.order_notebook()

    conf = OrderPage(driver)
    conf.order_confirmation()

