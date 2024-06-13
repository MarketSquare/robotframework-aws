from .librarycomponent import LibraryComponent
from robotlibcore import DynamicCore
from AWSLibrary.version import get_version
from AWSLibrary.keywords import (
    SessionKeywords,
    S3Keywords,
    ResourceKeywords
)

__version__ = get_version()


class AWSLibrary(DynamicCore):
    """AWSLibrary is a testing library for Robot Framework that gives you the ability to use some of the AWS
    services in your tests. This robot library is made from Boto3 SDK

    | ***** Settings *****
    | Library  AWSLibrary
    |
    |
    | ***** Variables *****
    | ${REGION}    eu-west-1
    | ${BUCKET}    some-bucket-name
    |
    |
    | ***** Test Cases *****
    | Test Case
    |     [Setup]    Create Session With Keys    ${REGION}    %{AWS_USER_NAME}    %{AWS_USER_PASS}
    |     S3 Upload File    ${BUCKET}    new_file.json    ${CURDIR}/local_file.json
    |     S3 Key Should Exist    ${BUCKET}    new_file.json
    |     S3 Key Should Not Exist    ${BUCKET}    local_file.json
    |     ${file_inside_folder}    S3 List Objects    ${BUCKET}    folder_name
    |     Log List   ${file_inside_folder}
    |     S3 Download File    ${BUCKET}    new_file.json    ${CURDIR}/new_local_file.json
    |     S3 Delete File    ${BUCKET}    new_file.json
    |     [Teardown]    Delete All Sessions
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):
        libraries = [
            SessionKeywords(self),
            S3Keywords(self),
            ResourceKeywords(self),
        ]
        DynamicCore.__init__(self, libraries)
