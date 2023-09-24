Feature: Verify that items can be added to cart

  Scenario Outline: Add one item to cart
    Given I am logged into the app
    When I click add to cart button for the item "<item>"
    And I click on the cart button
    Then I check that the item "<item>" was added to the cart
    Examples:
      |item |
    |Sauce Labs Backpack|
    |Sauce Labs Bolt T-Shirt|
    |Sauce Labs Onesie      |
    |Sauce Labs Bike Light  |
    |Sauce Labs Fleece Jacket|
    |Test.allTheThings() T-shirt (Red)|

    Scenario: add a random number of items in cart
      Given I am logged into the app
      When I click add to cart button for a random number of items
      Then I check that the cart icon show the number of items added to cart

