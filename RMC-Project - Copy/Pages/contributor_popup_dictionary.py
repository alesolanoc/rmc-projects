from selenium.webdriver.common.by import By

class contributorPage():
    contributor_Label = "Add project contributor"
    locator_dictionary = {
        "contributor_header_label" : (By.CSS_SELECTOR, 'div.bx--modal-header__heading.bx--type-beta'),
        "contributor_input_field" : (By.CSS_SELECTOR, 'input.bx--text-input.bx--text__input'),
        "contributor_submit_button" : (By.CSS_SELECTOR, 'div.relativePosition > button.bx--btn.bx--btn--primary')
    }
    
    class contributorPage1():
    contributor_Label = "Add project contributor"
    locator_dictionary = {
        "contributor_header_label" : (By.CSS_SELECTOR, 'div.bx--modal-header__heading.bx--type-beta'),
        "contributor_input_field" : (By.CSS_SELECTOR, 'input.bx--text-input.bx--text__input'),
        "contributor_submit_button" : (By.CSS_SELECTOR, 'div.relativePosition > button.bx--btn.bx--btn--primary')
    }

