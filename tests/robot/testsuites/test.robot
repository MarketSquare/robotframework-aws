*** Settings ***
Library  AWSLibrary  ${ACCESS_KEY}  ${SECRET_KEY}
Library  Collections


*** Test Case ***
First Test Case
    Create Session  us-east-1
    # Download File  zappastaticbin  test.html  static/test.html
    # Local File Should Exist  test.html
    # Key Should Not Exist  zappastaticbin  test.html
    ${crud}=  Create List  GET
    Allowed Methods  zappastaticbin  ${crud}
    # Get Bucket  zappastaticbin
    # Get Object  zappastaticbin  static/js/jquery.cookie.js
    # Key Should Not Exist  zappastaticbin  static/test.html  test.html
    # Upload File  zappastaticbin  static/test.html  test.html
    # Key Should Exist  zappastaticbin  static/test.html  test.html
    Delete Session  us-east-1