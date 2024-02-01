from selenium.webdriver.common.by import By

class gettingStartPage():
    getting_start_link_title_label = "Getting started"
    locator_dictionary = {
        "getting_start_link_title"   : (By.CSS_SELECTOR, 'h2.learningTileHeader'),
        "getting_start_close_button"  : (By.CSS_SELECTOR, 'div.relativePosition > button.bx--btn.bx--btn--secondary')
    }



from selenium.webdriver.common.by import By

class dashboardPage():
    dashboard_title_label = "Resource Onboarded onto IBM Cloud"
    dashboard_filter_label = "Filter resources by name:"
    dashboard_filter_input_field = ""
    dashboard_resource_name_column_title = "RESOURCE NAME"
    dashboard_resource_owner_column_title = "OWNER"
    dashboard_resource_date_column_title = "RELEASE DATE (UTC)"
    locator_dictionary = {
        "dashboard_title"   : (By.CSS_SELECTOR, 'h4.bx--data-table-v2-header'),
        "dashboard_filter"  : (By.CSS_SELECTOR, 'div.dashboard-table > div.bx--form-item > label.bx--label'),
        "dashboard_filter_input" : (By.CSS_SELECTOR, '#dashboard-text-input'),
        "dashboard_resource_name_column" : (By.XPATH, '//th'),
        "dashboard_resource_owner_column": (By.XPATH, '//th[2]'),
        "dashboard_resource_date_column": (By.XPATH, '//th[3]'),
        "dashboard_getting_start_link" : (By.LINK_TEXT, 'Getting started'),
        "dashboard_new_resource_button" : (By.CSS_SELECTOR, 'div.table-buttons > button.bx--btn.bx--btn--primary'),
        "dashboard_table_rows" : (By.XPATH, '//tr'),
        "dashboard_table_columns" : (By.XPATH, '//tr[2]/td'),
        "first_resource" : (By.CSS_SELECTOR, 'tr.bx--table-row.bx--parent-row.bx--parent-row--even > td'),
        "remove_icon" : (By.CSS_SELECTOR, 'svg[name=\"icon--delete--glyph\"] > path'),
        "tableContent" : (By.XPATH, '//div[@id="content"]/div/div/div[2]/div/table')
    }



from selenium.webdriver.common.by import By

class dashboardPage():
    dashboard_title_label = "Resource Onboarded onto IBM Cloud"
    dashboard_filter_label = "Filter resources by name:"
    dashboard_filter_input_field = ""
    dashboard_resource_name_column_title = "RESOURCE NAME"
    dashboard_resource_owner_column_title = "OWNER"
    dashboard_resource_date_column_title = "RELEASE DATE (UTC)"
    locator_dictionary = {
        "dashboard_title"   : (By.CSS_SELECTOR, 'h4.bx--data-table-v2-header'),
        "dashboard_filter"  : (By.CSS_SELECTOR, 'div.dashboard-table > div.bx--form-item > label.bx--label'),
        "dashboard_filter_input" : (By.CSS_SELECTOR, '#dashboard-text-input'),
        "dashboard_resource_name_column" : (By.XPATH, '//th'),
        "dashboard_resource_owner_column": (By.XPATH, '//th[2]'),
        "dashboard_resource_date_column": (By.XPATH, '//th[3]'),
        "dashboard_getting_start_link" : (By.LINK_TEXT, 'Getting started'),
        "dashboard_new_resource_button" : (By.CSS_SELECTOR, 'div.table-buttons > button.bx--btn.bx--btn--primary'),
        "dashboard_table_rows" : (By.XPATH, '//tr'),
        "dashboard_table_columns" : (By.XPATH, '//tr[2]/td'),
        "first_resource" : (By.CSS_SELECTOR, 'tr.bx--table-row.bx--parent-row.bx--parent-row--even > td'),
        "remove_icon" : (By.CSS_SELECTOR, 'svg[name=\"icon--delete--glyph\"] > path'),
        "tableContent" : (By.XPATH, '//div[@id="content"]/div/div/div[2]/div/table')
    }



from selenium.webdriver.common.by import By

class dashboardPage():
    dashboard_title_label = "Resource Onboarded onto IBM Cloud"
    dashboard_filter_label = "Filter resources by name:"
    dashboard_filter_input_field = ""
    dashboard_resource_name_column_title = "RESOURCE NAME"
    dashboard_resource_owner_column_title = "OWNER"
    dashboard_resource_date_column_title = "RELEASE DATE (UTC)"
    locator_dictionary = {
        "dashboard_title"   : (By.CSS_SELECTOR, 'h4.bx--data-table-v2-header'),
        "dashboard_filter"  : (By.CSS_SELECTOR, 'div.dashboard-table > div.bx--form-item > label.bx--label'),
        "dashboard_filter_input" : (By.CSS_SELECTOR, '#dashboard-text-input'),
        "dashboard_resource_name_column" : (By.XPATH, '//th'),
        "dashboard_resource_owner_column": (By.XPATH, '//th[2]'),
        "dashboard_resource_date_column": (By.XPATH, '//th[3]'),
        "dashboard_getting_start_link" : (By.LINK_TEXT, 'Getting started'),
        "dashboard_new_resource_button" : (By.CSS_SELECTOR, 'div.table-buttons > button.bx--btn.bx--btn--primary'),
        "dashboard_table_rows" : (By.XPATH, '//tr'),
        "dashboard_table_columns" : (By.XPATH, '//tr[2]/td'),
        "first_resource" : (By.CSS_SELECTOR, 'tr.bx--table-row.bx--parent-row.bx--parent-row--even > td'),
        "remove_icon" : (By.CSS_SELECTOR, 'svg[name=\"icon--delete--glyph\"] > path'),
        "tableContent" : (By.XPATH, '//div[@id="content"]/div/div/div[2]/div/table')
    }



from selenium.webdriver.common.by import By

class dashboardPage():
    dashboard_title_label = "Resource Onboarded onto IBM Cloud"
    dashboard_filter_label = "Filter resources by name:"
    dashboard_filter_input_field = ""
    dashboard_resource_name_column_title = "RESOURCE NAME"
    dashboard_resource_owner_column_title = "OWNER"
    dashboard_resource_date_column_title = "RELEASE DATE (UTC)"
    locator_dictionary = {
        "dashboard_title"   : (By.CSS_SELECTOR, 'h4.bx--data-table-v2-header'),
        "dashboard_filter"  : (By.CSS_SELECTOR, 'div.dashboard-table > div.bx--form-item > label.bx--label'),
        "dashboard_filter_input" : (By.CSS_SELECTOR, '#dashboard-text-input'),
        "dashboard_resource_name_column" : (By.XPATH, '//th'),
        "dashboard_resource_owner_column": (By.XPATH, '//th[2]'),
        "dashboard_resource_date_column": (By.XPATH, '//th[3]'),
        "dashboard_getting_start_link" : (By.LINK_TEXT, 'Getting started'),
        "dashboard_new_resource_button" : (By.CSS_SELECTOR, 'div.table-buttons > button.bx--btn.bx--btn--primary'),
        "dashboard_table_rows" : (By.XPATH, '//tr'),
        "dashboard_table_columns" : (By.XPATH, '//tr[2]/td'),
        "first_resource" : (By.CSS_SELECTOR, 'tr.bx--table-row.bx--parent-row.bx--parent-row--even > td'),
        "remove_icon" : (By.CSS_SELECTOR, 'svg[name=\"icon--delete--glyph\"] > path'),
        "tableContent" : (By.XPATH, '//div[@id="content"]/div/div/div[2]/div/table')
    }



