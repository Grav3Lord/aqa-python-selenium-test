import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.baseClass import Base


class CatalogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    left_price_filter = '//input[@name="pricefrom"]'
    right_price_filter = '//input[@id="priceto"]'
    filter_btn_submit = '//a[@class="oldi-butt-get-filtring"]'
    show_all_button_manufacturer = '//*[@id="P_1629contr"]/div/div'
    checkbox_huawei = '//div[@id="P_1629_169744-styler"]'
    checkbox_lenovo = '//div[@id="P_1629_4949-styler"]'
    assert_notebook = '//*[@id="catalog"]/div[1]/div[1]/div[3]/div[2]/div[1]/div/div/a'
    notebook_item = '//*[@id="item_4083357"]/div[2]/div[2]/div[1]/a'
    button_add_to_cart = '//div[@id="pbid5660151"]'
    cart_drop_menu = '//span[@id="cart_img_arrow"]'
    drop_cart_order_button = '//a[@class="orderlink"]'
    cart_sumtotal = '//span[@class="sumtotal"]'

    # Getters

    def get_left_input_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.left_price_filter)))

    def get_right_input_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.right_price_filter)))

    def get_filter_btn_submit(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_btn_submit)))

    def get_show_all_manufacturer(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.show_all_button_manufacturer)))

    def get_checkbox_huawei(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_huawei)))

    def get_checkbox_lenovo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_lenovo)))

    def get_assert_notebook(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_notebook)))

    def get_notebook_item(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.notebook_item)))

    # Actions

    def input_price_from(self):
        self.get_left_input_field().send_keys('59202')
        print('Минимальная стоимость выставлена')

    def input_price_to(self):
        self.get_right_input_field().send_keys('82004')
        print('Максимальная стоимость выставлена')

    def click_manufacturer_show_all(self):
        self.get_show_all_manufacturer().click()
        print('Список произоводителей раскрыт')

    def click_checkbox_huawei(self):
        self.get_checkbox_huawei().click()
        print('Производитель Huawei выбран')

    def click_checkbox_lenovo(self):
        self.get_checkbox_lenovo().click()
        print('Производитель Lenovo выбран')

    def click_filter_btn_submit(self):
        self.get_filter_btn_submit().click()
        print('Кнопка "Подтвердить фильтры" кликнута')

    def click_notebook_item(self):
        self.get_notebook_item().click()
        print('Открыта страница выбранного товара')

    # Methods

    def filter_change(self):
        self.get_current_url()
        try:
            self.click_manufacturer_show_all()
        except ElementClickInterceptedException:
            self.click_close_ad_button()
            self.click_manufacturer_show_all()
        time.sleep(5)
        self.click_checkbox_huawei()
        self.click_checkbox_lenovo()

        self.input_price_from()
        time.sleep(2)
        self.input_price_to()
        time.sleep(10)
        self.click_filter_btn_submit()
        time.sleep(5)
        self.assert_word(self.get_assert_notebook(), 'Производители: Huawei; Lenovo')
        try:
            self.click_notebook_item()
        except ElementClickInterceptedException:
            self.click_close_ad_button()
            self.click_notebook_item()
        self.assert_url('https://spb.oldi.ru/catalog/element/02008803/')
