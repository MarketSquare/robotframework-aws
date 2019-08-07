import sys, os, unittest
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from boto3.session import Session
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from robot.utils import ConnectionCache
from AWSLibrary import AWSLibrary
from AWSLibrary.keywords import SessionManager



class SessionManagerTests(unittest.TestCase):
    """Session Manager keyword test class."""

    def setUp(self):
        self.library = AWSLibrary() 
        self.aws_profile = 'default'
        """Instantiate the session manager class."""
        self.region = 'us-east-1'
        self.session_class = SessionManager()    

    def test_class_should_initiate(self):
        """Class init should instantiate required classes."""
        self.assertIsInstance(self.library._builtin, BuiltIn)
        self.assertIsInstance(self.library._cache, ConnectionCache)

    def test_create_session_with_keys(self):
        session = self.library.create_session_with_keys(self.region)
        self.assertEqual(session.region_name, self.region)
        try:
            self.library._cache.switch(session.region_name)
        except RuntimeError as e:
            self.fail(e)
        self.library.delete_all_sessions()

    def test_delete_all_sessions(self):
        session = self.library.create_session_with_keys(self.region)
        self.library.delete_all_sessions()
        with self.assertRaises(RuntimeError):
            self.library._cache.get_connection('us-east-1')
        self.assertTrue("Non existing index or alias '%s'." % session.region_name)

    