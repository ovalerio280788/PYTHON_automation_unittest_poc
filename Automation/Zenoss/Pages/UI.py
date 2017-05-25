from Automation.Framework.PageFactory import PageFactory
from Automation.Framework.UiSuper import UiSuper
from Automation.Zenoss.Data.Constant import Constant
from Automation.Zenoss.Pages.ControlCenterLoginPage import ControlCenterLoginPage

__author__ = 'Oscar Mario'


class UI(UiSuper):
    def __init__(self, browser_Type):
        print(browser_Type)
        UiSuper.__init__(self, browser_Type)

    def get_home_page(self):
        """self.get_driver().get(Constant.url)
        login = ControlCenterLogin()
        login.set_UI(self)
        return  login"""

        self.get_driver().get(Constant.url)
        login = PageFactory().init_elements(self.get_driver(), ControlCenterLoginPage())
        login.set_ui(self)
        return login
