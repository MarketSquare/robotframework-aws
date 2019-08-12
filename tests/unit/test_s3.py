import sys, os, unittest
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
from moto import mock_s3
import boto3
import AWSLibrary


class S3ManagerTests(unittest.TestCase):

    def setUp(self):
        self.library = AWSLibrary()
        self.bucket = "ddsvdsdsfdsfsdfdsfsdfsdfdfs"
        self.key = "fake_file.txt"
        self.value = "Test File"
        """Instantiate the session manager class."""
        self.region = 'us-east-1'
        self.client = boto3.client(
            region_name=self.region,
            aws_access_key_id=getenv('ACCESS_KEY'),
            aws_secret_access_key=getenv('SECRET_KEY')
        )

    @mock_s3
    def __moto_setup(self):
        """
        Simulate s3 file upload
        """
        try:
            s3 = boto3.resource(
                "s3",
                region_name=self.region,
                aws_access_key_id=getenv('ACCESS_KEY'),
                aws_secret_access_key=getenv('SECRET_KEY')
            )
            s3.meta.client.head_bucket(Bucket=self.bucket)
        except botocore.exceptions.ClientError:
            pass
        else:
            err = "{bucket} should not exist.".format(bucket=MY_BUCKET)
            raise EnvironmentError(err)

        self.client.create_bucket(Bucket=self.bucket)
        s3.put_object(Bucket=self.bucket, Key=self.key, Body=self.value)

    @mock_s3
    def download_file(self, bucket, path, key):

        self.__moto_setup()
        with tempfile.TemporaryDirectory() as tmpdir:
            self.library.download_file(self.bucket, self.key, tmpdir)
            mock_folder_local_path = os.path.join(tmpdir, self.key)
            self.assertTrue(os.path.isdir(mock_folder_local_path))