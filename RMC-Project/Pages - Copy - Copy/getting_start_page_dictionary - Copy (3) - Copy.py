from selenium.webdriver.common.by import By

class gettingStartPage():
    getting_start_link_title_label = "Getting started"
    locator_dictionary = {
        "getting_start_link_title"   : (By.CSS_SELECTOR, 'h2.learningTileHeader'),
        "getting_start_close_button"  : (By.CSS_SELECTOR, 'div.relativePosition > button.bx--btn.bx--btn--secondary')
    }



