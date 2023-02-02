import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Windows(unittest.TestCase):
    NEW_WINDOW_BUTTON = (By.XPATH, '//*[@id="windowButton"]')
    chrome = None

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.delete_all_cookies()
        self.chrome.maximize_window()
        self.chrome.get('https://demoqa.com/browser-windows')
        self.chrome.implicitly_wait(30)

    def tearDown(self):
        self.chrome.quit()

    def test_new_window(self):
        # open the new tab and swich to it
        self.chrome.find_element(*self.NEW_WINDOW_BUTTON).click()
        self.chrome.switch_to.window(self.chrome.window_handles[1])

        #get window size
        size = self.chrome.get_window_size()
        width1 = size.get("width")
        height1 = size.get("height")
        print(size)

        #get window position
        position = self.chrome.get_window_position()
        x1 = position.get('x')
        y1 = position.get('y')
        print(position)

        # swich on first tab
        self.chrome.switch_to.window(self.chrome.window_handles[0])


class Alerts(unittest.TestCase):
    ALERT = (By.XPATH, '//button[text()="Click for JS Alert"]')
    CONFRIM = (By.XPATH, '//button[text()="Click for JS Confirm"]')
    PROMPT = (By.XPATH, '//button[text()="Click for JS Prompt"]')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.delete_all_cookies()
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/javascript_alerts')
        self.chrome.implicitly_wait(10)

    def tearDown(self):
        self.chrome.quit()

    def test_alert(self):
        self.chrome.find_element(*self.ALERT).click()
        # Switch the control to the Alert window
        obj = self.chrome.switch_to.alert
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        time.sleep(3)
        # use the accept() method to accept the alert
        obj.accept()
        print("Clicked on the OK Button in the Alert Window")

    def test_confirm_ok(self):
        self.chrome.find_element(*self.CONFRIM).click()
        # Switch the control to the Confirm window
        obj = self.chrome.switch_to.alert
        # Retrieve the message on the Confirm window
        message = obj.text
        print("Alert shows following message: " + message)
        time.sleep(3)
        # use the accept() method to accept the Confirm
        obj.accept()
        print("Clicked on the OK Button in the Confirm Window")
        time.sleep(3)

    def test_confirm_cancel(self):
        self.chrome.find_element(*self.CONFRIM).click()
        # Switch the control to the Confirm window
        obj = self.chrome.switch_to.alert
        # Retrieve the message on the Confirm window
        message = obj.text
        print("Confirm shows following message: " + message)
        time.sleep(3)
        # use the dismiss() method to cancel the Confirm
        obj.dismiss()
        print("Clicked on the Cancel Button in the Confirm Window")
        time.sleep(3)

    def test_prompt(self):
        self.chrome.find_element(*self.PROMPT).click()
        # Switch the control to the Prompt window
        obj = self.chrome.switch_to.alert
        # Retrieve the message on the Prompt window
        message = obj.text
        print("Prompt shows following message: " + message)
        # Enter text into the Prompt using send_keys()
        obj.send_keys('Andy')
        # use the accept() method to accept the Prompt
        obj.accept()
        print("Clicked on the OK Button in the Prompt Window")
        time.sleep(3)
         