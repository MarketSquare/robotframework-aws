from AWSLibrary.keywords import SessionManager, S3Manger
from AWSLibrary.version import get_version


__version__ = get_version()


class AWSLibrary(SessionManager, S3Manager):

    ROBOT_EXIT_ON_FAILURE = True
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    """AWSLibrary is a testing library for Robot Framework
    that gives you the ability to use many of the AWS services in your tests. This library directly
    interacts with Boto3.

    Examples:
    | `Create Session` | us-west-2 | access_key=key | secret_key=secret | label=oregon    |
    """


    def __init__(self, access_key, secret_key):
        """AWSLibrary requires access and secret key as params.
        Examples:
        | Library `|` AWSLibrary | ACCESS_KEY |  SECRET_KEY
        """
        self.access_key = access_key
        self.secret_key = secret_key
        super(AWSLibrary, self).__init__(access_key, secret_key)


