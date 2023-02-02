import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Authentication(unittest.TestCase):
    USERNAME = 'admin'
    PASSWORD = 'admin'

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.delete_all_cookies()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(30)

    def test_auth(self):
        self.chrome.get('https://' + self.USERNAME + ':' + self.PASSWORD + '@the-internet.herokuapp.com/basic_auth')
        sleep(3)

    def tearDown(self) -> None:
        self.chrome.quit()

