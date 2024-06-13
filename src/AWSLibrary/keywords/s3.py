from robot.api.deco import keyword
from AWSLibrary.base import LibraryComponent
from robot.api import logger
import botocore


class S3Keywords(LibraryComponent):

    # begin of deprecated keywords

    @keyword('Create Bucket')
    def create_bucket(self, bucket, endpoint_url=None):
        """
        *DEPRECATED - this keyword will be removed in version 2.0.0* use `S3 Create Bucket` instead

        Creates S3 Bucket with the given bucket name

        | =Arguments= | =Description= |
        | ``bucket`` | <str> The bucket name. |

        *Examples:*
        | Create bucket _name | bucket_name |
        """
        logger.warn("Keyword 'Create Bucket' is deprecated. Use keyword 'S3 Create Bucket' instead")
        client = self.library.session.client('s3', endpoint_url=endpoint_url)
        try:
            client.create_bucket(Bucket=bucket)
            logger.debug(f"Created new bucket: {bucket}")
        except botocore.exceptions.ClientError as e:
            error_code = e.response["Error"]["Code"]
            if error_code == "BucketAlreadyExists":
                logger.debug(f"Keyword Failed: {error_code}")
                raise Exception(f"Keyword Failed: {error_code}")
            elif error_code == 'BucketAlreadyOwnedByYou':
                logger.debug("Bucket Already Exists")
                raise Exception("Bucket Already Exists")
            else:
                Exception(f"Error Code: {e.response['Error']['Code']}")

    @keyword('List Objects')
    def list_objects(self, bucket, prefix=""):
        """
        *DEPRECATED - this keyword will be removed in version 2.0.0* use `S3 List Objects` instead

        List objects in a bucket. (up to 1,000) each request

        If prefix is informed will list only the files that start with this string,
        could be used to list only the files inside a folder for example.

        | =Arguments= | =Description= |
        | ``bucket`` | <str> The bucket name. |
        | ``Prefix`` | <str> prefix of the filepath. |

        *Examples:*
        | List Objects | bucket_name |
        | List Objects | bucket_name | folder_name |
        | List Objects | bucket_name | folder_name/start_of_the_filename |
        """
        logger.warn("Keyword 'List Objects' is deprecated. Use keyword 'S3 List Objects' instead")
        client = self.library.session.client('s3')
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

        Deletes the file from a bucket

        | =Arguments= | =Description= |
        | ``bucket`` | <str> The bucket name. |
        | ``key`` | <str> complete filepath. |

        *Examples:*
        | Delete File | bucket_name | file.txt |
        | Delete File | bucket_name | folder/file.txt |
        """
        logger.warn("Keyword 'Delete File' is deprecated. Use keyword 'S3 Delete File' instead")
        client = self.library.session.client('s3', endpoint_url=endpoint_url)
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

        Download file from a bucket

        | =Arguments= | =Description= |
        | ``bucket`` | <str> The bucket name. |
        | ``key`` | <str> complete filepath. |
        | ``path`` | <str> Complete local filepath. |

        *Examples:*
        | Download File | bucket_name | s3_file.txt | ${OUTPUTDIR}/file.txt |
        | Download File | bucket_name | folder/s3_file.txt | ${OUTPUTDIR}/file.txt |
        """
        logger.warn("Keyword 'Download File' is deprecated. Use keyword 'S3 Download File' instead")
        client = self.library.session.client('s3', endpoint_url=endpoint_url)
        try:
            client.download_file(bucket, key, path)
        except botocore.exceptions.ClientError as e:
            raise Exception(e)

    @keyword('Upload File')
    def upload_file(self, bucket, key, path, endpoint_url=None):
        """
        *DEPRECATED - this keyword will be removed in version 2.0.0* use `S3 Upload File` instead

        Upload a file to the bucket

        | =Arguments= | =Description= |
        | ``bucket`` | <str> The bucket name. |
        | ``key`` | <str> complete s3 filepath. |
        | ``path`` | <str> Complete local filepath. |

        *Examples:*
        | Upload File | bucket_name | s3_file.txt | ${CURDIR}/file.txt |
        | Upload File | bucket_name | folder/s3_file.txt | ${CURDIR}/file.txt |
        """
        logger.warn("Keyword 'Upload File' is deprecated. Use keyword 'S3 Upload File' instead")
        client = self.library.session.client('s3', endpoint_url=endpoint_url)
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

        Check if the s3 object exist inside the bucket

        | =Arguments= | =Description= |
        | ``bucket`` | <str> The bucket name. |
        | ``key`` | <str> complete s3 filepath. |

        *Examples:*
        | Key Should Exist | bucket_name | s3_file.txt |
        | Key Should Exist | bucket_name | folder/s3_file.txt |
        """
        logger.warn("Keyword 'Key Should Exist' is deprecated. Use keyword 'S3 Key Should Exist' instead")
        client = self.library.session.client("s3", endpoint_url=endpoint_url)
        try:
            client.head_object(Bucket=bucket, Key=key)
        except botocore.exceptions.ClientError:
            raise Exception(f"Key: {key} does not exist inside {bucket}")
        return True

    @keyword('Key Should Not Exist')
    def key_should_not_exist(self, bucket, key, endpoint_url=None):
        """
        *DEPRECATED - this keyword will be removed in version 2.0.0* use `S3 Key Should Not Exist` instead

        Check if the s3 object not exist inside the bucket

        | =Arguments= | =Description= |
        | ``bucket`` | <str> The bucket name. |
        | ``key`` | <str> complete s3 filepath. |

        *Examples:*
        | Key Should Not Exist | bucket_name | s3_file.txt |
        | Key Should Not Exist | bucket_name | folder/s3_file.txt |
        """
        logger.warn("Keyword 'Key Should Not Exist' is deprecated. Use keyword 'S3 Key Should Not Exist' instead")
        client = self.library.session.client('s3', endpoint_url=endpoint_url)
        try:
            response = client.head_object(Bucket=bucket, Key=key)
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                raise Exception(f"Key: {key} exist inside {bucket}")
        except botocore.exceptions.ClientError as e:  # noqa
            if e.response['ResponseMetadata']['HTTPStatusCode'] != 404:
                raise Exception(e)

    # end of deprecated keywords

    @keyword('S3 Create Bucket')
    def s3_create_bucket(self, bucket):
        """ Creates S3 Bucket with the given bucket name

        | =Arguments= | =Description= |
        | ``bucket`` | <str> The bucket name. |

        *Examples:*
        | S3 Create bucket | bucket_name |
        """
        client = self.library.session.client('s3')
        try:
            client.create_bucket(Bucket=bucket)
            logger.debug(f"Created new bucket: {bucket}")
        except botocore.exceptions.ClientError as e:
            error_code = e.response["Error"]["Code"]
            if error_code == "BucketAlreadyExists":
                logger.debug(f"Keyword Failed: {error_code}")
                raise Exception(f"Keyword Failed: {error_code}")
            elif error_code == 'BucketAlreadyOwnedByYou':
                logger.debug("Bucket Already Exists")
                raise Exception("Bucket Already Exists")
            else:
                Exception(f"Error Code: {e.response['Error']['Code']}")

    @keyword('S3 List Objects')
    def s3_list_objects(self, bucket, prefix=""):
        """ List objects in a bucket. (up to 1,000) each request

        If prefix is informed will list only the files that start with this string,
        could be used to list only the files inside a folder for example.

        | =Arguments= | =Description= |
        | ``bucket`` | <str> The bucket name. |
        | ``Prefix`` | <str> prefix of the filepath. |

        *Examples:*
        | S3 List Objects | bucket_name |
        | S3 List Objects | bucket_name | folder_name |
        | S3 List Objects | bucket_name | folder_name/start_of_the_filename |
        """
        client = self.library.session.client('s3')
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
    def s3_delete_file(self, bucket, key):
        """ Deletes the file from a bucket

        | =Arguments= | =Description= |
        | ``bucket`` | <str> The bucket name. |
        | ``key`` | <str> complete s3 filepath. |

        *Examples:*
        | S3 Delete File | bucket_name | file.txt |
        | S3 Delete File | bucket_name | folder/file.txt |
        """
        client = self.library.session.client('s3')
        try:
            response = client.delete_object(
                Bucket=bucket,
                Key=key
            )
            logger.info(response)
        except botocore.exceptions.ClientError as e:
            raise Exception(e)

    @keyword('S3 Download File')
    def s3_download_file_from_s3(self, bucket, key, local_filepath):
        """ Download file from a bucket

        | =Arguments= | =Description= |
        | ``bucket`` | <str> The bucket name. |
        | ``key`` | <str> complete s3 filepath. |
        | ``local_path`` | <str> Complete local filepath. |

        *Examples:*
        | S3 Download File | bucket_name | s3_file.txt | ${OUTPUTDIR}/file.txt |
        | S3 Download File | bucket_name | folder/s3_file.txt | ${OUTPUTDIR}/file.txt |
        """
        client = self.library.session.client('s3')
        try:
            client.download_file(bucket, key, local_filepath)
        except botocore.exceptions.ClientError as e:
            raise Exception(e)

    @keyword('S3 Upload File')
    def s3_upload_file(self, bucket, key, local_path):
        """ Upload a file to the bucket

        | =Arguments= | =Description= |
        | ``bucket`` | <str> The bucket name. |
        | ``key`` | <str> complete s3 filepath. |
        | ``local_path`` | <str> Complete local filepath. |

        *Examples:*
        | S3 Upload File | bucket_name | s3_file.txt | ${CURDIR}/file.txt |
        | S3 Upload File | bucket_name | folder/s3_file.txt | ${CURDIR}/file.txt |
        """
        client = self.library.session.client('s3')
        try:
            client.upload_file(local_path, bucket, key)
            response = client.head_object(
                Bucket=bucket,
                Key=key
            )
            logger.info(response)
        except botocore.exceptions.ClientError as e:
            raise Exception(e)

    @keyword('S3 Key Should Exist')
    def s3_key_should_exist(self, bucket, key):
        """ Check if the s3 object exist inside the bucket

        | =Arguments= | =Description= |
        | ``bucket`` | <str> The bucket name. |
        | ``key`` | <str> complete s3 filepath. |

        *Examples:*
        | S3 Key Should Exist | bucket_name | s3_file.txt |
        | S3 Key Should Exist | bucket_name | folder/s3_file.txt |
        """
        client = self.library.session.client("s3")
        try:
            client.head_object(Bucket=bucket, Key=key)
        except botocore.exceptions.ClientError:
            raise Exception(f"Key: {key} does not exist inside {bucket}")

    @keyword('S3 Key Should Not Exist')
    def s3_key_should_not_exist(self, bucket, key):
        """ Check if the s3 object not exist inside the bucket

        | =Arguments= | =Description= |
        | ``bucket`` | <str> The bucket name. |
        | ``key`` | <str> complete s3 filepath. |

        *Examples:*
        | S3 Key Should Not Exist | bucket_name | s3_file.txt |
        | S3 Key Should Not Exist | bucket_name | folder/s3_file.txt |
        """
        client = self.library.session.client('s3')
        try:
            response = client.head_object(Bucket=bucket, Key=key)
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                raise Exception(f"Key: {key} exist inside {bucket}")
        except botocore.exceptions.ClientError as e:  # noqa
            if e.response['ResponseMetadata']['HTTPStatusCode'] != 404:
                raise Exception(e)
