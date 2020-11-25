*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://localhost
${ADMIN URL}      http://localhost/admin
${BROWSER}        Chrome
${admin}     admin
${password}     1
${fanboy}       fanboy
${email}        fanboy@dea.gov
${message}      such robot much framework
${store title}  GRIG22 HAPPY STORE

*** Test Cases ***
Buy iMac
    Open Browser To Login Page
    Go To Mac
    Add To Cart
    Open Cart
    Checkout
    [Teardown]    Close Browser

Contact Us
    Open Browser To Login Page
    Go To Contact Us
    Fill Contact Form
    Submit
    Continue From Submit
    Title Should Be    ${store title}
    [Teardown]    Close Browser

Login Admin
    Open Browser To Admin Page
    Login Admin
    Zoom Map
    Select Country

*** Keywords ***
Zoom Map
    Wait Until Page Contains Element    //*[@id="vmap"]/div[1]
    Click Element    //*[@id="vmap"]/div[1]
    Click Element    //*[@id="vmap"]/div[1]
    Click Element    //*[@id="vmap"]/div[1]

Select Country
    Click Element   //*[@id="jqvmap1_ne"]

Login Admin
    Input Text    input-username    ${admin}
    Input Text    input-password    ${password}
#    Click Button        Login
    Submit Form
    Title Should Be    Dashboard

Open Browser To Admin Page
    Open Browser    ${ADMIN URL}    ${BROWSER}
    Title Should Be    Administration

Submit
    Click Button        Submit

Continue From Submit
    Click Element    xpath://*[@id="content"]/div/div/a

Go To Contact Us
    Click Element       xpath:/html/body/footer/div/div/div[2]/ul/li[1]/a
    Title Should Be     Contact Us

Fill Contact Form
    Input Text    input-name    ${fanboy}
    Input Text    input-email    ${email}
    Input Text    input-enquiry    ${message}

Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    ${store title}

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