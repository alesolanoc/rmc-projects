from behave import then

from core.ui.variables import constants
from ibmcloud.ui.pages.rmc.jsonView_RMC_page import jsonViewRMCPage
from ibmcloud.ui.pages.rmc.translation_RMC_page import TranslationRMCPage


@then('Get json script values')
def step_impl(context):
    context.page = jsonViewRMCPage(constants.BROWSER)
    context.page.do_action("copy values")

@then('Get json script values from CL')
def step_impl(context):
    context.page = jsonViewRMCPage(constants.BROWSER)
    context.page.do_action("copy values from GC")

@then('Press close button from json script modal')
def step_impl(context):
    context.page.do_action("press_close_button")

@then('Update Json script with "{update}"')
def step_impl(context,update):
    context.page.do_action("update json values",update)

@then('Save Json script updates')
def step_impl(context):
    context.page.do_action("press save button")

@then('Press cancel button from json script')
def step_impl(context):
    context.page.do_action("press_cancel_button")

@then('update translation values with "{update}"')
def step_impl(context,update):
    context.page = TranslationRMCPage(constants.BROWSER)
    context.page.do_action("update_translation_values",update)

@then('Copy sample into json editor modal')
def step_impl(context):
    context.page = jsonViewRMCPage(constants.BROWSER)
    context.page.do_action("copy values from translation")

@then('Copy sample updated into json editor modal with "{update}"')
def step_impl(context,update):
    context.page = jsonViewRMCPage(constants.BROWSER)
    context.page.do_action("copy values updated from translation",update)

@then('Copy sample updated into json editor modal with new "{language}" language')
def step_impl(context,language):
    context.page = jsonViewRMCPage(constants.BROWSER)
    context.page.do_action("copy values new language from translation",language)

@then('Copy sample updated into json editor modal with new "{language}" language with no updates')
def step_impl(context,language):
    context.page = jsonViewRMCPage(constants.BROWSER)
    context.page.do_action("copy values new language from translation with no updates",language)

@then('Update "{language}" language with "{update}"')
def step_impl(context,language,update):
    context.page = jsonViewRMCPage(constants.BROWSER)
    context.page.do_action("update_language",language,update)

