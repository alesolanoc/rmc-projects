import time

from behave import given, then, when, step
from json import loads
from os.path import join

from core.ui.variables import constants
from ibmcloud.ibmcloud_dir import ibmcloud_path
from core.ui.utils.set_up_driver import set_up_driver
from ibmcloud.ui.pages.login_page import LoginPage
from ibmcloud.ui.pages.rmc.dashboard_RMC_page import DashboardRMCPage
from ibmcloud.ui.pages.rmc.getting_started_RMC_page import GettingStartedRMCPage
from ibmcloud.ui.pages.rmc.remove_resource_RMC_page import RemoveResourceRMCPage
from ibmcloud.ui.pages.rmc.summary_RMC_page import SummaryRMCPage

CONFIG = loads(open(join(ibmcloud_path, 'config.json')).read())

@given('I login in IBMCloud web application as {username}')
def step_impl(context, username):
    context.tab_level = 0
    global browser
    browser = set_up_driver(CONFIG)
    constants.BROWSER = browser
    context.page = LoginPage(browser)
    time.sleep(5)
    context.page.set_form(sign_in_as=CONFIG.get("USER").get(username).get("EMAIL"))
    context.page.set_form(password=CONFIG.get("USER").get(username).get("PASSWORD"))
    context.page.do_action("Sign In")

@step('Dashboard page is shown')
def step_impl(context):
    context.page = DashboardRMCPage(browser)
    context.page.set_wait(20)

@then('{title_header} should be displayed at the top')
def step_impl(context,title_header):
    context.page.do_action("dashboard title header", title_header[1:-1].upper())

@then('{filter_label} should be displayed at filter section')
def step_impl(context,filter_label):
    context.page.do_action("dashboard filter label", filter_label[1:-1].upper())

@then('{new_resource_button} button should be displayed')
def step_impl(context,new_resource_button):
    context.page.do_action("dashboard new resource button", new_resource_button[1:-1].upper())

@then('{header} column header should be displayed at {position} column')
def step_impl(context,header,position):
    if (position[1:-1].upper() == 'FIRST'):
        context.page.do_action("dashboard resource name column header", header[1:-1].upper())
    elif (position[1:-1].upper() == 'SECOND'):
        context.page.do_action("dashboard owner column header", header[1:-1].upper())
    elif (position[1:-1].upper() == 'THIRD'):
        context.page.do_action("dashboard release date column header", header[1:-1].upper())

@then('All resources are displayed')
def step_impl(context):
    context.page.do_action("dashboard all resources")

@then('All resources should have {column}')
def step_impl(context,column):
    if (column[1:-1].upper() == "RESOUCE NAME"):
        if (context.page.do_action("dashboard resorce name column",1) == 0):
            raise AssertionError("ERROR: Missing a resource name")
    elif (column[1:-1].upper() == "OWNER"):
        if (context.page.do_action("dashboard owner column",2) == 0):
            raise AssertionError("ERROR: Missing an owner")

@then('Getting started popup should be displayed after clicked over its link')
def step_impl(context):
#    global main_page
#    main_page = browser.current_window_handle
    context.page.do_action("dashboard getting started link")
    time.sleep(4)
    context.page = GettingStartedRMCPage(browser)

@then('{Getting_started} should be displayed at the top of the popup')
def step_impl(context,Getting_started):
    context.page.do_action("getting started title header", Getting_started[1:-1].upper())
    time.sleep(2)

@then('after pressed close button dashboard page should be displayed')
def step_impl(context):
    context.page.do_action("getting started close button")
    time.sleep(4)
#    browser.switch_to.window(main_page)
    context.page = DashboardRMCPage(browser)

@then('Filter table should display according filter criteria {filter_criteria}')
def step_impl(context,filter_criteria):
    context.page.set_form(dashboard_filter_resource=filter_criteria[1:-1])
    time.sleep(2)

@then('First {resource} resource should be equal than filter criteria {filter_criteria}')
def step_impl(context,resource,filter_criteria):
    context.page.do_action("dashboard select first resource",resource[1:-1],filter_criteria[1:-1])

@when('Filter by {resource_name}')
def step_impl(context,resource_name):
    context.page.set_form(dashboard_filter_resource=resource_name[1:-1])
    time.sleep(2)

@when('The press remove icon for {resource_name}')
def step_impl(context,resource_name):
    context.page.do_action("dashboard press remove icon")
    time.sleep(2)

@then('{Delete_confirmation_msg} Remove popup should be displayed')
def step_impl(context,Delete_confirmation_msg):
 #   global main_page1
 #   main_page1 = browser.current_window_handle
    time.sleep(2)
    context.page = RemoveResourceRMCPage(browser)
    context.page.do_action("remove confirmation title header",Delete_confirmation_msg[1:-1].upper())
    time.sleep(2)

@then('{resource_name} resource name was confirmed')
def step_impl(context,resource_name):
    context.page.set_form(confirm_resource_name=resource_name[1:-1])
    time.sleep(2)

@then('{resource_name} resource name should be displayed in order to be removed')
def step_impl(context,resource_name):
    context.page.do_action("remove resource should be displayed",resource_name[1:-1])
    time.sleep(2)

@then('Press delete button')
def step_impl(context):
    context.page.do_action("remove resource delete button")
    time.sleep(2)
    context.page = DashboardRMCPage(browser)

@then('Resource should not be displayed in dashboard')
def step_impl(context):
    context.page.do_action("removed resource is not displayed")
    time.sleep(2)

@when('Press new resource button')
def step_impl(context):
    context.page.do_action("dashboard press new resource")
    time.sleep(2)

@then('Go to all resources link')
def step_impl(context):
    context.page = SummaryRMCPage(browser)
    context.page.do_action("all resources link")
    context.page = DashboardRMCPage(browser)

@then('{resource_name} resource should be displayed in resouce name column')
def step_impl(context,resource_name):
    time.sleep(2)
    context.page.do_action("get resouce_name_first row",resource_name[1:-1])

@then('{email} owner should be displayed in owner column')
def step_impl(context,email):
    time.sleep(2)
    context.page.do_action("get owner_first row",email[1:-1])

@then('{Current} date should be displayed in release date column')
def step_impl(context,Current):
    time.sleep(2)
    context.page.do_action("get release_date_first row",Current[1:-1])
