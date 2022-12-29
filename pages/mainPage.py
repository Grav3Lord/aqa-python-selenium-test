import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from base.baseClass import Base


class MainPage(Base):
    url = 'https://www.oldi.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    location_button_no = "//button[@class='select_city_confirm_no']"
    location_city = "//a[@data-id='269480']"
    after_city = '//*[@id="head_geo_select"]/span'
    login_acc_btn = '//li[@id="notsigned"]'
    login_mail_input = '//*[@id="youremail_login"]'
    login_password_input = '//input[@data-valid="password"]'
    login_submit_button = '//button[@name="Login"]'
    catalog_button = '//a[@class="catalog-btn SECTION"]'
    catalog_category_main = '//a[@href="/catalog/8416/"]'
    catalog_category_second = '//*[@id="ol-menu-content"]/li[2]/ul/div[1]/span[1]/li/a'
    ad_from_hell = '//button[@class="close js-close"]'

    # Getters

    def get_location_button_no(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.location_button_no)))

    def get_location_city_id(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.location_city)))

    def get_city_name_after(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.after_city)))

    def get_personal_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_acc_btn)))

    def get_user_login(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.login_mail_input)))

    def get_user_pass(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.login_password_input)))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_submit_button)))

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_catalog_category_main(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_category_main)))

    def get_catalog_category_second(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_category_second)))

    def get_starter_ad_close_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ad_from_hell)))

    # Actions

    def click_location_city_change(self):
        self.get_location_button_no().click()
        print('Баннер выбора города открыт')

    def click_location_city_id(self):
        self.get_location_city_id().click()
        print('Город успешно выбран')

    def click_login_button(self):
        self.get_personal_login_button().click()
        print('Поле логина открыто')

    def input_login_window_crutch(self):
        self.get_user_login().send_keys(Keys.HOME)
        print('Костыль работает, поля авторизации доступны для ввода')

    def input_login_email(self, email):
        self.get_user_login().send_keys(email)
        print('E-mail введен')

    def input_login_password(self, password):
        self.get_user_pass().click()
        self.get_user_pass().send_keys(password)
        print('Пароль введён')

    def click_login_submit(self):
        self.get_submit_button().click()
        print('Кнопка подтверждения кликнута')

    def click_category_button(self):
        self.get_catalog_button().click()
        print('Меню категорий открыто')

    def hover_category_main(self):
        self.hover_mouse(self.get_catalog_category_main())
        print('Курсор наведен на выбранную категорию')

    def click_category_second(self):
        self.hover_and_click(self.get_catalog_category_second())
        print('Категория открыта')

    # Methods

    def change_location(self):
        self.driver.get(self.url)
        self.get_current_url()
        self.click_location_city_change()
        self.click_location_city_id()
        self.assert_word(self.get_city_name_after(), "Санкт-Петербург")

    def auth(self):
        self.click_login_button()
        self.input_login_window_crutch()
        self.input_login_email('test.aqa69@gmail.com')
        self.input_login_password('usertest1234')
        self.click_login_submit()
        time.sleep(3)

    def catalog_surfing(self):
        self.click_category_button()
        self.hover_category_main()
        self.click_category_second()
        time.sleep(3)
        self.assert_url('https://spb.oldi.ru/catalog/6535/')

