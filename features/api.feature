@api
Feature: API Mock Test

    Simple Api test
    Background:
        Given user has mock api for users

    Scenario: Validate a response code for get request 
        Given user has mock api for users
        When user execute a get request
        Then API will send response_code 200
    

    @api_schema_test
    Scenario: Validate json schema of response of get request 
        Given user has mock api for users
        When user execute a get request
        Then API will send response_code 200
        And validate all required fields are returned
            | field  | type |
            | users  | list |
            | total  | str  |

    Scenario: Validate post request
        Given user has mock api for post request
        When user post with body and headers
        Then API will send response_code 201

