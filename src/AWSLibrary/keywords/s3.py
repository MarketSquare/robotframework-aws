from AWSLibrary.base.robotlibcore import keyword
from AWSLibrary.base import LibraryComponent, KeywordError, ContinuableError, FatalError
from robot.api import logger
import boto3, logging, botocore


class S3Keywords(LibraryComponent):

    @keyword
    def create_bucket(self, bucket, region=None):
        client = self.state.session.client('s3')
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
        client = self.state.session.client("s3")
        try:
            client.download_file(bucket, key, path)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == '404':
                raise KeywordError(f"Keyword: {bucket} does not exist")
            else:
                logger.debug(e)

    @keyword('Upload File')
    def upload_file(self, bucket, key, file):
        client = self.state.session.client("s3")
        try:
            client.upload_file(file, bucket, key)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == '404':
                raise KeywordError(f"Keyword: {bucket} does not exist")
            else:
                self.logger.debug(e)