from AWSLibrary.base import LibraryComponent
from AWSLibrary.base.robotlibcore import keyword
from botocore.exceptions import ClientError
import os


class ResourceKeywords(LibraryComponent):

    @keyword("Local File Should Exist")
    def local_file_should_exist(self, path):
        try:
            if os.path.exists(path) == 1:
                self._builtin.log("File exists at {}".format(path)) 
                return True
        except FileNotFoundError:
            raise KeywordError("File does not exist at {}".format(path))

    @keyword("Local File Should Not Exist")
    def local_file_should_not_exist(self, path):
        try:
            if os.path.exists(path) == 0:
                self._builtin.log("File does not exist at {}".format(path)) 
                return True
        except FileNotFoundError:
            raise KeywordError("File does exist at {}".format(path))