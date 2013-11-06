import time
from behave import when
from behaving.web.steps import *
from behaving.sms.steps import *
from behaving.mail.steps import *
from behaving.personas.steps import *

@given('random new user as the persona')
def step(context):
    name = str(time.strftime("%Y%j%H%M%S"))
    user = dict(
    	fullname = name,
        email = name + "@email.com",
        password = "password",
        username = name + "_1"
    )
    context.personas[name] = user
    context.persona = context.personas[name]

@given('I am logged in as the current persona')
def step(context):
    assert context.persona
    context.execute_steps(u'''
        When I fill in "#login_login-main input[name=email]" with "$email"
        When I fill in "#login_login-main input[name=passwd]" with "$password"
        When I press "login"
    ''')
    if not context.browser.is_text_present("invalid password, real name ID, or email"):
        return
    context.execute_steps(u'''
        When I click the link with text "register"
        When I fill in "user" with "$fullname"
        When I fill in "email_reg" with "$email"
        When I fill in "passwd_reg" with "$password"
        When I fill in "passwd2_reg" with "$password"
        When I press "create account"
        Then I should see "$username"
    ''')


@given('I visit lightnet')
def step(context):
    context.execute_steps(u'''
        When I visit "%s" 
    ''' % context.base_url)

@when('visiting google')
def step(context):
    context.browser.get('http://www.google.com')

@when('I fill in "{field}" with "{value}"')
@persona_vars
def i_fill_in_field(context, field, value):
    field = \
        context.browser.find_by_css(field) or \
        context.browser.find_by_id(field) or \
        context.browser.find_by_name(field) or \
        context.browser.find_by_xpath("//button[text()='%s']" % field) or \
        context.browser.find_by_xpath("//button[contains(text(), '%s')]" % field) or \
        context.browser.find_link_by_text(field) or \
        context.browser.find_link_by_partial_text(field)
    field.first.value = value
  
@then('its title should be "Google"')
def step(context):
    assert context.browser.title == "Google"

@then(u'I should see "{text}"')
@persona_vars
def should_see(context, text):
    assert context.browser.is_text_present(text), u'Text not found'
