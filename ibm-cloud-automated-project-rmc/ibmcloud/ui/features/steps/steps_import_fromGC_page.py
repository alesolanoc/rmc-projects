import time

from behave import then
from core.ui.variables import constants
from ibmcloud.ui.pages.rmc.import_fromGC_RMC_page import ImportFromRMCPage


@then('Confirm import from GC')
def step_impl(context):
    context.page = ImportFromRMCPage(constants.BROWSER)
    time.sleep(2)
    context.page.do_action("press import confirm button")