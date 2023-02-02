import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Table(unittest.TestCase):

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.delete_all_cookies()
        self.chrome.maximize_window()
        self.chrome.get('https://www.softwaretestingmaterial.com/sample-webpage-to-automate/')
        self.chrome.implicitly_wait(30)

    def tearDown(self):
        self.chrome.quit()

    def test_table(self):
        # check the number of rows in table
        table_rows = self.chrome.find_elements(By. TAG_NAME, 'tr')
        len_table_rows = len(table_rows)
        print(f'The table has {len_table_rows} rows.')

        # check the number of columns in table
        table_columns = self.chrome.find_elements(By.TAG_NAME, 'th')
        len_table_columns = len(table_columns)
        print(f'The table has {len_table_columns} columns.')

        # print cell text
        c = self.chrome.find_elements(By.TAG_NAME, 'tr')
        for i in c:
            print(i.text)






