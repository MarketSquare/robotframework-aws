*** Settings ***
Library  Collections
Library  AWSLibrary  ${ACCESS_KEY}  ${SECRET_KEY}


*** Test Cases ***
Test List Buckets
    Create Session  us-east-1
    List Buckets

Test Get Bucket
    Get Bucket  zappastaticbin

Test List Objects
    List Objects  zappastaticbin

Test Get Object
    Get Object  zappastaticbin  test.html

Test Read S3 Object
    Read S3 Object  zappastaticbin  test.html

Test Key Should Not Exist
    Key Should Not Exist  zappastaticbin  test_not_there.html

Test Key Should Exist
    Key Should Exist  zappastaticbin  test.html

Test Upload File
    Upload File  zappastaticbin  static/test.html  uploaded_test.html
    Key Should Exist  zappastaticbin  uploaded_test.html
    Local File Should Not Exist  static/test.html

Test Download File
    Download File  zappastaticbin  static/downloaded_test.html  test.html
    Local File Should Exist  static/downloaded_test.html

Test Fail For Allowed Methods
    ${methods}=  Create List  GET POST
    Run Keyword And Expect Error  *  Allowed Methods  zappastaticbin  ${methods}

Test Pass For Allowed Methods
    ${methods}=  Create List  GET
    Allowed Methods  zappastaticbin  ${methods}