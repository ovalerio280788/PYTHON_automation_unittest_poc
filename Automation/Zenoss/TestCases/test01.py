from Automation.Framework.BrowserType import BrowserType
from Automation.Framework.TestCaseSuper import TestCaseSuper
from Automation.Zenoss.Pages.UI import UI


class Test01(TestCaseSuper):
    current_Page = None

    def setUp(self):
        self.ui = UI(BrowserType.chrome)

    def test_Test01(self):
        self.current_Page = self.ui.get_home_page().login_with_valid_user().is_on_application_pages_validator()

    def tearDown(self):
        self.current_Page.get_ui().get_driver().close()
