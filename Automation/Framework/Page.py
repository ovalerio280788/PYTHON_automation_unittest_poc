from Automation.Framework.PageFactory import PageFactory

__author__ = 'Oscar Mario'


class Page:

    __ui = None

    def go_to_page(self, btn, page):
        btn.click()
        page = PageFactory().init_elements(self.get_ui().get_driver(), page)
        page.set_ui(self.get_ui())
        return page

    def set_ui(self, ui):
        self.__ui = ui

    def get_ui(self):
        return self.__ui
