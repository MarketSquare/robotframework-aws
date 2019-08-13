from robot.libraries.String import String
from robot.utils import ConnectionCache
from robot.utils.dotdict import DotDict
from robot.api import logger
from AWSLibrary.base import LibraryComponent
from AWSLibrary.base.robotlibcore import keyword
from os import getenv
import boto3, logging, os


class SessionKeywords(LibraryComponent):

    def __init__(self, state):
        LibraryComponent.__init__(self, state)
        self._cache         = ConnectionCache('No sessions.')

    @keyword('Create Session With Keys')
    def create_session_with_keys(self, region):
        """Takes Region as an argument and creates as session with your access key
        and secret key stored at ~/.aws/credentials. Will throw error if not configured

        Examples:
        | Create Session With Keys | us-west-1 |
        """
        self.logger.debug("Starting Create session with keys")
        session = boto3.Session(
            aws_access_key_id=getenv('ACCESS_KEY'),
            aws_secret_access_key=getenv('SECRET_KEY'),
            region_name=region
        )
        self._builtin.log("Creating Session: %s" % region)
        self._cache.register(session, alias=region)
        self.state.session = session

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
        logger.console(self._cache._connections)