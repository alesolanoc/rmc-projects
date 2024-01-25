import time

from behave import when, then
from core.ui.variables import constants
from ibmcloud.ui.pages.rmc.part_creation_popup import PartPopupRMCPage
from ibmcloud.ui.pages.rmc.pricingPlan_RMC_page import PricingPlanRMCPage


@when('Select "{option}" tab from pricing plan')
def step_impl(context,option):
    context.page = PricingPlanRMCPage(constants.BROWSER)
    context.page.do_action("select tab",option)
    time.sleep(2)

@when('Press "{button}" button from pricing plan')
def step_impl(context,button):
    context.page.do_action("press_add_part",button)
    time.sleep(2)

@when('Select "{option}" from choose new experience popup')
def step_impl(context,option):
    context.page = PartPopupRMCPage(constants.BROWSER)
    context.page.do_action("choose_new_experience",option)
    time.sleep(2)

@when('Press "{button}" button from choose new experience popup')
def step_impl(context,button):
    context.page.do_action("press_next_button",button)
    time.sleep(2)

@when('Select "{option}" from choose part type popup')
def step_impl(context,option):
    context.page = PartPopupRMCPage(constants.BROWSER)
    context.page.do_action("choose_part_type",option)
    time.sleep(2)

@when('Press "{button}" button from choose part type popup')
def step_impl(context,button):
    context.page.do_action("press_next_button",button)
    time.sleep(2)

@when('Select "{option}" from choose priced setting')
def step_impl(context,option):
    context.page = PartPopupRMCPage(constants.BROWSER)
    context.page.do_action("choose_price_setting",option)
    time.sleep(2)

@when('Press "{button}" button from choose priced setting popup')
def step_impl(context,button):
    context.page.do_action("press_next_button",button)
    time.sleep(2)

@when('Select "{option}" from add new part')
def step_impl(context,option):
    context.page = PartPopupRMCPage(constants.BROWSER)
    context.page.do_action("choose_new_part",option)
    time.sleep(2)

@when('Press "{button}" button from add new part popup')
def step_impl(context,button):
    context.page.do_action("press_next_button",button)
    time.sleep(2)

@then('Part number should be "{part_number}"')
def step_impl(context,part_number):
    context.page.do_action("part_number",part_number)
    time.sleep(2)

@when('Select "{region}" region from dropdown menu')
def step_impl(context,region):
    context.page = PartPopupRMCPage(constants.BROWSER)
    context.page.do_action("dropdown_menu",region)
    time.sleep(2)
    context.page.do_action("select_default_option",region)
    time.sleep(2)

@when('Select "{invoice}" invoice part number')
def step_impl(context,invoice):
    context.page.do_action("invoice_menu",invoice)
    time.sleep(2)
    context.page.do_action("select_invoice_option",invoice)
    time.sleep(2)

@when('"{current}" date was selected for effective from date')
def step_impl(context,current):
    context.page.do_action("select_date",current)
    time.sleep(2)

@when('Fill part description with "{description}" for "{pos}" part')
def step_impl(context,description,pos):
    context.page = PartPopupRMCPage(constants.BROWSER)
    if (pos.upper() == "FIRST"):
        context.page.set_form(fill_description=description)
        time.sleep(2)
    elif (pos.upper() == "SECOND"):
        context.page.set_form(fill_description_1=description)
        time.sleep(2)

@when('Fill product name with "{product_name}"')
def step_impl(context,product_name):
    context.page.set_form(fill_product_name=product_name)
    time.sleep(2)

@when('Fill product tradename with "{product_tradename}"')
def step_impl(context,product_tradename):
    context.page.set_form(fill_product_tradename=product_tradename)
    time.sleep(2)

@when('Press edit metric button')
def step_impl(context):
    context.page.do_action("edit_metric_button")
    time.sleep(2)

@when('Select "{option}" from custom metric')
def step_impl(context,option):
    context.page = PartPopupRMCPage(constants.BROWSER)
    context.page.do_action("select_custom_metric",option)
    time.sleep(2)

@when('Click over metric grouping dropdown menu')
def step_impl(context):
    context.page.do_action("metric_grouping")
    time.sleep(2)

@then('Select "{option}" from metric grouping dropdown menu')
def step_impl(context,option):
    context.page.do_action("select_metric_option",option)
    time.sleep(2)

@when('Click over metric dropdown menu')
def step_impl(context):
    context.page.do_action("metric_option")
    time.sleep(2)

@then('Select "{option}" from metric dropdown menu')
def step_impl(context,option):
    context.page.do_action("select_option",option)
    time.sleep(2)

@when('"{button}" button was pressed from edit metric popup')
def step_impl(context,button):
    context.page.do_action("press_button_from_edit_metric",button)
    time.sleep(2)

@then('Press "{button}" button from part popup')
def step_impl(context,button):
    context.page = PartPopupRMCPage(constants.BROWSER)
    context.page.do_action("press_publish_pricing_button",button)
    time.sleep(2)

@then('Search "{part}" in filter criteria field')
def step_impl(context,part):
    context.page = PricingPlanRMCPage(constants.BROWSER)
    context.page.do_action("search_part",part)
    time.sleep(2)

@then('Verify that "{part}" part is displayed in "{pos}" row')
def step_impl(context,part,pos):
    context.page.do_action("verify_part",part,pos)
    time.sleep(2)

@then('Verify that "{region}" region is displayed for "{pos}" row')
def step_impl(context,region,pos):
    context.page.do_action("verify_region",region,pos)
    time.sleep(2)

@then('Verify that "{type}" type is displayed for "{pos}" row')
def step_impl(context,type,pos):
    context.page.do_action("verify_type",type,pos)
    time.sleep(2)

@then('Verify that "{part}" part was "{status}" for "{pos}" row')
def step_impl(context,part,status,pos):
    context.page.do_action("verify_part_status",part,status,pos)
    time.sleep(2)

@then('select "{model}" from pricing model')
def step_impl(context,model):
    context.page.do_action("select_pricing_model",model)
    time.sleep(2)

@then('Input "{value}" for charge unit quantity')
def step_impl(context,value):
    context.page.set_form(charge_unit_quantity=value)
    time.sleep(2)

@then('Input "{value}" for usa price')
def step_impl(context,value):
    context.page.set_form(usa_price=value)
    time.sleep(2)

@then('Input "{value}" for upper limit')
def step_impl(context,value):
    context.page.set_form(upper_limit=value)
    time.sleep(2)

@then('Press View Json button from part page')
def step_impl(context):
    context.page = PricingPlanRMCPage(constants.BROWSER)
    context.page.do_action("press_view_json_button")
    time.sleep(2)

@then('Press Edit action for "{part}" part')
def step_impl(context,part):
    context.page = PricingPlanRMCPage(constants.BROWSER)
    context.page.do_action("press_edit",part)
    time.sleep(2)

@then('Get values from "{part}" part')
def step_impl(context,part):
    context.page = PricingPlanRMCPage(constants.BROWSER)
    context.page.do_action("get_values_row",part)
    time.sleep(2)

@then('Get values from define popup for "{part}" part')
def step_impl(context,part):
    context.page = PartPopupRMCPage(constants.BROWSER)
    context.page.do_action("get_values_from_popup",part)
    time.sleep(2)

@then('Press edit metric button')
def step_impl(context):
    context.page.do_action("press_edit_metric")
    time.sleep(2)

@then('Verify that json values are equal than "{part}" part')
def step_impl(context,part):
    context.page = PricingPlanRMCPage(constants.BROWSER)
    context.page.do_action("verify_values",part)
    time.sleep(2)

@then('Press "{action}" action for "{part}" part')
def step_impl(context,action,part):
    context.page = PricingPlanRMCPage(constants.BROWSER)
    context.page.do_action("edit_action",action,part)
    time.sleep(2)

@when('Press duplicate button for second part')
def step_impl(context):
    context.page = PricingPlanRMCPage(constants.BROWSER)
    context.page.do_action("press_duplicate")
    time.sleep(2)
