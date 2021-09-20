Feature: Testing Wiki

    Scenario Outline: Scenario Outline name: Navigation to wikipedia
        Given Open wikipedia
        When I search for "<article>"
        Then I can see "<article>"
    
    Examples:
        | article |
        | software testing | 
        | dog |