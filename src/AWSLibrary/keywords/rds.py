from AWSLibrary.base.robotlibcore import keyword
from AWSLibrary.base import LibraryComponent, KeywordError, ContinuableError
from botocore.exceptions import ClientError
from robot.api import logger
import botocore


class RDSKeywords(LibraryComponent):

    @keyword
    def database_exists(self):
        pass
    