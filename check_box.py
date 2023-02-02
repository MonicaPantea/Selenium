import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class CheckBox(unittest.TestCase):
    ELEMENTS_BUTTON = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]')
    CHECK_BOX_BUTTON = (By.XPATH, '//*[@id="item-1"]')
    CHECK_BOX_BUTTON2 = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/label')
    OUTPUT_MESSAGE = (By.XPATH, '//*[@id="result"]')
    EXPAND_BUTTON = (By.XPATH, '//*[@id="tree-node"]/div/button[1]')
    ANGULAR_BUTTON = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[2]/span/label/span[1]')
    chrome = None

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.delete_all_cookies()
        self.chrome.maximize_window()
        self.chrome.get('https://demoqa.com/')
        self.chrome.implicitly_wait(30)

    def tearDown(self):
        self.chrome.quit()

    def test_check_box(self):
        # check the 'home' check box
        self.chrome.find_element(*self.ELEMENTS_BUTTON).click()
        self.chrome.find_element(*self.CHECK_BOX_BUTTON).click()
        self.chrome.find_element(*self.CHECK_BOX_BUTTON2).click()

        # verify that the output success message is displayed
        elem = self.chrome.find_element(*self.OUTPUT_MESSAGE)
        self.assertTrue(elem.is_displayed(), 'The message is not displayed!')
        self.chrome.refresh()

        # select 'Angular' option from 'home' list
        self.chrome.find_element(*self.EXPAND_BUTTON).click()
        self.chrome.find_element(*self.ANGULAR_BUTTON).click()
        time.sleep(10)

        # verify the output success message text
        elem = self.chrome.find_element(*self.OUTPUT_MESSAGE)
        print(elem.text)




