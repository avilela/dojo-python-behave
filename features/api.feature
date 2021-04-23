@api
Feature: API Mock Test

    Simple Api test

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
        """
            using tables to send multiples fields
        """
        
    