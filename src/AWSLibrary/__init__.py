import logging
import logging.config
import yaml
from AWSLibrary.keywords import SessionManager
from AWSLibrary.version import get_version

with open('logger_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
    



class FatalError(RuntimeError):
    ROBOT_EXIT_ON_FAILURE = True

class KeywordError(RuntimeError):
    ROBOT_SUPPRESS_NAME = True

class ContinuableError(RuntimeError):
    ROBOT_CONTINUE_ON_FAILURE = True

__version__ = get_version()

class AWSLibrary(SessionManager):

    ROBOT_EXIT_ON_FAILURE = True
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    """AWSLibrary is a testing library for Robot Framework
    that gives you the ability to use many of the AWS services in your tests. This library directly
    interacts with Boto3.

    Examples:
    | `Create Session` | us-west-2 |
    """


    def __init__(self):
        """AWSLibrary requires access and secret key as params.
        Examples:
        | Library `|` AWSLibrary | ACCESS_KEY |  SECRET_KEY
        """
        logger = logging.getLogger(__name__)
        logger.info('Completed configuring logger()!')
        for base in AWSLibrary.__bases__:
            base.__init__(self)



