from AWSLibrary.base.robotlibcore import keyword
from AWSLibrary.base import LibraryComponent
from robot.api import logger
import botocore


class S3Keywords(LibraryComponent):

    # begin of deprecated keywords

    @keyword('Create Bucket')
    def create_bucket(self, bucket, endpoint_url=None):
        """
        *DEPRECATED - this keyword will be removed in version 2.0.0* use `S3 Create Bucket` instead

        Creates S3 Bucket with the name given @param: ```bucket```
            and uses the optionally provided @param: ```endpoint_url```.
            If Bucket already exists, an exception will be thrown.

        Example:
        | Create Bucket | randomBucketName |
        """
        logger.warn("Keyword 'Create Bucket' is deprecated. Use keyword 'S3 Create Bucket' instead")
        client = self.state.session.client('s3', endpoint_url=endpoint_url)
        try:
            client.create_bucket(Bucket=bucket)
            logger.debug(f"Created new bucket: {bucket}")
        except botocore.exceptions.ClientError as e:
            error_code = e.response["Error"]["Code"]
            if error_code == "BucketAlreadyExists":
                self.logger.debug(f"Keyword Failed: {error_code}")
                raise Exception(f"Keyword Failed: {error_code}")
            elif error_code == 'BucketAlreadyOwnedByYou':
                self.logger.debug("Bucket Already Exists")
                raise Exception("Bucket Already Exists")
            else:
                Exception(f"Error Code: {e.response['Error']['Code']}")

    @keyword('List Objects')
    def list_objects(self, bucket, prefix=""):
        """
        *DEPRECATED - this keyword will be removed in version 2.0.0* use `S3 List Objects` instead

        List Objects
        Requires:   @param: ```bucket``` which is the bucket name
        Optional:   @param: ```prefix``` which limits the response to keys that begin with the specified prefix.
            Example:
            | List Objects | bucket | key |
        """
        logger.warn("Keyword 'List Objects' is deprecated. Use keyword 'S3 List Objects' instead")
        client = self.state.session.client('s3')
        try:
            response = client.list_objects_v2(
                Bucket=bucket,
                Prefix=prefix
            )
            if 'Contents' in response:
                return [key['Key'] for key in response['Contents']]
            else:
                return []
        except botocore.exceptions.ClientError as e:
            raise Exception(e)

    @keyword('Delete File')
    def delete_file(self, bucket, key, endpoint_url=None):
        """
        *DEPRECATED - this keyword will be removed in version 2.0.0* use `S3 Delete File` instead

        Delete File
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
                    @param: ```endpoint_url``` optionally override the s3 endpoint url
            Example:
            | Delete File | bucket | key |
        """
        logger.warn("Keyword 'Delete File' is deprecated. Use keyword 'S3 Delete File' instead")
        client = self.state.session.client('s3', endpoint_url=endpoint_url)
        try:
            response = client.delete_object(
                Bucket=bucket,
                Key=key
            )
            logger.info(response)
        except botocore.exceptions.ClientError as e:
            raise Exception(e)

    @keyword('Download File')
    def download_file_from_s3(self, bucket, key, path, endpoint_url=None):
        """
        *DEPRECATED - this keyword will be removed in version 2.0.0* use `S3 Download File` instead

        Downloads File from S3 Bucket
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
                    @param: ```path``` which is the local path of file and it´s name.
                    @param: ```endpoint_url``` optionally override the s3 endpoint url
            Example:
            | Download File | bucket | key | file.txt |
        """
        logger.warn("Keyword 'Download File' is deprecated. Use keyword 'S3 Download File' instead")
        client = self.state.session.client('s3', endpoint_url=endpoint_url)
        try:
            client.download_file(bucket, key, path)
        except botocore.exceptions.ClientError as e:
            raise Exception(e)

    @keyword('Upload File')
    def upload_file(self, bucket, key, path, endpoint_url=None):
        """
        *DEPRECATED - this keyword will be removed in version 2.0.0* use `S3 Upload File` instead

        Uploads File from S3 Bucket
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
                    @param: ```path``` which is the local path of file.
                    @param: ```endpoint_url``` optionally override the s3 endpoint url
            Example:
            | Upload File | bucket | path | key |
        """
        logger.warn("Keyword 'Upload File' is deprecated. Use keyword 'S3 Upload File' instead")
        client = self.state.session.client('s3', endpoint_url=endpoint_url)
        try:
            client.upload_file(path, bucket, key)
            response = client.head_object(
                Bucket=bucket,
                Key=key
            )
            logger.info(response)
        except botocore.exceptions.ClientError as e:
            raise Exception(e)

    @keyword('Key Should Exist')
    def key_should_exist(self, bucket, key, endpoint_url=None):
        """
        *DEPRECATED - this keyword will be removed in version 2.0.0* use `S3 Key Should Exist` instead

        Key Should Exist
        Description: Checks to see if the file on the s3 bucket exist. If so, the keyword will not fail.
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
                    @param: ```endpoint_url``` optionally override the s3 endpoint url
            Example:
            | Key Should Exist | bucket | key |
        """
        logger.warn("Keyword 'Key Should Exist' is deprecated. Use keyword 'S3 Key Should Exist' instead")
        client = self.state.session.client("s3", endpoint_url=endpoint_url)
        try:
            client.head_object(Bucket=bucket, Key=key)
        except botocore.exceptions.ClientError:
            raise Exception(f"Key: {key} does not exist inside {bucket}")
        return True

    @keyword('Key Should Not Exist')
    def key_should_not_exist(self, bucket, key, endpoint_url=None):
        """
        *DEPRECATED - this keyword will be removed in version 2.0.0* use `S3 Key Should Not Exist` instead

        Verifies Key on S3 Bucket Does Not Exist
        Description: Checks to see if the file on the s3 bucket exist. If so, the keyword will fail.
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
                    @param: ```endpoint_url``` optionally override the s3 endpoint url
            Example:
            | Key Should Not Exist | bucket | key |
        """
        logger.warn("Keyword 'Key Should Not Exist' is deprecated. Use keyword 'S3 Key Should Not Exist' instead")
        client = self.state.session.client('s3', endpoint_url=endpoint_url)
        try:
            response = client.head_object(Bucket=bucket, Key=key)
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                raise Exception(f"Key: {key} exist inside {bucket}")
        except botocore.exceptions.ClientError as e:  # noqa
            if e.response['ResponseMetadata']['HTTPStatusCode'] != 404:
                raise Exception(e)

    # end of deprecated keywords

    @keyword('S3 Create Bucket')
    def s3_create_bucket(self, bucket, endpoint_url=None):
        """ Creates S3 Bucket with the name given @param: ```bucket```
            and uses the optionally provided @param: ```endpoint_url```.
            If Bucket already exists, an exception will be thrown.

        Example:
        | Create Bucket | randomBucketName |
        """
        client = self.state.session.client('s3', endpoint_url=endpoint_url)
        try:
            client.create_bucket(Bucket=bucket)
            logger.debug(f"Created new bucket: {bucket}")
        except botocore.exceptions.ClientError as e:
            error_code = e.response["Error"]["Code"]
            if error_code == "BucketAlreadyExists":
                self.logger.debug(f"Keyword Failed: {error_code}")
                raise Exception(f"Keyword Failed: {error_code}")
            elif error_code == 'BucketAlreadyOwnedByYou':
                self.logger.debug("Bucket Already Exists")
                raise Exception("Bucket Already Exists")
            else:
                Exception(f"Error Code: {e.response['Error']['Code']}")

    @keyword('S3 List Objects')
    def s3_list_objects(self, bucket, prefix=""):
        """ List Objects
        Requires:   @param: ```bucket``` which is the bucket name
        Optional:   @param: ```prefix``` which limits the response to keys that begin with the specified prefix.
            Example:
            | List Objects | bucket | key |
        """
        client = self.state.session.client('s3')
        try:
            response = client.list_objects_v2(
                Bucket=bucket,
                Prefix=prefix
            )
            if 'Contents' in response:
                return [key['Key'] for key in response['Contents']]
            else:
                return []
        except botocore.exceptions.ClientError as e:
            raise Exception(e)

    @keyword('S3 Delete File')
    def s3_delete_file(self, bucket, key, endpoint_url=None):
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
            logger.info(response)
        except botocore.exceptions.ClientError as e:
            raise Exception(e)

    @keyword('S3 Download File')
    def s3_download_file_from_s3(self, bucket, key, path, endpoint_url=None):
        """ Downloads File from S3 Bucket
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
                    @param: ```path``` which is the local path of file and it´s name.
                    @param: ```endpoint_url``` optionally override the s3 endpoint url
            Example:
            | Download File | bucket | key | file.txt |
        """
        client = self.state.session.client('s3', endpoint_url=endpoint_url)
        try:
            client.download_file(bucket, key, path)
        except botocore.exceptions.ClientError as e:
            raise Exception(e)

    @keyword('S3 Upload File')
    def s3_upload_file(self, bucket, key, path, endpoint_url=None):
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
            logger.info(response)
        except botocore.exceptions.ClientError as e:
            raise Exception(e)

    @keyword('S3 Key Should Exist')
    def s3_key_should_exist(self, bucket, key, endpoint_url=None):
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

    @keyword('S3 Key Should Not Exist')
    def s3_key_should_not_exist(self, bucket, key, endpoint_url=None):
        """ Verifies Key on S3 Bucket Does Not Exist
        Description: Checks to see if the file on the s3 bucket exist. If so, the keyword will fail.
        Requires:   @param ```bucket``` which is the bucket name:
                    @param: ```key``` which is the bucket location/path name.
                    @param: ```endpoint_url``` optionally override the s3 endpoint url
            Example:
            | Key Should Not Exist | bucket | key |
        """
        client = self.state.session.client('s3', endpoint_url=endpoint_url)
        try:
            response = client.head_object(Bucket=bucket, Key=key)
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                raise Exception(f"Key: {key} exist inside {bucket}")
        except botocore.exceptions.ClientError as e:  # noqa
            if e.response['ResponseMetadata']['HTTPStatusCode'] != 404:
                raise Exception(e)
