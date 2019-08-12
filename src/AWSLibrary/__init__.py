from AWSLibrary.base import DynamicCore
from AWSLibrary.keywords import (
    SessionKeywords,
    S3Keywords
)
from AWSLibrary.version import get_version  
from robot.api import logger
from os import getenv
import boto3, logging, os 

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
        libraries = [
            SessionKeywords(self),
            S3Keywords(self),
        ]
        DynamicCore.__init__(self, libraries)
        


