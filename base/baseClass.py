import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver

    # Locators

    second_layer = '//iframe[@id="fl-586864"]'
    ad_button_close = '//button[@data-fl-close="1800"]'

    # Getters

    """ Геттер для кнопки закрытия рекламного баннера """

    def get_ad_button_close(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ad_button_close)))

    # Methods

    """ Метод для получения текущего юрл """

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url : " + get_url)

    """ Метод для сверки текста """

    def assert_word(self, word, result):
        valueWord = word.text
        print("Элемент проверки: " + valueWord)  # Checking text result
        assert valueWord == result
        print('Assertion complete')

    """ Метод для создания скриншота """

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M")
        screen_name = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('.\\screen\\' + screen_name)

    """ Метод для сверки URL """

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('URL assertion complete')

    """ Метод для наведения курсора на элемент """

    def hover_mouse(self, element):
        ac = ActionChains(self.driver)
        ac.move_to_element(element).perform()

    """ Метод для наведения на элемент и клика """

    def hover_and_click(self, element):
        ac = ActionChains(self.driver)
        ac.move_to_element(element).click().perform()

    """ Метод для управления элементом 'Слайдер' """

    def click_and_hold(self, slider, px):
        ac = ActionChains(self.driver)
        ac.click_and_hold(slider).move_by_offset(px, 0).release().perform()

    """ Метод для закрытия рекламного баннера """

    def click_close_ad_button(self):
        WebDriverWait(self.driver, 30).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.second_layer)))
        self.get_ad_button_close().click()
        self.driver.switch_to.default_content()
        print('Рекламный баннер закрыт')
