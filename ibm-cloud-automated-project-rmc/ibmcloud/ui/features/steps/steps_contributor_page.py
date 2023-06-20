import time

from behave import when, then
from core.ui.variables import constants
from ibmcloud.ui.pages.rmc.contributor_RMC_page import ContributorRMCPage

@when('Fill {contributor} contributor')
def step_impl(context,contributor):
    context.page = ContributorRMCPage(constants.BROWSER)
    time.sleep(2)
    context.page.set_form(input_contributor=contributor[1:-1])

@when('Press add contributor')
def step_impl(context):
    context.page.do_action("press add button")

@then('Press remove button')
def step_impl(context):
    context.page = ContributorRMCPage(constants.BROWSER)
    time.sleep(2)
    context.page.do_action("press remove button")




