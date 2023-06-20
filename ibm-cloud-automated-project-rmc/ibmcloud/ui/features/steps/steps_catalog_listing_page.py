import time

from behave import when, then
from core.ui.variables import constants
from ibmcloud.ui.pages.rmc.catalogListing_RMC_page import CatalogListingRMCPage
from ibmcloud.ui.pages.rmc.globalCatalog_RMC_page import GlobalCatalogRMCPage
from ibmcloud.ui.pages.rmc.import_fromGC_RMC_page import ImportFromRMCPage


@when('Go to "{tab}" tab in CL page')
def step_impl(context,tab):
    context.page = CatalogListingRMCPage(constants.BROWSER)
    time.sleep(2)
    context.page.do_action("select tab",tab.upper())

@when('Resource name was filled with "{resource_name}"')
def step_impl(context,resource_name):
    context.page.set_form(resource_name_field=resource_name)

@when('Shot description was filled with "{short}"')
def step_impl(context,short):
    context.page.set_form(short_field=short)

@when('Author was filled with "{author}"')
def step_impl(context,author):
    context.page.set_form(author_field=author)

@when('Detailed description was filled with "{detailed}"')
def step_impl(context,detailed):
    context.page.set_form(detailed_field=detailed)

@when('Service icon URL was filled with "{service_url}"')
def step_impl(context,service_url):
    context.page.set_form(service_url_field=service_url)

@when('Documentation URL was filled with "{documentation_url}"')
def step_impl(context,documentation_url):
    context.page.set_form(documentation_url_field=documentation_url)

@when('Terms URL was filled with "{terms_url}"')
def step_impl(context,terms_url):
    context.page.set_form(terms_url_field=terms_url)

@when('Management type selected is "{management}"')
def step_impl(context,management):
    context.page.do_action("management type",management.upper())

@when('Instructions URL was filled with "{intructions_url}"')
def step_impl(context,intructions_url):
    context.page.set_form(instructions_url_field=intructions_url)

@when('Support URL was filled with "{support_url}"')
def step_impl(context,support_url):
    context.page.set_form(support_url_field=support_url)

@when('Provisionable selected is "{Provision}"')
def step_impl(context,Provision):
    context.page.do_action("provisionable type",Provision.upper())

@when('Bindable selected is "{bindable}"')
def step_impl(context,bindable):
    context.page.do_action("bindable",bindable.upper())

@when('Plan Changes selected is "{plan}"')
def step_impl(context,plan):
    context.page.do_action("plan changes",plan.upper())

@when('Require unique selected is "{requires}"')
def step_impl(context,requires):
    context.page.do_action("requires unique",requires.upper())

@when('Resource keys selected is "{resource}"')
def step_impl(context,resource):
    context.page.do_action("resource kwys",resource.upper())

@when('Support email was filled with "{support_email}"')
def step_impl(context,support_email):
    context.page.set_form(support_email=support_email)

@when('Custom URL was filled with "{custom_url}"')
def step_impl(context,custom_url):
    context.page.set_form(custom_url=custom_url)

@when('Save button was pressed in CL page')
def step_impl(context):
    context.page.do_action("press save button")

@then('Global catalog link should be displayed')
def step_impl(context):
    context.page.do_action("global catalog link")

@then('All required fields in "{tab}" tab should be displayed as filled')
def step_impl(context,tab):
    context.page.do_action("get values from",tab)

@when('Press Add Feature button in optional section')
def step_impl(context):
    context.page.do_action("press add feature")

@when('bullet title was filled with "{bullet_title}"')
def step_impl(context,bullet_title):
    context.page.set_form(bullet_title=bullet_title)

@when('bullet description was filled with "{bullet_description}"')
def step_impl(context,bullet_description):
    context.page.set_form(bullet_description=bullet_description)

@then('Bullets should be displayed as filled')
def step_impl(context):
    context.page.do_action("get bullet values")

@when('Press Delete Feature button in optional section')
def step_impl(context):
    context.page.do_action("press remove feature")

@then('Bullets should not be displayed')
def step_impl(context):
    context.page.do_action("bullets removed")

@when('Press Add Media button in optional section')
def step_impl(context):
    context.page.do_action("press add media")

@when('type of media option was filled with "{image}"')
def step_impl(context,image):
    context.page.do_action("select media type",image)

@when('thumbnail was filled with "{thumbnail}"')
def step_impl(context,thumbnail):
    context.page.set_form(thumbnail_url=thumbnail)

@when('media url was filled with "{media_url}"')
def step_impl(context,media_url):
    context.page.set_form(media_url=media_url)

@when('media caption was filled with "{caption}"')
def step_impl(context,caption):
    context.page.set_form(media_caption=caption)

@then('media should be displayed as filled')
def step_impl(context):
    context.page.do_action("get media values")

@when('Go "{page_up}"')
def step_impl(context,page_up):
    context.page.set_form(go_page=page_up)

@when('Press remove media')
def step_impl(context):
    context.page.do_action("press revmove media")

@then('media should not be displayed as filled')
def step_impl(context):
    context.page.do_action("media revmoved")

@when('Check "{tag}" checkbox')
def step_impl(context,tag):
    context.page.do_action("tag_check",tag)

@then('"{tag}" checkbox should be displayed as checked')
def step_impl(context,tag):
    context.page.do_action("tag_checked",tag)

@when('Uncheck "{tag}" checkbox')
def step_impl(context,tag):
    context.page.do_action("tag_uncheck",tag)

@then('"{tag}" checkbox should be displayed as unchecked')
def step_impl(context,tag):
    context.page.do_action("tag_unchecked",tag)

@then('Press View Json button')
def step_impl(context):
    context.page.do_action("press_view_json")

@when('Get Listing Page values')
def step_impl(context):
    context.page.do_action("get_listing_page_values")

@when('Get Settings values')
def step_impl(context):
    context.page.do_action("get_settings_values")


@then('Verify that catalog listing values are equal than json script modal')
def step_impl(context):
    time.sleep(2)
    context.page = CatalogListingRMCPage(constants.BROWSER)
    context.page.do_action("validate_catalog_listing_agains_json_modal")

@then('Go to global catalog page')
def step_impl(context):
    context.page = CatalogListingRMCPage(constants.BROWSER)
    context.page.do_action("go_to_GC")

@then('Press import button')
def step_impl(context):
    time.sleep(2)
    context.page.do_action("press import button")

@then('Verify that global catalog updates are iqual than imported to catalog listing')
def step_impl(context):
    time.sleep(2)
    context.page.do_action("validate_global_catalog_agains_catalog_listing")

@then('Validate Json script from GC against catalog listing')
def step_impl(context):
    context.page = CatalogListingRMCPage(constants.BROWSER)
    time.sleep(2)
    context.page.do_action("Validate_Json_script_from_GC_against_catalog_listing")

@then('Verify that json script modal values are equal than json script from GC')
def step_impl(context):
    context.page = CatalogListingRMCPage(constants.BROWSER)
    time.sleep(2)
    context.page.do_action("Verify_that_json_script_modal_values_are_equal_than_json_script_from_GC")

@then('Updates all values from "{tab}" with "{update}"')
def step_impl(context,tab,update):
    time.sleep(2)
    context.page.do_action("Updates_all_values_from_catalog_listing",tab,update)

@then('Verify1')
def step_impl(context):
    context.page.do_action("get_listing_page_values12")
