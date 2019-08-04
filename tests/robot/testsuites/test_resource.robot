*** Settings ***
Library  Collections
Library  AWSLibrary  ${ACCESS_KEY}  ${SECRET_KEY}


*** Test Cases ***
Test Local File Should Not Exist
    Local File Should Not Exist  static/not_exist.html

Test Local File Should Exist
    Local File Should Exist  static/test.html