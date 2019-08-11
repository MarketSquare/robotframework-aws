from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.String import String
from robot.utils import ConnectionCache
from robot.utils.dotdict import DotDict
from robot.api import logger
from os import getenv
import boto3, logging, os
from AWSLibrary.base import DynamicCore
import logging
import logging.config
from AWSLibrary.keywords import (
    SessionManager,
    S3Manager
)
from AWSLibrary.version import get_version   

__version__ = get_version()

class AWSLibrary(DynamicCore):

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
        libraries = [
            SessionManager(self),
            S3Manager(self),
        ]
        self._builtin       = BuiltIn()
        self.logger         = logging.getLogger(__name__)
        self._cache         = ConnectionCache('No sessions.')
        DynamicCore.__init__(self, libraries)



