import time

from behave import when, then
from core.ui.variables import constants
from ibmcloud.ui.pages.rmc.translation_RMC_page import TranslationRMCPage


@then('Expand sample json icon')
def step_impl(context):
    context.page = TranslationRMCPage(constants.BROWSER)
    context.page.do_action("expand_sample_json")

@then('Press copy icon')
def step_impl(context):
    context.page.do_action("copy_sample")

@then('Press Save Json button')
def step_impl(context):
    context.page = TranslationRMCPage(constants.BROWSER)
    context.page.do_action("press_save_button")

@then('Verify that translation script is equal than CL')
def step_impl(context):
    context.page = TranslationRMCPage(constants.BROWSER)
    context.page.do_action("verify_translation_script_equal_CL")

@then('Verify that translation script is equal than json from CL')
def step_impl(context):
    context.page = TranslationRMCPage(constants.BROWSER)
    context.page.do_action("verify_translation_script_equal_json_from_CL")

@then('Verify that translation script is equal than global catalog values')
def step_impl(context):
    context.page = TranslationRMCPage(constants.BROWSER)
    context.page.do_action("verify_translation_script_equal_than_GC")

@then('Verify that translation script is equal than json script from global catalog')
def step_impl(context):
    context.page = TranslationRMCPage(constants.BROWSER)
    context.page.do_action("verify_translation_equal_than_json_script_from_gc")

@then('Verify that translation script with new "{language}" language is equal than json from CL')
def step_impl(context,language):
    context.page = TranslationRMCPage(constants.BROWSER)
    context.page.do_action("verify_translation_with_new_language_equal_than_json_script_from_CL",language)

@then('Verify that translation script with new "{language}" is equal than global catalog values')
def step_impl(context,language):
    context.page = TranslationRMCPage(constants.BROWSER)
    context.page.do_action("verify_translation_with_new_language_equal_than_global_catalog_values",language)

@then('Verify that translation script with new "{language}" is equal than json script from global catalog')
def step_impl(context,language):
    context.page = TranslationRMCPage(constants.BROWSER)
    context.page.do_action("verify_translation_with_new_language_equal_than_json_script_from_gc",language)

@then('verify11')
def step_impl(context):
    context.page = TranslationRMCPage(constants.BROWSER)
    context.page.do_action("verify11")
