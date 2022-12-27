

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.baseClass import Base


class ItemPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    ad_button_close = '//button[@data-fl-close="1800"]'
    second_layer = '//iframe[@id="fl-586864"]'
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

    def get_ad_button_close(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ad_button_close)))

    def get_assert_notebook(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_notebook)))

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))

    def get_cart_arrow_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_drop_menu)))

    def get_cart_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.drop_cart_order_button)))

    def get_cart_sumtotal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_sumtotal)))

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

    def click_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print('Item successfully added to cart')

    def click_cart_drop_menu(self):
        self.get_cart_arrow_button().click()
        print('Cart menu dropped')

    def click_order_from_drop_cart(self):
        self.get_cart_order_button().click()
        print('Transition to checkout')

    def input_phone_number(self, phone):
        self.get_phone_number().send_keys(phone)
        print('Phone number')

    def click_close_ad_button(self):
        WebDriverWait(self.driver, 30).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.second_layer)))
        self.get_ad_button_close().click()
        self.driver.switch_to.default_content()
        print('Ad button closed, finally')

    def click_delivery_button(self):
        self.get_delivery_button().click()
        print('Delivery to address selected')

    def input_delivery_address(self, address):
        self.get_delivery_address_field().send_keys(address)
        # Здесь раньше был ещё одна строчка, но после одного оформленного заказа я её удалил.
        # self.get_delivery_address_field().send_keys(Keys.ENTER)
        # Если ввести сразу адрес, то можно обойтись без ввода индекса.
        print('Address inputted')

    def click_payment_radio(self):
        self.get_payment_radio().click()
        print('Payday')

    # Methods

    def order_notebook(self):
        self.get_current_url()
        try:
            self.click_add_to_cart()
        except ElementClickInterceptedException:
            self.click_close_ad_button()
            self.click_add_to_cart()
        self.click_cart_drop_menu()
        self.assert_word(self.get_cart_sumtotal(), "59 690 a")
        self.click_order_from_drop_cart()
        self.input_phone_number('9951234567')
        self.click_delivery_button()
        self.input_delivery_address('ул Верности, д 34 литера А')
        self.assert_word(self.get_total_sumtotal(), "59 939 a")
        self.get_screenshot()
        print('Test finished')
