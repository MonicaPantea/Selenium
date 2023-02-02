import requests

import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class BrokenLink(unittest.TestCase):
    BROKEN_LINK = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/a[2]')
    chrome = None

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.delete_all_cookies()
        self.chrome.maximize_window()
        self.chrome.get('https://demoqa.com/broken')
        self.chrome.implicitly_wait(30)

    def tearDown(self):
        self.chrome.quit()

    def test_broken_link(self):
        link = self.chrome.find_element(*self.BROKEN_LINK).get_attribute('href')
        result = requests.head(link)
        if result.status_code == 500:
            print(f'{link} is a broken URL!')

    def test_broken_img(self):
        link = self.chrome.find_element(*self.BROKEN_LINK).get_attribute('href')
        result = requests.head(link)
        if result.status_code == 500:
            print(f'{link} is a broken URL!')










