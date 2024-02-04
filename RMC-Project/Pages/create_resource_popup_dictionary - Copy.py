from selenium.webdriver.common.by import By

class createResourcePopup():
    create_new_resource_title_label = "Create a new resource",
    locator_dictionary = {
        "create_new_resource_title" : (By.CSS_SELECTOR, 'div.bx--modal-header__heading.bx--type-beta > div'),
        "would_you_like_impor_broker_yes"   : (By.CSS_SELECTOR, 'span.bx--radio-button__appearance'),
        "would_you_like_impor_broker_no"  : (By.XPATH, '//label[2]/span'),
        "is_your_resource_going_to_be_child_yes" : (By.CSS_SELECTOR, 'span > form.bx--form > div.tileText.newResourceForm > div.bx--radio-button-group > label.bx--radio-button__label > span.bx--radio-button__appearance'),
        "is_your_resource_going_to_be_child_no" : (By.XPATH, '//span/form/div/div/label[2]/span'),
        "resource_name": (By.ID, 'newServiceName'),
        "resource_type_dropdown": (By.CSS_SELECTOR, '#newServiceType > option.bx--select-option'),
        "resource_type_service" : (By.XPATH, '//option[@value="service"]'),
        "resource_type_operations_only": (By.XPATH, '//option[@value="operations_only"]'),
        "resource_type_composite": (By.XPATH, '//option[@value="composite"]'),
        "composite_tag" : (By.ID, 'newCompositeTag'),
        "contained_resource_types" : (By.ID, 'newContainedResourceTypes'),
        "composite_parent_name" : (By.ID, 'compositeParentName'),
        "composite_child_name" : (By.ID, 'compositeChildName'),
        "submit_button" : (By.CSS_SELECTOR, 'div.relativePosition > button.bx--btn.bx--btn--primary')
    }



