import sys, os, unittest
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
from moto import mock_s3
from AWSLibrary import S3Manager, SessionManager
import AWSLibrary

class S3TestCase(unittest.TestCase):

    def setUp(self):
        self.access_key = os.environ.get('ACCESS_KEY')
        self.secret_key = os.environ.get('SECRET_KEY')
        self.s3 = S3Manager(self.access_key, self.secret_key)
        self.session = SessionManager(self.access_key, self.secret_key)
        self.bucket = "aws_s3_test"
        self.key = "index-test.html"
        self.value = "static/index.html"

    @mock_s3
    def __moto_setup(self):
        """
        Simulate s3 file upload
        """
        session = AWSLibrary.SessionManager(self.access_key, self.secret_key)
        s3 = session.get_client()
        s3.create_bucket(Bucket=self.bucket)
        s3.put_object(Bucket=self.bucket, Key=self.key, Body=self.value)

    
    @mock_s3
    def test_list_s3_buckets(self):
        self.__moto_setup()
        buckets = [b for b in self.s3.list_buckets()]
        self.assertTrue(self.bucket in buckets)