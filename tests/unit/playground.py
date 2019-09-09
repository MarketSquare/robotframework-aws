# flake8: noqa

from robot.utils import ConnectionCache
import os
from AWSLibrary import AWSLibrary
from AWSLibrary.keywords import SessionKeywords
import boto3

import unittest

from AWSLibrary import AWSLibrary


class KeywordMethods:

    @classmethod
    def setup(cls):
        cls.aws = AWSLibrary()

    def kw_method_name(cls):
        print(cls.aws.keywords)

from os import getenv
a = getenv('ACCESS_KEY')
b = getenv('SECRET_KEY')
    
def main():
    r = KeywordMethods.setup()
    r.kw_method_name()
    # lib = AWSLibrary.run_keyword(SessionKeywords, 'us-east-1', a, b)
    # s = lib.create_session_with_keys("us-east-1", a, b)

    # lib.download_file_from_s3("zappastaticbin", "test.html", "static/downloaded_test.html")


if __name__ == "__main__":
    main()




# class TestSession(unittest.TestCase):

#     def setUp(self):
#         SessionKeywords.__bases__ = (Fake.imitate(AWSLibrary, LibraryComponent),)

#     def test_works(self):
        
#     def test_create_session_with_keys(self, monkeypatch):
#         with patch('AWSLibrary.keywords.session.boto3') as mock_session:
#             mock_session.Session = "Session(region_name='us-east-1')"
