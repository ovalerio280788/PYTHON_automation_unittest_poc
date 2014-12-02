import unittest
from Automation.Framework.BrowserType import BrowserType
from Automation.Framework.TestCase_Super import TestCase_Super
from Automation.Zenoss.Pages.UI import UI

__author__ = 'Oscar Mario'


class test01(TestCase_Super):
    def setUp(self):
        self.ui = UI(BrowserType.firefox)

    def test_Test01(self):
        self.current_Page = self.ui.get_Home_Page().loginWithValidUser().isItOnApplicationPagesValidator()

    def tearDown(self):
        self.current_Page.get_UI().get_driver().close()