import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class ButtonsClick(unittest.TestCase):
    DOUBLE_CLICK_BUTTON = (By.XPATH, '//*[@id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.XPATH, '//*[@id="rightClickBtn"]')
    DOUBLE_CLICK_OUTPUT_MESSAGE = (By.XPATH, '//*[@id="doubleClickMessage"]')
    RIGHT_CLICK_OUTPUT_MESSAGE = (By.XPATH, '//*[@id="rightClickMessage"]')
    chrome = None

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.delete_all_cookies()
        self.chrome.maximize_window()
        self.chrome.get('https://demoqa.com/buttons')
        self.chrome.implicitly_wait(30)

    def tearDown(self):
        self.chrome.quit()

    def test_right_click_double_click(self):
        # double click and output message verification
        double_click = self.chrome.find_element(*self.DOUBLE_CLICK_BUTTON)
        webdriver.ActionChains(self.chrome).double_click(on_element=double_click).perform()

        elem = self.chrome.find_element(*self.DOUBLE_CLICK_OUTPUT_MESSAGE)
        print(elem.text)

        # right click and output message verification
        right_click = self.chrome.find_element(*self.RIGHT_CLICK_BUTTON)
        webdriver.ActionChains(self.chrome).context_click(right_click).perform()

        elem = self.chrome.find_element(*self.RIGHT_CLICK_OUTPUT_MESSAGE)
        print(elem.text)
