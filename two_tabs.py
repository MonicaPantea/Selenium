import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class SwichToTab(unittest.TestCase):
    HOME_LINK = (By.XPATH, '//*[@id="simpleLink"]')
    chrome = None

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.delete_all_cookies()
        self.chrome.maximize_window()
        self.chrome.get('https://demoqa.com/links')
        self.chrome.implicitly_wait(30)

    def tearDown(self):
        self.chrome.quit()

    def test_swich_to_tab(self):
        # open the new tab and swich to it
        self.chrome.find_element(*self.HOME_LINK).click()
        self.chrome.switch_to.window(self.chrome.window_handles[1])

        # verify the new tab url
        expected = 'https://demoqa.com/'
        self.assertTrue(expected, 'URL is incorrect')
        print(f'The second tab url is {self.chrome.current_url}')

        # swich on first tab and verify the url
        self.chrome.switch_to.window(self.chrome.window_handles[0])

        expected = 'https://demoqa.com/links'
        self.assertTrue(expected, 'URL is incorrect')
        print(f'The first tab url is {self.chrome.current_url}')

