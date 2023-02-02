import time
import unittest
from select import select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class PracticeForm(unittest.TestCase):
    ACCEPT_COOKIE = (By.XPATH, '//*[@id="ez-accept-all"]')
    FIRST_NAME = (By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[2]/input')
    LAST_NAME = (By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[5]/input')
    GENDER = (By.XPATH, '//*[@id="sex-1"]')
    YEARS_OF_EXPERIENCE = (By.XPATH, '//*[@id="exp-0"]')
    DATE = (By.XPATH, '//*[@id="datepicker"]')
    PROFESSION = (By.XPATH, '//*[@id="profession-1"]')
    AUTOMATION_TOOLS = (By.XPATH, '//*[@id="tool-2"]')
    CONTINENTS = (By.XPATH, '//*[@id="continents"]/option[2]')
    SELENIUM_COMMANDS = (By.XPATH, '//*[@id="selenium_commands"]/option[1]')
    BUTTON = (By.XPATH, '//*[@id="submit"]')
    chrome = None

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.delete_all_cookies()
        self.chrome.maximize_window()
        self.chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
        self.chrome.implicitly_wait(30)

    def tearDown(self):
        self.chrome.quit()

    def test_practice_form(self):
        self.chrome.find_element(*self.ACCEPT_COOKIE).click()
        self.chrome.find_element(*self.FIRST_NAME).send_keys('Monica')
        self.chrome.find_element(*self.LAST_NAME).send_keys('Ioana')
        self.chrome.find_element(*self.GENDER).click()
        self.chrome.find_element(*self.YEARS_OF_EXPERIENCE).click()
        self.chrome.find_element(*self.DATE).send_keys('25.11.1992')
        self.chrome.find_element(*self.PROFESSION).click()
        self.chrome.find_element(*self.AUTOMATION_TOOLS).click()
        self.chrome.find_element(*self.CONTINENTS).click()
        self.chrome.find_element(*self.SELENIUM_COMMANDS).click()
        button = self.chrome.find_element(*self.BUTTON)
        self.assertTrue(button.is_enabled())
