import sys, os, unittest
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from boto3.session import Session
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from robot.utils import ConnectionCache
from AWSLibrary import SessionManager



class SessionManagerTests(unittest.TestCase):
    """Session Manager keyword test class."""

    def setUp(self):
        self.access_key = os.environ.get('ACCESS_KEY')
        self.secret_key = os.environ.get('SECRET_KEY')
        """Instantiate the session manager class."""
        self.region = 'us-east-1'
        self.session = SessionManager(self.access_key, self.secret_key)
        

    def test_class_should_initiate(self):
        """Class init should instantiate required classes."""
        self.assertIsInstance(self.session._builtin, BuiltIn)
        self.assertIsInstance(self.session._cache, ConnectionCache)

    def test_create_should_register_new_session(self):
        session = self.session.create_session(self.region)
        self.assertEqual(session.region_name, self.region)
        try:
            self.session._cache.switch(self.region)
        except RuntimeError:
            self.fail("Session '%s' should Exist")
        self.session.delete_all_sessions()
        
    def test_get_client(self):
        s3 = self.session.get_client()
        self.assertEqual(s3._endpoint.host, "https://s3.amazonaws.com")

    def test_delete_session(self):
        aws_session = self.session.create_session(self.region)
        self.session.delete_session(self.region)
        self.session.delete_all_sessions()


    