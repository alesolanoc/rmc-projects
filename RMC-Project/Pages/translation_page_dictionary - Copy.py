from selenium.webdriver.common.by import By

class translationPage():
    locator_dictionary = {
        "translation_option" : (By.XPATH, '//div[@id="root"]/div/div[2]/nav/ul/li[14]/span/a/span'),
        "json_view_modal": (By.CSS_SELECTOR, 'textarea.ace_text-input'),
        "expand_example_script_button" : (By.CSS_SELECTOR, 'button.accordion_button'),
        "copy_button" : (By.CSS_SELECTOR, 'div.bx--snippet.bx--snippet--code > button.bx--snippet-button > svg.bx--snippet__icon'),
        "save_button" : (By.XPATH, '//div[@id="content"]/div/div[3]/div/button[2]')
    }

