*** Settings ***
Library  Collections
Library  AWSLibrary



*** Variable ***
${REGION}=  us-east-1
${BUCKET}=  zappastaticbin
${KEY}=  test.html
${PATH}=  downloaded_test_file.html


Bucket Permissions
    ${CRUD}=  Create List  GET
    Allowed Methods  ${BUCKET}  ${CRUD}