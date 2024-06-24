from AWSLibrary.librarycomponent import LibraryComponent
from robot.utils import ConnectionCache
from robot.api import logger
from robot.api.deco import keyword
import boto3


class SessionKeywords(LibraryComponent):

    def __init__(self, library):
        LibraryComponent.__init__(self, library)
        self._cache = ConnectionCache('No sessions.')

    @keyword('Create Session With Keys')
    def create_session_with_keys(self, region, access_key, secret_key):
        """ Create an AWS session in region using your access key and secret key.

        | =Arguments= | =Description= |
        | ``region`` | <str> The AWS region name. |
        | ``access_key`` | <str> the access key. |
        | ``secret_key`` | <str> the secret key. |

        *Examples:*
        | Create Session With Keys | eu-west-1 | access_key | secret_key |
        """
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )
        logger.info(f"Session created: {str(session)} using access key: {access_key}")
        self._cache.register(session, alias=region)
        self.library.session = session
        return session

    @keyword('Create Session With Token')
    def create_session_with_token(self, region, access_key, secret_key, token):
        """ Create an AWS session in region using access key, secret key and token.

        | =Arguments= | =Description= |
        | ``region`` | <str> The AWS region name. |
        | ``access_key`` | <str> the access key. |
        | ``secret_key`` | <str> the secret key. |
        | ``token`` | <str> the user token. |

        *Examples:*
        | Create Session With Token | eu-west-1 | access_key | secret_key | token |
        """
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token=token,
            region_name=region
        )
        logger.info(f"Session created: {str(session)} using access key: {access_key} and corresponding token")
        self._cache.register(session, alias=region)
        self.library.session = session
        return session

    @keyword('Create Session With Profile')
    def create_session_with_profile(self, region, profile):
        """Create an AWS session in region with your profile
         stored at ~/.aws/config.
        
        | =Arguments= | =Description= |
        | ``region`` | <str> The AWS region name. |
        | ``profile`` | <str> the profile name. |
        
        *Examples:*
        | Create Session With Profile | us-west-1 | profile_name |
        """
        session = boto3.Session(
            profile_name=profile,
            region_name=region
        )
        logger.info(f"Session created: {str(session)} using profile: {profile}")
        self._cache.register(session, alias=region)
        self.library.session = session
        return session

    @keyword('Create Session With Role')
    def create_session_with_role(self, region):
        """ Create an AWS session in region using current role context.

        | =Arguments= | =Description= |
        | ``region`` | <str> The AWS region name. |

        *Examples:*
        | Create Session With Role | eu-west-1 |
        """
        session = boto3.Session(region_name=region)
        logger.info(f"Session created: {str(session)} using current role context")
        self._cache.register(session, alias=region)
        self.library.session = session
        return session

    @keyword('Delete Session')
    def delete_session(self, region):
        """ Delete session by entering the region.

        | =Arguments= | =Description= |
        | ``region`` | <str> The AWS region name. |

        *Examples:*
        | Delete Session | us-west-1 |
        """
        if self._cache.current_index is None:
            logger.info("There is no active session to delete.")
        else:
            self._cache.switch(region)
            index = self._cache.current_index
            self._cache.current = self._cache._no_current
            self._cache._connections[index - 1] = None
            self._cache._aliases.pop(region)

    @keyword('Delete All Sessions')
    def delete_all_sessions(self):
        """ Delete all current sessions.

        *Examples:*
        | Delete All Sessions |
        """
        if self._cache.current_index is None:
            logger.info("There is no active session to delete.")
        else:
            self._cache.empty_cache()
