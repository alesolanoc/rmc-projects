import time

from behave import when, then
from core.ui.variables import constants
from core.ui.variables.constants import VALIDATE_REQUIRED_FIELDS_SERVICE
from ibmcloud.ui.pages.rmc.contributor_RMC_page import ContributorRMCPage
from ibmcloud.ui.pages.rmc.dashboard_RMC_page import DashboardRMCPage
from ibmcloud.ui.pages.rmc.success_RMC_page import SuccessRMCPage
from ibmcloud.ui.pages.rmc.summary_RMC_page import SummaryRMCPage


@then('Go to {option} tab')
def step_impl(context, option):
    context.page = SummaryRMCPage(constants.BROWSER)
    context.page.do_action("select tab", option[1:-1].upper())


@then('{resource_name} resource should be displayed at top')
def step_impl(context, resource_name):
    context.page.do_action("resource name label", resource_name[1:-1])


@then('{option} should be displayed for target release')
def step_impl(context, option):
    context.page.do_action("version selected label", option[1:-1])
    time.sleep(2)


@then('{option} should be displayed for type')
def step_impl(context, option):
    context.page.do_action("type selected label", option[1:-1])
    time.sleep(2)


@then('{owner} account should be displayed for first contributor')
def step_impl(context, owner):
    context.page.do_action("first contributor", owner[1:-1])
    time.sleep(2)


@when('Press add contributor button')
def step_impl(context):
    time.sleep(2)
    context.page.do_action("press add contributor button")


@then('Contributor {email} should be displayed in contributor table')
def step_impl(context, email):
    context.page = SummaryRMCPage(constants.BROWSER)
    context.page.do_action("second contributor", email[1:-1])
    time.sleep(2)


@when('Select first resource from table')
def step_impl(context):
    #    context.page = SummaryRMCPage(constants.BROWSER)
    #    context.page = DashboardRMCPage(constants.BROWSER)
    time.sleep(2)
    context.page.do_action("select first resource")
    time.sleep(2)


@then('Press remove contributor')
def step_impl(context):
    context.page.do_action("press remove contributor")
    time.sleep(2)


@then('Contributor should be removed from table')
def step_impl(context):
    context.page = SummaryRMCPage(constants.BROWSER)
    time.sleep(2)
    context.page.do_action("contributor was removed")
    time.sleep(2)


@when('{target} was selected for target release level')
def step_impl(context, target):
    time.sleep(2)
    position = VALIDATE_REQUIRED_FIELDS_SERVICE[0].index(target[1:-1])
    context.page.do_action("select target release version", position)  # VALIDATE_REQUIRED_FIELDS_SERVICE[0][position])


@when('{framework} was selected for service framework version')
def step_impl(context, framework):
    time.sleep(2)
    position = VALIDATE_REQUIRED_FIELDS_SERVICE[1].index(framework[1:-1])
    context.page.do_action("select service framework", position)


@when('{Current_future} date was selected for release date')
def step_impl(context,Current_future):
    time.sleep(2)
    context.page.do_action("select release date",Current_future[1:-1])


@when('{type_service} was selected for type')
def step_impl(context, type_service):
    time.sleep(2)
    position = VALIDATE_REQUIRED_FIELDS_SERVICE[2].index(type_service[1:-1])
    context.page.do_action("select type of service", position)


@when('{brand} was selected for offering category')
def step_impl(context, brand):
    time.sleep(2)
    position = VALIDATE_REQUIRED_FIELDS_SERVICE[3].index(brand[1:-1])
    context.page.do_action("select category", position)


@when('{sub_brand} was selected for sub-category')
def step_impl(context, sub_brand):
    time.sleep(2)
    position = VALIDATE_REQUIRED_FIELDS_SERVICE[4].index(sub_brand[1:-1])
    context.page.do_action("select sub category", position)


@when('Save button was pressed')
def step_impl(context):
    time.sleep(2)
    context.page.do_action("press save button")


@then('{Success} message should be displayed')
def step_impl(context):
    time.sleep(2)
    context.page = SuccessRMCPage(constants.BROWSER)
    time.sleep(2)
    context.page.do_action("success_msg")


@when('Press close button from success popup')
def step_impl(context):
    context.page = SuccessRMCPage(constants.BROWSER)
    time.sleep(2)
    context.page.do_action("press close button")
    time.sleep(2)
    context.page = SummaryRMCPage(constants.BROWSER)


@then('{target} {framework} {service} {category} {sub_category} {current_date} inputs should be displayed')
def step_impl(context, target, framework, service, category, sub_category, current_date):
    category = category.replace("_", " ")
    sub_category = sub_category.replace("_", " ")
    context.page.do_action("verify_inputs", target[1:-1], framework[1:-1], service[1:-1], category[1:-1],
                           sub_category[1:-1], current_date[1:-1])


@when('Go to first resource from table')
def step_impl(context):
    context.page.do_action("go to first resource")


@then(u'Label at top is "{target_release}" for "{release}"')
def step_impl(context, target_release,release):
    context.page.do_action("label_at_top", target_release.upper(),release.upper())


@then(u'Current maturity is "{current_maturity}" for "{target}"')
def step_impl(context, current_maturity, target):
    context.page.do_action("maturity_label", current_maturity[1:-1].upper(), target.upper())


@then(u'Target maturity is "{Target_maturity}" for "{target}"')
def step_impl(context, Target_maturity, target):
    context.page.do_action("target_label", Target_maturity[1:-1].upper(), target.upper())


@then('"{is_value}" should be displayed for composite tag')
def step_impl(context, is_value):
    context.page.do_action("composite_tag", is_value)

@then('"{test}" should be displayed for contained resource types')
def step_impl(context, test):
    context.page.do_action("contaned_resource_types", test)

@then('"{test}" should be displayed for contained resource types2')
def step_impl(context, test):
    context.page.do_action("contaned_resource_types2", test)
