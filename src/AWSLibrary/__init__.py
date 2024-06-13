from AWSLibrary.base import DynamicCore
from AWSLibrary.keywords import (
    SessionKeywords,
    S3Keywords,
    ResourceKeywords
)
from AWSLibrary.version import get_version

__version__ = get_version()


class AWSLibrary(DynamicCore):

    ROBOT_EXIT_ON_FAILURE = True
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    """AWSLibrary is a testing library for Robot Framework
    that gives you the ability to use many of the AWS services in your tests. 
    This library directly interacts with Boto3.

    Examples:
    | `Create Session` | us-west-2 |
    """

    def __init__(self):
        """
        Initialization:
        AWSLibrary requires access and secret key to currently be stored as environment variables.
        Examples:
        | Library `|` AWSLibrary |

        Inheritance:
        You can directly access all keywords from this class.
        Class state is transfered with LibraryComponent
        """
        libraries = [
            SessionKeywords(self),
            S3Keywords(self),
            ResourceKeywords(self),
            # RDSKeywords(self)
        ]
        DynamicCore.__init__(self, libraries)
