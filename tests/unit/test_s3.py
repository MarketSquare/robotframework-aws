import sys, os, unittest, uuid
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
        self.bucket = 'robotramework-aws-mock-test'
        self.key = "index-test.txt"
        self.value = "Placeholder string"

    @mock_s3
    def __moto_setup(self):
        """
            Simulate s3 file upload
        """
        session = AWSLibrary.SessionManager(self.access_key, self.secret_key)
        s3 = session.get_client()
        b = s3.create_bucket(Bucket=self.bucket)
        file = s3.put_object(Bucket=self.bucket, Key=self.key, Body=self.value)
    
    def tearDown(self):
        """
        tearDown will run after execution of each test case
        """
        pass

    @mock_s3
    def test_list_s3_buckets(self):
        self.__moto_setup()
        buckets = [b for b in self.s3.list_buckets()]
        self.assertTrue(self.bucket in buckets)

    @mock_s3
    def test_list_objects(self):
        """
        check that object is in bucket as expected
        """

        # setup s3 environment
        self.__moto_setup()

        objects = [o for o in self.s3.list_objects(self.bucket)]
        self.assertTrue(self.key in objects)