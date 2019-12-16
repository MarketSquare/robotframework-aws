*** Settings ***
Library  Collections
Library  AWSLibrary



*** Variable ***
${REGION}=  us-east-1
${BUCKET}=  zappastaticbin
${KEY}=  path_test.html



*** Test Case ***
Test Key Should Not Exist
    Create Session With Keys  ${REGION}  ${ACCESS_KEY}  ${SECRET_KEY}
    Key Should Exist  ${BUCKET}  ${KEY}
    Delete All Sessions