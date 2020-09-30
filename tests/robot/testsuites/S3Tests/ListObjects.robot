*** Settings ***
Library  Collections
Library  AWSLibrary



*** Variable ***
${REGION}=  us-east-1
${BUCKET}=  zappastaticbin
${KEY}=  test.html
${PATH}=  downloaded_test_file.html


*** Test Case ***
List Objects
    Create Session With Keys  ${REGION}  ${ACCESS_KEY}  ${SECRET_KEY}
    Upload File  ${BUCKET}  ${KEY}  ${PATH}
    ${list_of_objects}=  List Objects  ${BUCKET}
    Should Not Be Empty  ${list_of_objects}
    Delete All Sessions