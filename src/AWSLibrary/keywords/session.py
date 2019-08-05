from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.String import String
from robot.utils import ConnectionCache
from robot.utils.dotdict import DotDict
from robot.api import logger
import boto3, logging


class SessionManager(object):
    
    def __init__(self):
        boto3.set_stream_logger('boto3', logging.INFO)
        self._builtin       = BuiltIn()
        self._cache         = ConnectionCache('No sessions.')
        self.session        = None

    def create_session_with_keys(self, region, access_key, secret_key):
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )

        self._builtin.log("Creating Session: %s" % region)
        self._cache.register(session, alias=region)
        self.session = session
        return session
        
    def create_session_with_profile(self, profile):
        session = boto3.Session(
            profile_name=profile
        )
        logger.console(session)
        self._builtin.log("Creating Session with Profile: %s" % profile)
        self._cache.register(session, alias=session.region_name)
        self.session = session
        return session


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

    def delete_all_sessions(self):
        """ Delete All Sessions """
        self._cache.empty_cache()

    def get_client(self, service):
        if self.session == None:
            raise Exception("No Session")
        client = self.session.client('s3')
        return client

    def get_resource(self, service='s3'):
        resource = self.session.resource(service)
        self.resource = resource
        return resource
