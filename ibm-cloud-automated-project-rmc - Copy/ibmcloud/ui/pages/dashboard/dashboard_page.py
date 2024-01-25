import time

from core.ui.pages.action_page import ActionPage
from core.ui.pages.element import Element
from core.ui.pages.tab_page import TabPage
from core.ui.pages.element_search import ElementSearch

dashboard_page_label = '#dashboard-selector'

class DashboardPage(ActionPage,TabPage, ElementSearch,Element):
    def __init__(self, driver):
        super().__init__(driver)

        actions = {
            "Dashboard Label page": lambda: self.is_there_dashboard_label()
        }
        self.update_actions(**actions)

    def is_there_dashboard_label(self):
        print("sdfsfdsfsdfsdfsdfsdf")
        if self.is_existing(dashboard_page_label):
            print("alejoo")
            return DashboardPage(self._driver)