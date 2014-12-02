from trace import rx_blank
from selenium.webdriver.common.by import By
from Automation.Framework.UI_Super import UI_Super

__author__ = 'Oscar Mario'


class PageFactory:

    def initElements(self, driver, class_page):
        new_P = class_page
        variables = tuple(set(dir(new_P)))

        for var in variables:
            if "Find_" in var:
                var_value = getattr(new_P, var)
                webElement = self.findElement(driver, var_value[0], var_value[1])
                setattr(new_P, var, webElement)
        return new_P

    def findElement(self, driver, selectorType, selectorValue):
        if selectorType == "xpath":
            return driver.find_element_by_xpath(selectorValue)