*** Settings ***
Library  Collections
Library  AWSLibrary



*** Variable ***
${REGION}=  us-east-1
${BUCKET}=  zappastaticbin
${KEY}=  test.html
${PATH}=  downloaded_test_file.html


*** Test Case ***
Download File
    Create Session With Keys  ${REGION}  ${ACCESS_KEY}  ${SECRET_KEY}
    Upload File  ${BUCKET}  ${KEY}  ${PATH}
    Download File  ${BUCKET}  ${KEY}  ${PATH}
    Local File Should Exist  ${PATH}
    Delete All Sessions