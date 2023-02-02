import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Windows(unittest.TestCase):
    ELEMENT1 = (By.XPATH, '//*[@id="draggable"]')
    ELEMENT2 = (By.XPATH, '//*[@id="droppable"]')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.delete_all_cookies()
        self.chrome.maximize_window()
        self.chrome.get('https://demoqa.com/droppable')
        self.chrome.implicitly_wait(30)

    def tearDown(self):
        self.chrome.quit()

    def test_drag_and_drop(self):

        elem1 = self.chrome.find_element(*self.ELEMENT1)
        elem2 = self.chrome.find_element(*self.ELEMENT2)

        webdriver.ActionChains(self.chrome).drag_and_drop(elem1, elem2).perform()
        time.sleep(10)
