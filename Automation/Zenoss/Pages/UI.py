from Automation.Framework.PageFactory import PageFactory
from Automation.Framework.UI_Super import UI_Super
from Automation.Zenoss.Data.Constant import Constant
from Automation.Zenoss.Pages.ControlCenterLogin import ControlCenterLogin

__author__ = 'Oscar Mario'


class UI(UI_Super):
    def __init__(self, browser_Type):
        print(browser_Type)
        UI_Super.__init__(self, browser_Type)

    def get_Home_Page(self):
        """self.get_driver().get(Constant.url)
        login = ControlCenterLogin()
        login.set_UI(self)
        return  login"""

        self.get_driver().get(Constant.url)
        login = PageFactory().initElements(self.get_driver(), ControlCenterLogin())
        login.set_UI(self)
        return  login