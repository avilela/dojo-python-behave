from behave import given, when, then
from pages.google_page import GooglePage
from helpers.utils import check_element_exists


@given('users go to Google')
def user_go_to_google(context):
    context.driver.get('http://www.google.com.br')


@given('users go to Google.DE')
def user_go_to_google(context):
    context.driver.get('http://www.google.de')


@when('user type "{search_word}"')
def user_type(context, search_word):
    google_page = GooglePage(context.driver)
    google_page.input_field = search_word


@when('click on search button')
def click_search_button(context):
    google_page = GooglePage(context.driver)
    google_page.search_button.submit()


@then('research to be successfully executed')
def list_results(context):
    google_page = GooglePage(context.driver)
    assert google_page.result_list.is_displayed(), (
        'Elemento não está sendo exibido')


@then('list of value results to be shown to user')
def list_results(context):
    google_page = GooglePage(context.driver)
    assert google_page.result_count.is_displayed()


@then('list of value results will not be shown to user')
def empty_list_results(context):
    google_page = GooglePage(context.driver)
    assert not check_element_exists(google_page.result_count)
