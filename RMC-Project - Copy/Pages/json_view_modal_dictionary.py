from selenium.webdriver.common.by import By

class jsonviewPage():
    locator_dictionary = {
        "json_view_modal" : (By.CSS_SELECTOR, 'textarea.ace_text-input'),
        "close_json_view" : (By.CSS_SELECTOR, 'div.bx--modal-container.widerModal > div.bx--modal-header > button.bx--modal-close > svg.bx--modal-close__icon > path'),
        "save_button" : (By.ID, 'save-edit-btn')
    }

