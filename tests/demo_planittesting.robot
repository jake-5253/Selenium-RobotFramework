*** Settings ***
Library    ./../core/WebHandler.py
Library    ./../keywords/CommonKeywords.py
Library    ./../keywords/ContactKeywords.py
Library    ./../keywords/ShopKeywords.py
Library    ./../keywords/CartKeywords.py
Test Setup    WebHandler.setup
Test Teardown    WebHandler.Teardown

*** Keywords ***
Test Case 2
    Go To Jupiter Toys Home Page
    Go To Menu    Contact
    Fill In Contact Form    Jake    Alconcel    jake@test.com   0212345678  This is an auto-generated message
    Click Submit Button
    Verify Successful Contact Submission Message Displayed      Thanks Jake

*** Test Cases ***
Test Case 1 - Verify Mandatory Fields and Error Messages
    Go To Jupiter Toys Home Page
    Go To Menu    Contact
    Click Submit Button
    Verify Validation on Mandatory Fields
    Verify Error Messages For Required Fields Displayed
    Fill In Contact Form    Jake    Alconcel    jake@test.com   0212345678  This is an auto-generated message
    Verify Error Messages For Required Fields Not Displayed
    [Tags]    regression

Test Case 2 - Fill-in and Successfully Submit Contact Details
    FOR    ${index}     IN RANGE    5
        Test Case 2
    END
    [Tags]    regression

Test Case 3 - Verify Unit Price and Total Calculation
    Go To Jupiter Toys Home Page
    Go To Menu    Shop
    Add Item With Quantity    Stuffed Frog  2
    Add Item With Quantity    Fluffy Bunny  5
    Add Item With Quantity    Valentine Bear  3
    Go To Cart
    Verify Item Subtotals Per Item  Stuffed Frog
    Verify Item Subtotals Per Item  Fluffy Bunny
    Verify Item Subtotals Per Item  Valentine Bear
    Verify Subtotal Equal to Total