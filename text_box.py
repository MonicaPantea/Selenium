import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TextBox(unittest.TestCase):
    ELEMENTS_BUTTON = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]')
    TEXT_BOX_BUTTON = (By.XPATH, '//*[@id="item-0"]')
    FULL_NAME_BOX = (By.XPATH, '//*[@id="userName"]')
    EMAIL_BOX = (By.XPATH, '//*[@id="userEmail"]')
    ADDRESS_BOX = (By.XPATH, '//*[@id="currentAddress"]')
    ADDRESS2_BOX = (By.XPATH, '//*[@id="permanentAddress"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="submit"]')
    OUTPUT_MESSAGE = (By.XPATH, '//*[@id="output"]/div')
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

    def test_text_box(self):
        # insert credentials

        self.chrome.find_element(*self.ELEMENTS_BUTTON).click()
        self.chrome.find_element(*self.TEXT_BOX_BUTTON).click()
        self.chrome.find_element(*self.FULL_NAME_BOX).send_keys('Ioana Monica')
        self.chrome.find_element(*self.EMAIL_BOX).send_keys('Ioana.Monica@gmail.com')
        self.chrome.find_element(*self.ADDRESS_BOX).send_keys('Bucuresti, sector 6')
        self.chrome.find_element(*self.ADDRESS2_BOX).send_keys('Bucuresti, sector 6')
        self.chrome.find_element(*self.SUBMIT_BUTTON).click()

        # verify that the output success message is displayed
        elem = self.chrome.find_element(*self.OUTPUT_MESSAGE)
        self.assertTrue(elem.is_displayed(), 'The message is not displayed!')
