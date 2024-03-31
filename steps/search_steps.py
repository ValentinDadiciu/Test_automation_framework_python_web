from behave import *

@given('I am on the home page')
def step_impl(context):
    context.home_page.open()

@when('I enter "{text}" in the search filed')
def step_impl(context, text):
    context.home_page.set_search_term(text)

@when('I click the search magnifying button')
def step_impl(context):
    context.home_page.click_search_magnifying_button()

@then('I am redirected on the search results page')
def step_impl(context):
    context.search_results_page.verify_url()

@then('There are some results displayed')
def step_impl(context):
    context.search_results_page.verify_search_results_displayed()