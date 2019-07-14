from AWSLibrary.Keywords import SessionManager
from AWSLibrary.version import version


class AWSLibrary(SessionManager):

    ROBOT_EXIT_ON_FAILURE = True
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    """AWSLibrary is a testing library for Robot Framework
    that gives you the ability to use many of the AWS services in your tests. This library directly
    interacts with Boto3.

    Examples:
    | `Create Session` | us-west-2 | access_key=key | secret_key=secret | label=oregon    |
    """


    def __init__(self):
        """AWSLibrary requires access and secret key as params.
        Examples:
        | Library `|` AWSLibrary | ACCESS_KEY |  SECRET_KEY
        """

        for base in AWSLibrary.__bases__:
            base.__init__(self)