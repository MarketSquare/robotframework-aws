import unittest
import os
import sys
from unittest.mock import patch, MagicMock
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
from AWSLibrary import AWSLibrary
from AWSLibrary.keywords import SessionKeywords
from AWSLibrary.base import LibraryComponent, DynamicCore
from os import getenv
from boto3.session import Session


class TestSession(unittest.TestCase):

    def test_create_session_with_keys(self):
        mock_gobject = MagicMock()
        mock_gobject.LibraryComponent.__bases__ = (object,)
        with patch.dict('sys.modules', gobject=mock_gobject):
            kw = SessionKeywords(mock_gobject)
            lib_session = kw.create_session_with_keys(
                'us-east-1',
                getenv('ACCESS_KEY'),
                getenv('ACCESS_KEY'))

        with patch('AWSLibrary.keywords.session.boto3') as mock_session:
            ms = mock_session.Session = Session(region_name='us-east-1')

        self.assertEquals(str(lib_session), str(ms))

    def test_create_session_with_profile(self):
        mock_gobject = MagicMock()
        mock_gobject.LibraryComponent.__bases__ = (object,)
        with patch.dict('sys.modules', gobject=mock_gobject):
            kw = SessionKeywords(mock_gobject)
            lib_session = kw.create_session_with_profile(
                'us-east-1',
                getenv('PROFILE'))
                
        with patch('AWSLibrary.keywords.session.boto3') as mock_session:
            ms = mock_session.Session = Session(region_name='us-east-1')

        self.assertEquals(str(lib_session), str(ms))