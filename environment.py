import os
from behaving.environment import *
from behaving import environment as benv

def before_all(context):
    benv.before_all(context)
    context.base_url = "http://localdev.lightnetb.org/"
    context.screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")

def before_scenario(context, scenario):
    context.default_browser = "phantomjs"
    benv.before_scenario(context, scenario)
    context.personas = {
        'Frank' : dict(
            fullname = "Frank",
            email = "frank@example.com",
            password = "password",
            username = "Frank_1"	
        ),
        'Mary' : dict(
            fullname = "Mary",
            email = "mary@example.com",
            password = "password",
            username = "Mary_1"
        )
    }
    context.step_counter = 0

def after_step(context, step):
    context.step_counter += 1
    fullpath = os.path.join(context.screenshot_dir, context.scenario.name, "%s_%s.png" % (context.step_counter, step.name.replace("/","-")))
    if not os.path.exists(os.path.dirname(fullpath)):
        os.makedirs(os.path.dirname(fullpath))
    context.browser.driver.get_screenshot_as_file(fullpath)
    

def after_scenario(context, scenario):
    if context.failed:
        fullpath = os.path.join(context.screenshot_dir, "failed_" + scenario.name + ".png")
        context.browser.driver.get_screenshot_as_file(fullpath)
    benv.after_scenario(context, scenario)