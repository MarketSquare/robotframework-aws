from AWSLibrary.librarycomponent import LibraryComponent
from robot.api.deco import keyword
from robot.api import logger
import os


class ResourceKeywords(LibraryComponent):

    @keyword("Local File Should Exist")
    def local_file_should_exist(self, path):
        """
        *DEPRECATED - this keyword will be removed in version 2.0.0*

        Verifies Local File at the given path does exist
        Requires:   @param: ```path``` which is the bucket location/path name.
            Example:
            | Local File Should Exist | bucket | path |
        """
        logger.warn("This Keyword 'Local File Should Exist' is deprecated. Use Robot Library 'OperatingSystem' instead")
        try:
            if os.path.exists(path) == 1:
                logger.info("File exists at {}".format(path))
                return True
        except FileNotFoundError:
            raise Exception("File does not exist at {}".format(path))

    @keyword("Local File Should Not Exist")
    def local_file_should_not_exist(self, path):
        """
        *DEPRECATED - this keyword will be removed in version 2.0.0*

        Verifies Local File at the given path does not exist
        Requires:   @param: ```path``` which is the bucket location/path name.
            Example:
            | Local File Should Not Exist | bucket | path |
        """
        logger.warn("This Keyword 'Local File Should Not Exist' is deprecated. Use Robot Library 'OperatingSystem' instead")
        try:
            if os.path.exists(path) == 0:
                logger.info("File does not exist at {}".format(path))
                return True
        except FileNotFoundError:
            raise Exception("File does exist at {}".format(path))
