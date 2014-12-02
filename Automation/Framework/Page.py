from Automation.Framework.PageFactory import PageFactory

__author__ = 'Oscar Mario'


class Page():

    def go_To_Page(self, btn, page):
        btn.click()
        page = PageFactory().initElements(self.get_UI().get_driver(), page)
        page.set_UI(self.get_UI())
        return page

    def set_UI(self, ui):
        self.__ui = ui

    def get_UI(self):
        return  self.__ui