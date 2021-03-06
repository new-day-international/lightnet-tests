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
    context.execute_steps(u'''
        Given "%s" as the persona
    ''' % name)

@given('I am logged in as the current persona')
def step(context):
    assert context.persona
    context.execute_steps(u'''
        When I fill in "#login_login-main input[name=email]" with "$email"
        When I fill in "#login_login-main input[name=passwd]" with "$password"
        When I press "login"
    ''')
    if context.browser.is_text_present("invalid password, real name ID, or email"):
        context.execute_steps(u'''
            When I click the link with text "register"
            When I fill in "user" with "$fullname"
            When I fill in "email_reg" with "$email"
            When I fill in "passwd_reg" with "$password"
            When I fill in "passwd2_reg" with "$password"
            When I press "create account"
        ''')
    context.execute_steps(u'''
        Then I should be logged in
    ''')

@when('visiting google')
def step(context):
    context.browser.get('http://www.google.com')

@when('I fill in "{field}" with the current timestamp')
def step(context, field):
    timestamp = str(time.strftime("%Y%j%H%M%S"))
    context.execute_steps(u'''
        When I fill in "%(field)s" with "%(timestamp)s"
        ''' % locals())
    context.space_name = timestamp

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

@then(u'I save a screenshot to "{path}"')
def step(context, path):
    fullpath = os.path.join(context.screenshot_dir, path)
    context.browser.driver.get_screenshot_as_file(fullpath)

@then(u'the browser\'s url should contain the timestamp')
def step(context):
    context.execute_steps(u'''
        Then the browser's URL should contain "%s"
        ''' % context.space_name)

@then(u'the browser\'s URL should contain "{text}"')
@persona_vars
def the_browser_url_should_contain(context, text):
    assert text in context.browser.url, "I was looking for %r but I couldn't find it in %r" % (text, context.browser.url)

@then(u'I should see "{text}"')
@persona_vars
def should_see(context, text):
    assert context.browser.is_text_present(text), u'Text not found'

@then(u'I should be logged in')
def step(context):
    context.execute_steps(u'''
     Then I should see an element with the css selector "body.loggedin .user" within 20 seconds
        ''')

@then(u'I should not be logged in')
def set(context):
    context.execute_steps(u'''
     Then I should see an element with the css selector "#login_login-main" within 20 seconds
        ''')
