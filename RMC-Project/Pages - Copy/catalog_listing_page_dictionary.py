from selenium.webdriver.common.by import By

class cataloglistingPage():
    locator_dictionary = {
        "catalog_listing_option" : (By.XPATH, '//div[@id="root"]/div/div[2]/nav/ul/li[3]/span/a/span'),
        "listing_page_tab" : (By.CSS_SELECTOR, 'div.bx--tabs__nav-link'),
        "resource_display_name" : (By.ID, 'service/metadata/displayName'),
        "short_description" : (By.ID, 'service/description'),
        "author" : (By.ID, 'service/metadata/providerDisplayName'),
        "detailted_description" : (By.ID, 'service/metadata/longDescription'),
        "service_icon_url" : (By.ID, 'service/metadata/featuredImageUrl'),
        "documentation_url" : (By.ID, 'service/metadata/documentationUrl'),
        "terms_of_agreenment_url" : (By.ID, 'service/metadata/termsUrl'),
        "settings_tab" : (By.XPATH, '//nav/div/div[2]/div'),
        "management_type_dropdown_menu" : (By.ID, 'service/metadata/type'),
        "management_type_public_option" : (By.XPATH, '//option[@value="Public"]'),
        "instructions_url" : (By.ID, 'service/metadata/instructionsUrl'),
        "supported_url" : (By.ID, 'service/metadata/supportUrl'),
        "bindable_yes" : (By.XPATH, '//div[5]/div/label/span'),
        "require_unique_yes" : (By.XPATH, '//div[7]/div/label/span'),
        "provisionable_yes" : (By.XPATH, '//div/label/span'),
        "plan_changes_yes" : (By.XPATH, '//div[6]/div/label/span'),
        "resource_keys_yes" : (By.XPATH, '//div[8]/div/label/span'),
        "supported_email" : (By.ID, 'service/metadata/supportEmail'),
        "custom_provisioning_url" : (By.ID, 'service/metadata/catalogDetailsUrl'),
        "save_button" : (By.ID, 'serviceMetadataSaveButton'),
        "resource_name_header" : (By.CSS_SELECTOR, 'h1.bx--detail-page-header-title'),
        "review_offering_link" : (By.LINK_TEXT, 'Review Offering in Global Catalog'),
        "view_json" : (By.CSS_SELECTOR, 'div.bssBtnGroup.flex-end.offering-btn-row > div > button.bx--btn.bx--btn--secondary'),
        "add_feature_button" : (By.CSS_SELECTOR, 'div.whitePanel > button.bx--btn.bx--btn--primary'),
        "bullet_title" : (By.ID, 'service/metadata/bullets/0/title'),
        "bullet_description" : (By.ID, 'service/metadata/bullets/0/description'),
        "remove_bullet_button" : (By.CSS_SELECTOR, 'div.feature-bullet > button.bx--btn.bx--btn--primary'),
        "add_media_button" : (By.XPATH, '//div[2]/button[2]'),
        "media_type" : (By.ID, 'service/metadata/media/0/type'),
        "media_option" : (By.XPATH, '//option[@value="image"]'),
        "media_thumbnail" : (By.ID, 'service/metadata/media/0/thumbnailUrl'),
        "media_url" : (By.ID, 'service/metadata/media/0/url'),
        "media_caption" : (By.ID, 'service/metadata/media/0/caption'),
        "remove_media" : (By.XPATH, '//div[4]/button'),
        "import_from_gc" : (By.CSS_SELECTOR, 'div.bssBtnGroup.flex-end.offering-btn-row > button.bx--btn.bx--btn--secondary')
    }

from selenium.webdriver.common.by import By

class accessIAMPage():
    locator_dictionary = {
        "access_IAM_option" : (By.XPATH, '//div[@id="root"]/div/div[2]/nav/ul/li[5]/span/a/span'),
        "required_tab" : (By.CSS_SELECTOR, 'div.bx--tabs__nav-link'),
        "iam_integration_yes" : (By.XPATH, '//div[@id="content"]/div/div/div[2]/div/div/div[2]/div/div/div/form/div/div/label/span'),
        "iam_integration_no" : (By.XPATH, '//div[@id="content"]/div/div/div[2]/div/div/div[2]/div/div/div/form/div/div/label[2]/span'),
        "iam_integratio_save_button" : (By.ID, 'iamIntegrationSaveButton'),
        "status_button" : (By.ID, 'statusButton'),
        "enable_iam" : (By.ID, 'enableIAMButton'),
        "close_button" : (By.ID, 'enableIamModal_closeButton'),
        "close_button_status_popup" : (By.ID, 'statusModal_closeButton')

    }
