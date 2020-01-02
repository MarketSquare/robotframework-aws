from robot.utils import ConnectionCache
from AWSLibrary.base import LibraryComponent
from AWSLibrary.base.robotlibcore import keyword
import boto3


class SessionKeywords(LibraryComponent):

    def __init__(self, state):
        LibraryComponent.__init__(self, state)
        self._cache = ConnectionCache('No sessions.')

    @keyword('Create Session With Keys')
    def create_session_with_keys(self, region, access_key, secret_key):
        """Takes Region as an argument and creates as session with your access key
        and secret key stored at ~/.aws/credentials.
        Will throw error if not configured.

        Examples:
        | Create Session With Keys | us-west-1 | access key | secret key |
        """
        self.rb_logger.info("Creating Session: %s" % region)
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )
        print(session)
        self._cache.register(session, alias=region)
        self.state.session = session
        return session

    @keyword('Create Session With Profile')
    def create_session_with_profile(self, region, profile):
        """Takes Region as an argument and creates as session with your profile
         stored at ~/.aws/config. Will throw error if not configured

        Examples:
        | Create Session With Profile | us-west-1 |  profile name |
        """
        self.rb_logger.info(f"Creating Session: {region}, {profile}")
        session = boto3.Session(
            profile_name=profile,
            region_name=region
        )
        self._cache.register(session, alias=region)
        self.state.session = session
        return session

    @keyword('Delete Session')
    def delete_session(self, region, profile=None):
        """Removes session.
        Arguments:
        - ``region``: A case and space insensitive string to identify the session.
                     (Default ``region``)
        Examples:
        | Delete Session | REGION |
        """
        self._cache.switch(region)
        index = self._cache.current_index
        self._cache.current = self._cache._no_current
        self._cache._connections[index - 1] = None
        self._cache._aliases.pop(region)

    @keyword('Delete All Sessions')
    def delete_all_sessions(self):
        """ Delete All Sessions """
        self._cache.empty_cache()
