@web
Feature: Feature test google search automation

  Feature Description

  Background:


  @positivo
  Scenario: Google automation
    Given users go to Google
    When user type "casa colorida"
    And click on search button
    Then research to be successfully executed
    And list of value results to be shown to user

  @positivo
  Scenario Outline: Google automation scenario 2
    Given users go to Google
    When user type "<bananinhas>"
    And click on search button
    Then research to be successfully executed
    And list of value results to be shown to user

    Examples:
      | bananinhas        |
      | casa colorida     |
      | casa não colorida |

  @positivoDE
  Scenario: Google automation for Germany
    Given users go to Google.DE
    When user type "casa colorida"
    And click on search button
    Then research to be successfully executed
    And list of value results to be shown to user

  @negativoDE
  Scenario: Google automation for Germany
    Given users go to Google.DE
    When user type "HFUISDDHFISUDFHSIUNHJKnJKDFSAKLFNSDLKFG"
    And click on search button
    Then research to be successfully executed
    And list of value results will not be shown to user