

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.baseClass import Base


class OrderPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    assert_notebook = '//*[@id="item_4241947"]/div[2]/div[2]/div[1]/a/span'
    button_add_to_cart = '//div[@id="pbid5660151"]'
    item_price_list = '//span[@id="price-02012889"]'
    cart_drop_menu = '//span[@id="cart_img_arrow"]'
    drop_cart_order_button = '//a[@class="orderlink"]'
    cart_sumtotal = '//span[@class="sumtotal"]'
    phone_number_input = '//*[@id="vue-order-user-info"]/div[2]/div/div/div/div[2]/input[1]'
    delivery_button = '//li[@data-id="267247"]'
    delivery_address_field = '//input[@id="product_delivery_address"]'
    payment_method_radio = '//div[@id="payment_method_1668060-styler"]'
    all_summ_total = '//*[@id="allsum"]'

    # Getters

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number_input)))

    def get_delivery_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_button)))

    def get_delivery_address_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_address_field)))

    def get_payment_radio(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_method_radio)))

    def get_total_sumtotal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.all_summ_total)))

    # Actions

    def input_phone_number(self, phone):
        self.get_phone_number().send_keys(phone)
        print('Телефонный номер успешно введен')

    def click_delivery_button(self):
        self.get_delivery_button().click()
        print('Категория "Доставка" кликнута')

    def input_delivery_address(self, address):
        self.get_delivery_address_field().send_keys(address)
        # Кнопка Enter нужна для подтверждения ввода адресса, но, она же подтверждает Заказ,
        # Поэтому мне пришлось её закомментить.

        # self.get_delivery_address_field().send_keys(Keys.ENTER)

        # Если ввести сразу адрес, то можно обойтись без ввода индекса.
        print('Аддрес введён')

    def click_payment_radio(self):
        self.get_payment_radio().click()
        print('Вариант "Оплатить картой онлайн" выбран')

    # Methods

    def order_confirmation(self):
        self.input_phone_number('9951234567')
        self.click_delivery_button()
        self.click_payment_radio()
        self.input_delivery_address('ул Верности, д 34 литера А')
        self.assert_word(self.get_total_sumtotal(), "60 899 a")
        self.get_screenshot()
        print('Test finished')
