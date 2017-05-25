from gettext import find
from symbol import return_stmt
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webelement import WebElement
from Automation.Framework.Page import Page
from Automation.Framework.PageFactory import PageFactory
from Automation.Zenoss.Pages.ControlCenterApplications import ControlCenterApplications

__author__ = 'Oscar Mario'


class ControlCenterLoginPage(Page):
    
    Find_user = (By.CSS_SELECTOR, "[placeholder='Username']")
    Find_password = (By.CSS_SELECTOR, "[placeholder='Password']")
    Find_btnLogin = (By.CSS_SELECTOR, "[type='submit']")

    def login_with_valid_user(self):
        self.Find_user.send_keys("root")
        self.Find_password.send_keys("D0gP0und!")
        return self.go_to_page(self.Find_btnLogin, ControlCenterApplications())
