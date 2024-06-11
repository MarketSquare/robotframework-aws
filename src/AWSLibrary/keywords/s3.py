from AWSLibrary.base.robotlibcore import keyword
from AWSLibrary.base import LibraryComponent, KeywordError, ContinuableError
from robot.api import logger
import botocore


class S3Keywords(LibraryComponent):

    @keyword('Create Bucket')
    def create_bucket(self, bucket, region=None, endpoint_url=None):
        """ Creates S3 Bucket with the name given @param: ```bucket```
            and uses the optionally provided @param: ```endpoint_url```.
            If Bucket already exists, an exception will be thrown.

        Example:
        | Create Bucket | randomBucketName |
        """
        client = self.state.session.client('s3', endpoint_url=endpoint_url)
        try:
            client.create_bucket(Bucket=bucket)
            self.rb_logger.debug(f"Created new bucket: {bucket}")
        except botocore.exceptions.ClientError as e:
            error_code = e.response["Error"]["Code"]
            if error_code == "BucketAlreadyExists":
                self.logger.debug(f"Keyword Failed: {error_code}")
                raise ContinuableError(f"Keyword Failed: {error_code}")
            elif error_code == 'BucketAlreadyOwnedByYou':
                self.logger.debug("Bucket Already Exists")
                raise ContinuableError("Bucket Already Exists")
            else:
                self.rb_logger.debug(f"Error Code: {e.response['Error']['Code']}")

    @keyword('List Objects')
    def list_objects(self, bucket, prefix=""):
        """ List Objects
        Requires:   @param: ```bucket``` which is the bucket name
        Optional:   @param: ```prefix``` which limits the response to keys that begin with the specified prefix.
            Example:
            | List Objects | bucket | key |
        """
        client = self.state.session.client('s3')
        try:
            response = client.list_objects(
                Bucket=bucket,
                Prefix=prefix
            )
            if 'Contents' in response:
                return [key['Key'] for key in response['Contents']]
            else:
                return []
        except botocore.exceptions.ClientError as e:
            raise AssertionError(e)

    @keyword('Delete File')
    def delete_file(self, bucket, key, endpoint_url=None):
        """ Delete File
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
                    @param: ```endpoint_url``` optionally override the s3 endpoint url
            Example:
            | Delete File | bucket | key |
        """
        client = self.state.session.client('s3', endpoint_url=endpoint_url)
        try:
            response = client.delete_object(
                Bucket=bucket,
                Key=key
            )
            if response['ResponseMetadata']['HTTPStatusCode'] != 204:
                raise ContinuableError(f"Error {response['ResponseMetadata']}")
        except botocore.exceptions.ClientError as e:
            raise KeywordError(e)

    @keyword('Download File')
    def download_file_from_s3(self, bucket, key, path, endpoint_url=None):
        """ Downloads File from S3 Bucket
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
                    @param: ```path``` which is the local path of file.
                    @param: ```endpoint_url``` optionally override the s3 endpoint url
            Example:
            | Download File | bucket | path | key |
        """
        client = self.state.session.client('s3', endpoint_url=endpoint_url)
        try:
            client.download_file(bucket, key, path)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == '404':
                raise KeywordError(f"Keyword: {bucket} does not exist")
            else:
                self.rb_logger.debug(e)

    @keyword('Upload File')
    def upload_file(self, bucket, key, path, endpoint_url=None):
        """ Uploads File from S3 Bucket
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
                    @param: ```path``` which is the local path of file.
                    @param: ```endpoint_url``` optionally override the s3 endpoint url
            Example:
            | Upload File | bucket | path | key |
        """
        client = self.state.session.client('s3', endpoint_url=endpoint_url)
        try:
            client.upload_file(path, bucket, key)
            response = client.head_object(
                Bucket=bucket,
                Key=key
            )
            self.rb_logger.info(response)
        except botocore.exceptions.S3 as e:
            if e.response['Error']:
                raise KeywordError(e)
            else:
                raise ContinuableError(e)

    @keyword('Key Should Exist')
    def key_should_exist(self, bucket, key, endpoint_url=None):
        """ Key Should Exist
        Description: Checks to see if the file on the s3 bucket exist. If so, the keyword will not fail.
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
                    @param: ```endpoint_url``` optionally override the s3 endpoint url
            Example:
            | Key Should Exist | bucket | key |
        """
        client = self.state.session.client("s3", endpoint_url=endpoint_url)
        try:
            client.head_object(Bucket=bucket, Key=key)
        except botocore.exceptions.ClientError:
            raise Exception(f"Key: {key} does not exist inside {bucket}")
        return True

    @keyword('Key Should Not Exist')
    def key_should_not_exist(self, bucket, key, endpoint_url=None):
        """ Verifies Key on S3 Bucket Does Not Exist
        Description: Checks to see if the file on the s3 bucket exist. If so, the keyword will fail.
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
                    @param: ```endpoint_url``` optionally override the s3 endpoint url
            Example:
            | Key Should Not Exist | bucket | key |
        """
        client = self.state.session.client('s3', endpoint_url=endpoint_url)
        self.rb_logger.info(f"Retrieve Client Hanlder: {client}")
        try:
            res = client.head_object(Bucket=bucket, Key=key)
            if res['ResponseMetadata']['HTTPStatusCode'] == 200:
                raise KeywordError("Key: {}, already exists".format(key))
        except botocore.exceptions.ClientError as e: # noqa
            if e.response['ResponseMetadata']['HTTPStatusCode'] != 404:
                raise ContinuableError("Error at: {} with data {}".format(e.operation_name, e.response))

    @keyword('Allowed Methods')
    def allowed_methods(self, bucket, methods=[], endpoint_url=None):
        client = self.state.session.client("s3", endpoint_url=endpoint_url)
        self.rb_logger.info(f"Retrieve Client Hanlder: {client}")
        try:
            response = client.get_bucket_cors(Bucket=bucket)
            obj = response['CORSRules'][0]
            aws_methods = obj['AllowedMethods']
            assert set(aws_methods) == set(methods)
        except botocore.exceptions.ClientError as e:
            raise KeywordError(e)
