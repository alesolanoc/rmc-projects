from core.ui.pages.tab_page import TabPage
from core.ui.pages.element_search import ElementSearch


class UserPage(TabPage, ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        pass