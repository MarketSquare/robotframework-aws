*** Settings ***
Library  Collections
Library  AWSLibrary



*** Variable ***
${REGION}=  us-east-1
${BUCKET}=  zappastaticbin
${KEY}=  fail_test.html


*** Test Case ***
Test Key Should Not Exist
    Create Session With Keys  ${REGION}  ${ACCESS_KEY}  ${SECRET_KEY}
    Key Should Not Exist  ${BUCKET}  ${KEY}
    Delete All Sessions