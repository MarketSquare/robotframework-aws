*** Settings ***
Library  Collections
Library  AWSLibrary



*** Variable ***
${REGION}=  us-east-1
${BUCKET}=  zappastaticbin
${KEY}=  test.html
${PATH}=  downloaded_test_file.html
${s3FolderName}=  s3FolderName


*** Test Case ***
Upload File
    Create Session With Keys  ${REGION}  ${ACCESS_KEY}  ${SECRET_KEY}
    Upload File  ${BUCKET}  ${KEY}  ${PATH}
    Key Should Exist  ${BUCKET}  ${KEY}
    Delete File  ${BUCKET}  ${KEY}
    Delete All Sessions


** Test Cases ***
Upload file to S3 folder
    ${uploadKey}    Set variable    ${s3FolderName}/folder_file_test.html
    ${uploadpath}    Set variable    ${EXECDIR}/static/test.html
    Create Session With Keys    ${REGION}  ${ACCESS_KEY}  ${SECRET_KEY}
    Upload File    ${BUCKET}    ${uploadKey}    ${uploadPath}