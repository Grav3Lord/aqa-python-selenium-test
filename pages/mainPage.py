from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.baseClass import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_product_one = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_two = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_three = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//div[@id='shopping_cart_container']"
    burger_button = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"

    # Getters

    def get_product_one(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_one)))

    def get_product_two(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_two)))

    def get_product_three(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_three)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_burger(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_button)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))

    # Actions

    def add_to_cart_first(self):
        self.get_product_one().click()
        print('Product successfully added to the cart 1')

    def add_to_cart_second(self):
        self.get_product_two().click()
        print('Product successfully added to the cart 2')

    def add_to_cart_third(self):
        self.get_product_three().click()
        print('Product successfully added to the cart 3')

    def enter_cart(self):
        self.get_cart().click()
        print('Cart entered')

    def click_burger(self):
        self.get_burger().click()
        print('Burger button clicked')

    def click_link_about(self):
        self.get_link_about().click()
        print('Link about opened')

    # Methods

    def select_product_first(self):
        self.get_current_url()
        self.add_to_cart_first()
        self.enter_cart()

    def select_product_second(self):
        self.get_current_url()
        self.add_to_cart_second()
        self.enter_cart()

    def select_product_third(self):
        self.get_current_url()
        self.add_to_cart_third()
        self.enter_cart()

    def open_link_about(self):
        self.get_current_url()
        self.click_burger()
        self.click_link_about()