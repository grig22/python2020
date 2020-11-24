*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://localhost
${BROWSER}        Chrome

*** Test Cases ***
Buy iMac
    Open Browser To Login Page
    Go To Mac
    Add To Cart
    Open Cart
    Checkout
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    GRIG22 HAPPY STORE

Go To Mac
    Click Element     //*[@id="menu"]/div[2]/ul/li[1]/a
    Click Element     //*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a
    Title Should Be     Mac

Add To Cart
    Click Element    //*[@id="content"]/div[2]/div/div/div[2]/div[2]/button[1]/i

Open Cart
    Wait Until Page Contains Element    //*[@id="product-category"]/div[1]/a[2]
    Click Element     //*[@id="product-category"]/div[1]/a[2]
    Title Should Be     Shopping Cart

Checkout
    Click Element   //*[@id="content"]/div[3]/div[2]/a
    Title Should Be     Checkout