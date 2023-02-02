import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Cookies(unittest.TestCase):

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://reddit.com')
        self.chrome.implicitly_wait(30)

    def tearDown(self):
        self.chrome.quit()

    def test_cookies(self):

        # get cookies
        cookies = self.chrome.get_cookies()
        print(cookies)
        print(len(cookies))

        #add cookie
        cookie = {'name': 'Selenium', 'value': 'Python'}
        self.chrome.add_cookie(cookie)

        cookies = self.chrome.get_cookies()
        print(cookies)
        print(len(cookies))







