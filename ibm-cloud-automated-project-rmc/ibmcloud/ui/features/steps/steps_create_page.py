import time

from behave import when, then
from core.ui.variables import constants
from ibmcloud.ui.pages.rmc.create_new_resource_RMC_page import CreateNewResourceRMCPage

@then('{Create_a_new_resource} popup is displayed')
def step_impl(context,Create_a_new_resource):
    global main_page
    main_page = constants.BROWSER.current_window_handle
    context.page = CreateNewResourceRMCPage(constants.BROWSER)
    context.page.do_action("create resource title header",Create_a_new_resource[1:-1].upper())
    time.sleep(2)

@then('{option} for would you like to import')
def step_impl(context,option):
    context.page.do_action("select No for would you like",option[1:-1])

@then('{option} for is your resource going to be a child')
def step_impl(context,option):
    context.page.do_action("select No for is your resource",option[1:-1])

@then('Fill resource name with {resource_name}')
def step_impl(context,resource_name):
    context.page.set_form(create_new_resource_input=resource_name[1:-1])

@then('Select {service} for resource type')
def step_impl(context,service):
    context.page.do_action("select service from service type",service[1:-1])

@then('Press {submit} buttons')
def step_impl(context,submit):
    context.page.do_action("press submit button",submit[1:-1])

@then('Fill composite tag with "{is_value}"')
def step_impl(context,is_value):
    context.page.set_form(input_composite_tag=is_value)

@then('Fill contained resource types with "{test}"')
def step_impl(context,test):
    context.page.set_form(input_composite_child=test)

@then('Fill resource parent name with "{parent_resource}"')
def step_impl(context,parent_resource):
    context.page.set_form(input_resource_parent=parent_resource)

@then('Fill resource child name with "{child_resource}"')
def step_impl(context,child_resource):
    context.page.set_form(input_resource_child=child_resource)



