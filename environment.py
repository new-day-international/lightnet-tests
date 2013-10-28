from selenium import webdriver

def before_all(context):
    context.browser = webdriver.PhantomJS("/usr/local/bin/phantomjs") # path to phantomjs binary

def after_all(context):
    context.browser.quit()
    