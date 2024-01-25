from behave import then
from core.ui.variables import constants
from ibmcloud.ui.pages.rmc.globalCatalog_RMC_page import GlobalCatalogRMCPage
from ibmcloud.ui.pages.rmc.jsonView_RMC_page import jsonViewRMCPage


@then('Go to "{tab}" tab in GC')
def step_impl(context,tab):
    context.page = GlobalCatalogRMCPage(constants.BROWSER)
    context.page.do_action("go to tab in GC",tab)

@then('Go to "{language}" language tab')
def step_impl(context,language):
    context.page.do_action("go to language tab",language)

@then('Get GC content values')
def step_impl(context):
    context.page.do_action("get content values")

@then('Get GC overview values')
def step_impl(context):
    context.page.do_action("get overview values")

@then('Get GC tags values')
def step_impl(context):
    context.page.do_action("get tag values")

@then('Verify that catalog listing values are equal than global catalog')
def step_impl(context):
    context.page.do_action("verify CL against GC")

@then('Press tree dots')
def step_impl(context):
    context.page.do_action("press_tree_dots")

@then('Press Edit action for Json menu')
def step_impl(context):
    context.page.do_action("press_edit_action")

@then('Validate Json script agains Global Catalog')
def step_impl(context):
    context.page = GlobalCatalogRMCPage(constants.BROWSER)
    context.page.do_action("verify jsonGC against GC")

@then('Update content tab values in GC with "{update}"')
def step_impl(context,update):
    context.page.set_form(update_content_values=update)

@then('Update overview tab values in GC with "{update}"')
def step_impl(context,update):
    context.page.set_form(update_overview_values=update)

@then('Press Save button in GC')
def step_impl(context):
    context.page.do_action("press save button")

@then('Go back to RMC page')
def step_impl(context):
    context.page.do_action("go back to RMC")

@then('Get GC content values1')
def step_impl(context):
    context.page.do_action("get content values1")

@then('Validate global catalog against Json script view modal')
def step_impl(context):
    context.page = GlobalCatalogRMCPage(constants.BROWSER)
    context.page.do_action("verify GC against Json script view modal")

@then('Get "{type_service}" label')
def step_impl(context,type_service):
    context.page = GlobalCatalogRMCPage(constants.BROWSER)
    context.page.do_action("get_composite_label",type_service)

@then('Validate "{type_service}" reference "{child}" "{type}" "{tag}" in json script from GC')
def step_impl(context,type_service,child,type,tag):
    context.page = GlobalCatalogRMCPage(constants.BROWSER)
    context.page.do_action("validate_reference",type_service,child,type,tag)

@then('Get GC content values for "{language}"')
def step_impl(context,language):
    context.page = GlobalCatalogRMCPage(constants.BROWSER)
    context.page.do_action("get content values fr",language)
