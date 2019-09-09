from AWSLibrary.keywords import S3Keywords
from AWSLibrary.base import LibraryComponent
from unittest.mock import patch, MagicMock
import unittest


class TestS3Keywords(unittest.TestCase):

    def setUp(self):
        self.bucket = "test_bucket"
        self.key = "tmp/test_file.txt"
        self.path = "tmp/local.txt"

    def test_upload_file_to_bucket(self):
        mock_gobject = MagicMock()
        mock_gobject.LibraryComponent.__bases__ = (object,)
        with patch.dict('sys.modules', gobject=mock_gobject):
            kw = S3Keywords(mock_gobject)
            kw.upload_file(self.bucket, self.key, self.path)


