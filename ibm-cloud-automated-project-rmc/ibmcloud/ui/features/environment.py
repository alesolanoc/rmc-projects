#from ibmcloud.api.features.steps.functions import delete_items


def after_all(context):
    pass
    #delete_items('user')

def before_all(context):
    pass
    #delete_items('projects')

def after_scenario(context, scenario):
    # driver is being closed here because we login in each scenario
    # when only we login only once it should be closed in after all hook method
    close_driver(context)
    pass

def close_driver(context):
    if context.page is not None:
        context.page.get_driver().quit()

