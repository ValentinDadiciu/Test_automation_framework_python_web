from behave import *

@when('I click size button')
def step_impl(context):
    context.search_results_page.click_size()

@when('I click color button')
def step_impl(context):
    context.search_results_page.click_color()

@when('I click Add to cart button')
def step_impl(context):
    context.search_results_page.click_add_to_cart()

@then('Cart has "{number}" item in it')
def step_impl(context, number):
    context.search_results_page.verify_cart_quantity(number)