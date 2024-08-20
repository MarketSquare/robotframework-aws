*** Settings ***
Resource    common.resource
Suite Setup    Create Session And Set Endpoint
Suite Teardown    Delete All Sessions


*** Variables ***
${BUCKET_NAME}      test-bucket-1
${BUCKET_NAME_2}    test-bucket-2


*** Test Cases ***
Test Upload And List
	[Tags]    s3
	S3 Upload File    ${BUCKET_NAME}    s3_file.txt    ${CURDIR}/data/local_file.txt
	${objects}    S3 List Objects    ${BUCKET_NAME}
	Should Not Be Empty    ${objects}
	Should Be Equal    ${objects}[0]    s3_file.txt
	S3 Key Should Exist    ${BUCKET_NAME}    s3_file.txt
	[Teardown]    S3 Delete File    ${BUCKET_NAME}    s3_file.txt

Test Upload And List With Folder
	[Tags]    s3
	S3 Upload File    ${BUCKET_NAME}    s3_file_no_folder.txt    ${CURDIR}/data/local_file.txt
	S3 Upload File    ${BUCKET_NAME}    new_folder/s3_file_in_folder.txt    ${CURDIR}/data/local_file.txt
	${objects}    S3 List Objects    ${BUCKET_NAME}
	Should Not Be Empty    ${objects}
	List Should Contain Value    ${objects}    s3_file_no_folder.txt
	List Should Contain Value    ${objects}    new_folder/s3_file_in_folder.txt
	${objects_folder}    S3 List Objects    ${BUCKET_NAME}    new_folder/
	List Should Not Contain Value    ${objects_folder}    s3_file_no_folder.txt
	List Should Contain Value    ${objects_folder}    new_folder/s3_file_in_folder.txt
	[Teardown]    Run Keywords    S3 Delete File    ${BUCKET_NAME}    s3_file_no_folder.txt
    ...    AND    S3 Delete File    ${BUCKET_NAME}    new_folder/s3_file_in_folder.txt

Test Remove And List With Prefix
    [Tags]    s3
    [Setup]    S3 Key Should Not Exist    ${BUCKET_NAME}    s3_file_to_remove.txt
    ${objects}    S3 List Objects    ${BUCKET_NAME}    prefix=s3_file_to_remove
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
    [Teardown]    S3 Delete File    ${BUCKET_NAME}    s3_file_to_download.txt

Test Get Content
    [Tags]    s3
    [Setup]    S3 Upload File    ${BUCKET_NAME}    s3_file_to_read.txt    ${CURDIR}/data/local_file.txt
    ${content}    S3 Get File Content    ${BUCKET_NAME}    s3_file_to_read.txt
    Should Be Equal As Strings    ${content}    File for Robot Framework test
    [Teardown]    S3 Delete File    ${BUCKET_NAME}    s3_file_to_read.txt

Test Copy
    [Tags]    s3
    [Setup]    S3 Upload File    ${BUCKET_NAME}    s3_file_to_copy.txt    ${CURDIR}/data/local_file.txt
    S3 Copy Between Buckets    ${BUCKET_NAME}    s3_file_to_copy.txt    ${BUCKET_NAME_2}    s3_file_copied.txt
    S3 Key Should Exist    ${BUCKET_NAME_2}    s3_file_copied.txt
    [Teardown]    Run Keywords    S3 Delete File    ${BUCKET_NAME}    s3_file_to_copy.txt
    ...    AND    S3 Delete File    ${BUCKET_NAME_2}    s3_file_copied.txt

Test Metadata
    [Tags]    s3
    [Setup]    S3 Upload File    ${BUCKET_NAME}    s3_file_metadata.txt    ${CURDIR}/data/local_file.txt
    ${metadata}    S3 Get File Metadata    ${BUCKET_NAME}    s3_file_metadata.txt
    Dictionary Should Contain Key    ${metadata}    ResponseMetadata
    Dictionary Should Contain Key    ${metadata}    Metadata
    Dictionary Should Contain Key    ${metadata}[ResponseMetadata]    RequestId
    Dictionary Should Contain Key    ${metadata}[ResponseMetadata][HTTPHeaders]    last-modified
    [Teardown]    S3 Delete File    ${BUCKET_NAME}    s3_file_metadata.txt
