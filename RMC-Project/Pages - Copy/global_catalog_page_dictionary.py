from selenium.webdriver.common.by import By

class globalcatalogPage():
    locator_dictionary = {
        "display_name" : (By.ID, 'en-display-name-input'),
        "description" : (By.ID, 'en-desc-textarea'),
        "long_description" : (By.ID, 'en-long-desc-textarea'),
        "media_caption" : (By.ID, 'en-0-media-caption-input'),
        "media_type" : (By.ID, 'en-0-media-type-input'),
        "media_url" : (By.ID, 'en-0-media-url-input'),
        "bullet_title_field" : (By.ID, 'en-0-bullet-title'),
        "bullet_title" : (By.ID, 'en-0-bullet-title-input'),
        "bullet_description_field" : (By.ID, 'en-0-bullet-desc'),
        "bullet_description" : (By.ID, 'en-0-bullet-desc-input'),
        "content_tab" : (By.ID, 'content-link'),
        "overview_tab" : (By.ID, 'overview-link'),
        "resource_name" : (By.ID, 'name-input'),
        "author" : (By.XPATH, '//div[@id="overview-panel"]/div/div/div[3]/div[2]/p'),
        "provisioning_url" : (By.ID, 'catalog-details-url-input'),
        "documentaton_url" : (By.ID, 'doc-url-input'),
        "terms_url" : (By.ID, 'terms-url-input'),
        "instructions_url" : (By.ID, 'instructions-url-input'),
        "three_dots_menu": (By.CSS_SELECTOR, 'svg.bx--overflow-menu__icon'),
        "edit_option": (By.ID, 'edit-json-btn'),
        "en_languaje": (By.LINK_TEXT, 'en'),
        "display_name-en": (By.ID, 'en-display-name-input'),
        "description-en": (By.ID, 'en-desc-textarea'),
        "long_description-en": (By.ID, 'en-long-desc-textarea'),
        "media_caption-en": (By.ID, 'en-0-media-caption-input'),
        "media_type-en": (By.ID, 'en-0-media-type-input'),
        "media_url-en": (By.ID, 'en-0-media-url-input'),
        "bullet_title_field-en": (By.ID, 'en-0-bullet-title'),
        "bullet_title-en": (By.ID, 'en-0-bullet-title-input'),
        "bullet_description_field-en": (By.ID, 'en-0-bullet-desc'),
        "bullet_description-en": (By.ID, 'en-0-bullet-desc-input'),
        "fr_languaje": (By.LINK_TEXT, 'fr'),
        "display_name-fr": (By.ID, 'fr-display-name-input'),
        "description-fr": (By.ID, 'fr-desc-textarea'),
        "long_description-fr": (By.ID, 'fr-long-desc-textarea'),
        "media_caption-fr": (By.ID, 'fr-0-media-caption-input'),
        "media_type-fr": (By.ID, 'fr-0-media-type-input'),
        "media_url-fr": (By.ID, 'fr-0-media-url-input'),
        "bullet_title_field-fr": (By.ID, 'fr-0-bullet-title'),
        "bullet_title-fr": (By.ID, 'fr-0-bullet-title-input'),
        "bullet_description_field-fr": (By.ID, 'fr-0-bullet-desc'),
        "bullet_description-fr": (By.ID, 'fr-0-bullet-desc-input'),
        "save_button" : (By.ID, 'save-btn')
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



