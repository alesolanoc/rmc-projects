import datetime
import time

from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage


class DashboardRMCPage(FormPage,ActionPage):
    dashboard_dictionary = {
        'dashboard_RMC_page_header_label': 'h4.bx--data-table-v2-header',
        'dashboard_RMC_page_filter_resource': '#dashboard-text-input',
        'dashboard_RMC_page_filter_label': 'div.dashboard-table > div.bx--form-item > label.bx--label',
        'dashboard_RMC_new_resource_button': 'div.table-buttons > button.bx--btn.bx--btn--primary',
        'dashboard_RMC_resource_name_column_header': '//th',
        'dashboard_RMC_owner_column_header': '//th[2]',
        'dashboard_RMC_release_date_column_header': '//th[3]',
        'dashboard_RMC_all_resources_rows': '//tr',
        'dashboard_RMC_all_resources_columnns': '//tr[2]/td',
        'dashboard_RMC_getting_started_link': 'p > a.bx--link',
        'dashboard_RMC_first_resource': 'tr.bx--table-row.bx--parent-row.bx--parent-row--even > td',
        'dashboard_RMC_remove_icon': 'svg[name=\"icon--delete--glyph\"] > path',
        'dashboard_RMC_create_resource': 'div.table-buttons > button.bx--btn.bx--btn--primary',
        'dashboard_RMC_resource_name_first_row': 'tr.bx--table-row.bx--parent-row.bx--parent-row--even > td',
        'dashboard_RNC_owner_first_row': '//td[2]',
        'dashboard_RNC_release_date_first_row': '//td[3]'
    }

    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "dashboard_filter_resource": lambda value: self.set_FilterValue(value)
        }
        actions = {
            "dashboard title header": lambda value: self.is_there_dashboard_label(value),
            "dashboard filter label": lambda value: self.is_there_filter_label(value),
            "dashboard new resource button" : lambda value: self.is_there_new_resource_button(value),
            "dashboard resource name column header": lambda value: self.is_there_resource_name_column_header(value),
            "dashboard owner column header": lambda value: self.is_there_owner_column_header(value),
            "dashboard release date column header": lambda value: self.is_there_release_date_column_header(value),
            "dashboard all resources": lambda: self.is_there_resources(),
            "dashboard resorce name column" : lambda value: self.is_there_column(value),
            "dashboard owner column": lambda value: self.is_there_column(value),
            "dashboard getting started link": lambda: self.is_there_getting_started_popup(),
            "dashboard select first resource": lambda value1,value2: self.is_there_first_resource(value1,value2),
            "dashboard press remove icon": lambda: self.is_there_remove_icon(),
            "removed resource is not displayed": lambda: self.is_there_resource(),
            "dashboard press new resource": lambda: self.press_new_resource(),
            "get resouce_name_first row": lambda value: self.first_row_resource_name(value),
            "get owner_first row": lambda value: self.first_row_owner(value),
            "get release_date_first row": lambda value: self.first_row_release_date(value),
            "go to first resource": lambda: self.go_to_first_resource_from_table()
        }
        self.update_form_fields(**fields)
        self.update_actions(**actions)

    def is_there_dashboard_label(self, value):
        if (self.get_value(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_page_header_label']).upper() != value):
            raise AssertionError ("---> ERROR: " + self.get_value((DashboardRMCPage.dashboard_dictionary['dashboard_RMC_page_header_label']).upper()) + " --Not equals-- " + value)

    def is_there_filter_label(self, value):
        if (self.get_value(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_page_filter_label']).upper() != value):
            raise AssertionError ("---> ERROR: " + self.get_value((DashboardRMCPage.dashboard_dictionary['dashboard_RMC_page_filter_label']).upper()) + " --Not equals-- " + value)

    def is_there_new_resource_button(self, value):
        if (self.get_value(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_new_resource_button']).upper() != value):
            raise AssertionError("---> ERROR: " + self.get_value((DashboardRMCPage.dashboard_dictionary['dashboard_RMC_new_resource_button']).upper()) + " --Not equals-- " + value)

    def is_there_resource_name_column_header(self, value):
        if (self.get_value(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_resource_name_column_header']).upper() != value):
            raise AssertionError("---> ERROR: " + self.get_value((DashboardRMCPage.dashboard_dictionary['dashboard_RMC_resource_name_column_header']).upper()) + " --Not equals-- " + value)

    def is_there_owner_column_header(self, value):
        if (self.get_value(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_owner_column_header']).upper().upper() != value):
            raise AssertionError("---> ERROR: " + self.get_value((DashboardRMCPage.dashboard_dictionary['dashboard_RMC_owner_column_header']).upper()) + " --Not equals-- " + value)

    def is_there_release_date_column_header(self, value):
        if (self.get_value(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_release_date_column_header']).upper() != value):
            raise AssertionError("---> ERROR: " + self.get_value((DashboardRMCPage.dashboard_dictionary['dashboard_RMC_release_date_column_header']).upper()) + " --Not equals-- " + value)

    def is_there_resources(self):
        noOfRows = len(self.find_elements(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_all_resources_rows'])) - 1
        # get number of columns
        noOfColumns = len(self.find_elements(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_all_resources_columnns']))
        allData = []
        # iterate over the rows, to ignore the headers we have started the i with '1'
        for i in range(2, noOfRows):
            # reset the row data every time
            ro = []
            # iterate over columns
            for j in range(1, noOfColumns):
                # get text from the i th row and j th column
                ro.append(self.get_value("//tr[" + str(i) + "]/td[" + str(j) + "]"))
            # add the row data to allData of the self.table
            allData.append(ro)
        if (len(allData) < 0):
            raise AssertionError("ERROR: There is no resources ", len(allData), 0)

    def is_there_column(self,value):
        col = self.find_elements("//tr/td[" + str(value) + "]")
        rData = []
        i = 1
        for webElement in col:
            if not webElement.text.strip():
                i = 0
                break
            rData.append(webElement.text)
        return i

    def is_there_getting_started_popup(self):
        self.click(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_getting_started_link'])

    def set_FilterValue(self, value):
        self.click(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_page_filter_resource'])
        self.clear_value(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_page_filter_resource'])
        self.set_value(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_page_filter_resource'], value)
        time.sleep(2)

    def is_there_first_resource(self,value1,value2):
        time.sleep(2)
        if (self.get_value(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_first_resource']) != self.get_attribute_value(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_page_filter_resource']) or value1 != value2):
            raise AssertionError ("---> ERROR: " + value1 + " --Not equals-- " + value2)
        time.sleep(2)

    def is_there_remove_icon(self):
        self.click(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_remove_icon'])

    def is_there_resource(self):
        if self.is_existing(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_first_resource']):
            raise AssertionError("---> ERROR: resource was not removed")

    def press_new_resource(self):
        time.sleep(2)
        self.click(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_create_resource'])
        time.sleep(5)

    def first_row_resource_name(self,value):
        if (self.get_value(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_resource_name_first_row']) != value):
            raise AssertionError ("---> ERROR: " + self.get_value(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_resource_name_first_row']) + " --Not equals-- " + value)

    def first_row_owner(self,value):
        if (self.get_value(DashboardRMCPage.dashboard_dictionary['dashboard_RNC_owner_first_row']) != value):
            raise AssertionError ("---> ERROR: " + self.get_value(DashboardRMCPage.dashboard_dictionary['dashboard_RNC_owner_first_row']) + " --Not equals-- " + value)

    def first_row_release_date(self,value):
        if (value.upper() == 'CURRENT'):
            value = datetime.date.today()
            value = value.strftime("%m/%d/%Y")
            if value[0] == "0":
                value = value[1:]
        if (self.get_value(DashboardRMCPage.dashboard_dictionary['dashboard_RNC_release_date_first_row']) != value):
            raise AssertionError ("---> ERROR: " + self.get_value(DashboardRMCPage.dashboard_dictionary['dashboard_RNC_release_date_first_row']) + " --Not equals-- " + value)

    def go_to_first_resource_from_table(self):
        time.sleep(2)
        self.click(DashboardRMCPage.dashboard_dictionary['dashboard_RMC_first_resource'])
        time.sleep(5)

