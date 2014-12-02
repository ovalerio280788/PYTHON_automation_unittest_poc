from selenium.webdriver.common.by import By

from Automation.Framework.Page import Page


__author__ = 'Oscar Mario'


class ControlCenterApplications (Page):

    Find_labelApplication = (By.XPATH, ".//span[text()='Applications']")

    def isItOnApplicationPagesValidator(self):
        if self.Find_labelApplication.is_displayed():
            print("Label was displayed")
        else:
            print("Label was not displayed")
        return self