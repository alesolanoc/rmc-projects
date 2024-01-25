from core.ui.pages.element import Element


class TabPage(Element):
    def __init__(self, driver):
        super().__init__(driver)
        self._tabs = {}
        self._tab = None

    def update_tabs(self, **tabs):
        for tag in tabs:
            self._tabs[tag] = tabs[tag]

    def go_to(self, tab):
        self._tabs[tab]()

    def do_action(self, value, *params):
        switch = self._tab.do_action(value, *params)
        if switch in self._tabs:
            self.go_to(switch)
            return ''
        return switch

    def do_action_with_value(self, action_id, value):
        switch = self._tab.do_action_with_value(action_id, value)
        if switch in self._tabs:
            self.go_to(switch)
            return ''
        return switch

    def get_tab(self):
        return self._tab

    def set_tab(self, tab):
        self._tab = tab

    def get_tab_level(self):
        current = self
        has_tab = True
        level = -1
        while has_tab:
            if hasattr(current, 'get_tab'):
                current = current.get_tab()
                level += 1
            else:
                has_tab = False
        return level
