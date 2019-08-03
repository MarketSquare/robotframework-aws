from robot.api import logger
from botocore.exceptions import ClientError
import os

class FatalError(RuntimeError):
    ROBOT_EXIT_ON_FAILURE = True
    
class KeywordError(RuntimeError):
    ROBOT_SUPPRESS_NAME = True

class ContinuableError(RuntimeError):
    ROBOT_CONTINUE_ON_FAILURE = True


class ResourceManager(object):

    def local_file_should_exist(self, path):
        try:
            if os.path.exists(path) == 1:
                self._builtin.log("File exists at {}".format(path)) 
                return True
        except FileNotFoundError:
            raise KeywordError("File does not exist at {}".format(path))
        
    def local_file_should_not_exist(self, path):
        try:
            if os.path.exists(path) == 0:
                self._builtin.log("File does not exist at {}".format(path)) 
                return True
        except FileNotFoundError:
            raise KeywordError("File does exist at {}".format(path))