import datetime

from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self, driver):
        self.driver = driver

    """ Method for getting current url """

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url : " + get_url)

    """ Method for word assertion """

    def assert_word(self, word, result):
        valueWord = word.text
        print("Элемент проверки: " + valueWord)  # Checking text result
        assert valueWord == result
        print('Assertion complete')

    """ Method screenshot """

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M")
        screen_name = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('.\\screen\\' + screen_name)

    """ Method for link assertion """

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('URL assertion complete')

    """ Method for hover an element """

    def hover_mouse(self, element):
        ac = ActionChains(self.driver)
        ac.move_to_element(element).perform()

    """ Method for hover and click an element """

    def hover_and_click(self, element):
        ac = ActionChains(self.driver)
        ac.move_to_element(element).click().perform()

    """ Method for dragging slider """

    def click_and_hold(self, slider, px):
        ac = ActionChains(self.driver)
        ac.click_and_hold(slider).move_by_offset(px, 0).release().perform()

