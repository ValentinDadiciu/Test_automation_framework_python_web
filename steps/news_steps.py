from behave import *

@given("I am on the Whats New page")
def step_impl(context):
    context.new_page.open()


@then('The URL of the page is "https://magento.softwaretestingboard.com/what-is-new.html"')
def step_impl(context):
    context.new_page.verify_url()