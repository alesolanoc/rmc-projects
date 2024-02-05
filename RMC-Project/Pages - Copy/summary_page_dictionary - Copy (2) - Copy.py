from selenium.webdriver.common.by import By

class summaryPage():
    locator_dictionary = {
        "resource_name_label" : (By.CSS_SELECTOR, 'h1.bx--detail-page-header-title'),
        "target_version_dropdown_menu" : (By.ID, 'version-select'),
        "target_version_GA" : (By.XPATH, '//option[@value="ga"]'),
        "service_framework_dropdown_menu" : (By.ID, 'serviceFramework'),
        "service_framework_3Q2020" : (By.XPATH, '//option[@value="3Q2020"]'),
        "release_date" : (By.CSS_SELECTOR, 'svg[name="calendar"]'),
        "type_dropdown_menu" : (By.ID, 'type'),
        "service_type_option" : (By.XPATH, '//option[@value="service"]'),
        "composite_type_option" : (By.XPATH, '// option[ @ value = "composite"]'),
        "operations_only_type_option" : (By.XPATH, '//option[@value="operations_only"]'),
        "offering_category_dropdown_menu" : (By.ID, 'brand'),
        "3rd_party_option" : (By.XPATH, '//option[@value="3rd Party"]'),
        "sub_brand_dropdown_menu" : (By.ID, 'subBrand'),
        "84_codes" : (By.XPATH, '//option[@value="84 Codes"]'),
        "save_button" : (By.ID, 'summarySaveButton'),
        "contributor_owner_row" : (By.XPATH, '//tr[@id="0column"]/td'),
        "contributor_add_button" : (By.CSS_SELECTOR, 'div.contributorsHeader > button.bx--btn.bx--btn--primary'),
        "contributor_added_row" : (By.XPATH, '//tr[@id="1column"]/td'),
        "contributor_remove_icon" : (By.XPATH, '//tr[@id="1column"]/td'),
        "all_resources" : (By.LINK_TEXT, 'All Resources')
    }

