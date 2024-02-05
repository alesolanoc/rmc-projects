import time

from behave import when, then
from Pages.access_iam_page_dictionary import accessIAMPage


@when(u'Go to access iam page')
def go_to_access_page(context):
    context.element = context.web.find_element(*accessIAMPage.locator_dictionary['access_IAM_option'])
    context.element.click()
    time.sleep(3)

@when(u'Go to required tab')
def go_required_tab(context):
    context.element = context.web.find_element(*accessIAMPage.locator_dictionary['required_tab'])
    context.element.click()
    time.sleep(3)

@when(u'Select {option} for iam integration settings')
def select_for_integration(context,option):
    option = option[1:-1].upper()
    if (option == "YES"):
        context.element = context.web.find_element(*accessIAMPage.locator_dictionary['iam_integration_yes'])
    elif (option == "NO"):
        context.element = context.web.find_element(*accessIAMPage.locator_dictionary['iam_integration_no'])
    context.element.click()
    time.sleep(1)

@when(u'Press save button for for iam integration settings')
def press_save_button_iam_integ(context):
    context.element = context.web.find_element(*accessIAMPage.locator_dictionary['iam_integratio_save_button'])
    context.element.click()
    time.sleep(10)


@when(u'Press enable IAM button')
def press_enable_iam(context):
    context.element = context.web.find_element(*accessIAMPage.locator_dictionary['enable_iam'])
    context.element.click()
    time.sleep(20)


@then(u'validate that status is approved {where}')
def validate_status(context,where):
    where = where[1:-1].upper()
    main_page = context.web.current_window_handle
    main_window_handle = None
    time.sleep(5)
    i = 0
    try:
        ids = context.web.find_elements_by_xpath("//*[@id='approved']")
        for li in ids:
            print(li.get_attribute("name"))
            print(li.get_attribute("aria-label"))
            i = i + 1
    except AssertionError as e:
        print(str(e))
    if (i < 6):
        print("Completed steps were not completed.")
        raise AssertionError("ERROR: ", True , False)
    if (where == "enabling"):
        context.element = context.web.find_element(*accessIAMPage.locator_dictionary['enableIamModal_closeButton'])
        context.element.click()
    elif (where == "status"):
        context.element = context.web.find_element(*accessIAMPage.locator_dictionary['close_button_status_popup'])
        context.element.click()
    time.sleep(3)
    context.web.switch_to.window(main_page)
    time.sleep(2)


@then(u'Click status button')
def click_status(context):
    context.element = context.web.find_element(*accessIAMPage.locator_dictionary['status_button'])
    context.element.click()
    time.sleep(3)


