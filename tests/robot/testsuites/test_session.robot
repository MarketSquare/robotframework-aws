*** Settings ***
Library  Collections
Library  AWSLibrary  ${ACCESS_KEY}  ${SECRET_KEY}



*** Test Case ***
Test Create Session
    Create Session  us-east-1

Test Delete Session
    Delete Session  us-east-1

Test Delete All Sessions
    Delete All Sessions

Test Get Client
    Get Client

Test Get Resource
    Get Resource





    # Download File  zappastaticbin  test.html  static/test.html
    # Local File Should Exist  test.html
    # Key Should Not Exist  zappastaticbin  test.html
    
    # Allowed Methods  zappastaticbin  ${crud}
    # Get Bucket  zappastaticbin
    # Get Object  zappastaticbin  static/js/jquery.cookie.js
    # Key Should Not Exist  zappastaticbin  static/test.html  test.html
    # Upload File  zappastaticbin  static/test.html  test.html
    # Key Should Exist  zappastaticbin  static/test.html  test.html
