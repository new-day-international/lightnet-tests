from behaving.environment import *
from behaving import environment as benv

def before_all(context):
    benv.before_all(context)
    context.base_url = "http://localdev.lightnetb.org/"

def before_scenario(context, scenario):
    benv.before_scenario(context, scenario)
    context.personas = {
        'Frank' : dict(
            fullname = "Frank",
            email = "frank@email.com",
            password = "password",
            username = "Frank_1"	
        )
    }