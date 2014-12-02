from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

__author__ = 'Oscar Mario'


class UI_Super:

    def __init__(self, browser_type):
        if browser_type != "":
            print("SELECTED BROWSER " + browser_type)
            if browser_type == 'firefox':
                self.__driver = webdriver.Firefox()
            elif browser_type == 'chrome':
                self.__driver = webdriver.Chrome()
            elif browser_type == 'Ie':
                self.__driver = webdriver.Ie()
            else:
                self.__driver = None

            self.__driver.maximize_window()
            self.__driver.delete_all_cookies()
            self.__driver.implicitly_wait(100)
            self.__driver.set_page_load_timeout(100)
            print('BROWSER OPENED')
        else:
            self.__driver = self.get_driver()

    def __init_Empty__(self, driver):
        self.__driver = driver
        return self

    def get_driver(self):
        return self.__driver