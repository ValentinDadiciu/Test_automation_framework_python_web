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

@when('I am redirected on the search results page')
def step_impl(context):
    context.search_results_page.verify_url()

@when('There are some results displayed')
def step_impl(context):
    context.search_results_page.verify_search_results_displayed()
@when("I click Reviews button")
def step_impl(context):
    context.search_results_page.click_review_button()
@when('I click 5 stars Raiting')
def step_impl(context):
    context.search_results_page.click_rating_rev()
@when('I write the Nickname "{text}"')
def step_impl(context, text):
    context.search_results_page.set_nickname(text)
@when('I write the summary "{text}"')
def step_impl(context, text):
    context.search_results_page.set_summary(text)
@when('I write the Review "{text}"')
def step_impl(context, text):
    context.search_results_page.set_review(text)

@then('I click on the Submit Review button')
def step_impl(context):
    context.search_results_page.click_submit_review_button()


@when('I click the cart button')
def step_impl(context):
    context.search_results_page.click_cart()

@when('I click the Proceed to Checkout button')
def step_impl(context):
    context.search_results_page.click_proceed_checkout()

@when('I am on the Shipping page "{url}"')
def step_impl(context, url):
    context.search_results_page.verify_url_shipping(url)

@when('I enter Street Address')
def step_impl(context):
    context.search_results_page.set_street_address('Avenue28')

@when('I enter City')
def step_impl(context):
    context.search_results_page.set_city('Georgia')

@when('I select State "{text}"')
def step_impl(context, text):
    context.search_results_page.select_state(text)

@when('I enter Postal Code "{number}"')
def step_impl(context, number):
    context.search_results_page.set_postal_code(number)

@when('I select Country "{text}"')
def step_impl(context, text):
    context.search_results_page.select_country(text)

@when('I enter Phone Number')
def step_impl(context):
    context.search_results_page.set_phone_number('0744888855')

@when('I choose Shipping Methods')
def step_impl(context):
    context.search_results_page.click_shipping_methods()

@when('I click Next button')
def step_impl(context):
    context.search_results_page.click_next_button()

@when('I check the confirmation for bill address')
def step_impl(context):
    context.search_results_page.click_check_bill_address()
@when('I click Place Order button')
def step_impl(context):
    context.search_results_page.click_place_order_button()

@then('I am redirected on the success order page "{url}"')
def step_impl(context, url):
    context.search_results_page.verify_url_order(url)

@then ('Success order message is displayed')
def step_impl(context):
    context.search_results_page.verify_success_message_displayed()

@then('The success order message is "{text}"')
def step_impl(context, text):
    context.search_results_page.verify_success_message_contains_text(text)