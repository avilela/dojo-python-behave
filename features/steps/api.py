from behave import given, when, then
from requests import get
import json

REQUEST_ERROR_MESSAGE = {200: "Something is not ok, please check the request"}


@given('user has mock api for users')
def user_has_mock_api(context):
    context.api = 'http://0.0.0.0:3000/users'


@when('user execute a get request')
def user_execute_a_get_request(context):
    context.response = get(context.api)


@then('API will send response_code {response_code:d}')
def check_response_code(context, response_code):
    assert context.response.status_code == response_code, (
        f'Response status code was unexpected\n'
        f'Expected: {response_code}\n'
        f'Found: {context.response.status_code}'
    )


@then('validate all required fields are returned')
def validate_all_required_fields_are_returned(context):
    table = []
    for row in context.table.rows:
        table.append({row['field']: row['type']})

    json_received_fields = json.loads(context.response.text)

    for item in table:
        for key, value in item.items():
            assert key in json_received_fields, f"Error: {key} not in response"
            assert value == type(json_received_fields[key]).__name__, (
                f"Error: {value} not in response"
            )
