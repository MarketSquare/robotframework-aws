from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.String import String
from robot.utils import ConnectionCache
from robot.utils.dotdict import DotDict
from robot.api.deco import keyword
from robot.api import logger
from os import getenv
import boto3, logging, botocore
from AWSLibrary.keywords import SessionManager
from AWSLibrary.base.robotlibcore import keyword
from AWSLibrary.base import LibraryComponent
from AWSLibrary.exceptions import KeywordError, ContinuableError, FatalError
import botocore.session
session = botocore.session

class S3Manager(LibraryComponent):

    @keyword
    def create_bucket(self, bucket, region=None):
        client = self.state.session.client('s3')
        self.logger.debug("Running Create Bucket")
        try:
            client.create_bucket(Bucket=bucket)
            self.logger.debug(f"Created new bucket: {bucket}")
        except botocore.exceptions.ClientError as e:
            error_code = e.response["Error"]["Code"]
            if error_code == "BucketAlreadyExists":
                self.logger.debug(f"Keyword Failed: {error_code}")
                raise ContinuableError(f"Keyword Failed: {error_code}")
            elif error_code == 'BucketAlreadyOwnedByYou':
                self.logger.debug("Bucket Already Exists")
                raise ContinuableError("Bucket Already Exists")
            else:
                self.logger.debug(f"Error Code: {e.response['Error']['Code']}")

    @keyword('Download File')
    def download_file_from_s3(self, bucket, key, path):
        """ Downloads File from S3 Bucket

            Example:
            | Download File | bucket | path | key |
        """
        # print(self.state)
        print(self.aws_session)
        self.logger.debug("Starting Download")
        try:
            client.download_file(bucket, key, path)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == '404':
                raise KeywordError(f"Keyword: {bucket} does not exist")
            else:
                logger.debug(e)


        