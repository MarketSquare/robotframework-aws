import unittest

from AWSLibrary import AWSLibrary


class TestKeywordMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.aws = AWSLibrary()

    def test_kw_method_name(self):
        self.assertTrue(self.aws.keywords['Create Session With Keys'])
        self.assertTrue(self.aws.attributes['create_session_with_keys'])