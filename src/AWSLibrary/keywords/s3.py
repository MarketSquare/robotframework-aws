from AWSLibrary.base.robotlibcore import keyword
from AWSLibrary.base import LibraryComponent, KeywordError, ContinuableError
from botocore.exceptions import ClientError
from robot.api import logger
import botocore


class S3Keywords(LibraryComponent):

    @keyword('Create Bucket')
    def create_bucket(self, bucket, region=None):
        """ Creates S3 Bucket with the name given @param: ```bucket```
        in the specified @param: ```region```.
            If Bucket already exists, an exception will be thrown.

        Example:
        | Create Bucket | randomBucketName | us-west-2 |
        """
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
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
                    @param: ```path``` which is the local path of file.
            Example:
            | Download File | bucket | path | key |
        """
        client = self.state.session.client('s3')
        try:
            client.download_file(bucket, key, path)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == '404':
                raise KeywordError(f"Keyword: {bucket} does not exist")
            else:
                logger.debug(e)

    @keyword('Upload File')
    def upload_file(self, bucket, key, path):
        """ Uploads File from S3 Bucket
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
                    @param: ```path``` which is the local path of file.
            Example:
            | Upload File | bucket | path | key |
        """
        client = self.state.session.client('s3')
        try:
            client.upload_file(path, bucket, key)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == '404':
                raise KeywordError(f"Keyword: {bucket} does not exist")
            else:
                raise ContinuableError(e)

    @keyword('Key Should Exist')
    def key_should_exist(self, bucket, key):
        """ Key Should Exist
        Description: Checks to see if the file on the s3 bucket exist. If so, the keyword will not fail.
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
            Example:
            | Key Should Exist | bucket | key |
        """
        client = self.state.session.client("s3")
        res = client.head_object(Bucket=bucket, Key=key)
        try:
            if res['ResponseMetadata']['HTTPStatusCode'] == 404:
                raise KeywordError("Key: {}, does not exist".format(key))
        except ClientError as e:
            raise ContinuableError(e.response['Error'])
        return True

    @keyword('Key Should Not Exist')    
    def key_should_not_exist(self, bucket, key):
        """ Verifies Key on S3 Bucket Does Not Exist
        Description: Checks to see if the file on the s3 bucket exist. If so, the keyword will fail.
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
            Example:
            | Key Should Not Exist | bucket | key |
        """
        client = self.state.session.client('s3')
        self.rb_logger.info(f"Retrieve Client Hanlder: {client}")
        try:
            res = client.head_object(Bucket=bucket, Key=key)
            if res['ResponseMetadata']['HTTPStatusCode'] == 200:
                raise KeywordError("Key: {}, already exists".format(key))
        except ClientError as e:
            raise ContinuableError(e.response['Error'])
        return True

    @keyword('Allowed Methods')
    def allowed_methods(self, bucket, methods=[]):
        client = self.state.session.client("s3")
        self.rb_logger.info(f"Retrieve Client Hanlder: {client}")
        try:
            response = client.get_bucket_cors(Bucket=bucket)
            obj = response['CORSRules'][0]
            aws_methods = obj['AllowedMethods']
            assert set(aws_methods) == set(methods)
        except ClientError as e:
            raise KeywordError(e)
        
    
