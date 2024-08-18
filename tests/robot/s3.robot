*** Settings ***
Resource    data.resource
Suite Setup    Create Session And Set Endpoint
Suite Teardown    Delete All Sessions


*** Variables ***
${BUCKET_NAME}    test-bucket


*** Test Cases ***
Test Upload And List
	[Tags]    s3
	S3 Upload File    ${BUCKET_NAME}    s3_file.txt    ${CURDIR}/data/local_file.txt
	${objects}    S3 List Objects    ${BUCKET_NAME}
	Should Not Be Empty    ${objects}
	Should Be Equal    ${objects}[0]    s3_file.txt
	S3 Key Should Exist    ${BUCKET_NAME}    s3_file.txt

Test Remove
    [Tags]    s3
    S3 Key Should Not Exist    ${BUCKET_NAME}    s3_file_to_remove.txt
    ${objects}    S3 List Objects    ${BUCKET_NAME}
    Should Be Empty    ${objects}
    S3 Upload File    ${BUCKET_NAME}    s3_file_to_remove.txt    ${CURDIR}/data/local_file.txt
    S3 Key Should Exist    ${BUCKET_NAME}    s3_file_to_remove.txt
    S3 Delete File    ${BUCKET_NAME}    s3_file_to_remove.txt
    S3 Key Should Not Exist    ${BUCKET_NAME}    s3_file_to_remove.txt

Test Download
    [Tags]    s3
    [Setup]    Remove File    ${OUTPUTDIR}/downloaded_file.txt
    File Should Not Exist    ${OUTPUTDIR}/downloaded_file.txt
    S3 Upload File    ${BUCKET_NAME}    s3_file_to_download.txt    ${CURDIR}/data/local_file.txt
    S3 Download File    ${BUCKET_NAME}    s3_file_to_download.txt    ${OUTPUTDIR}/downloaded_file.txt
    File Should Exist    ${OUTPUTDIR}/downloaded_file.txt
