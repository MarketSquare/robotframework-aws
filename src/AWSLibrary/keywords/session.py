from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.String import String
from robot.utils import ConnectionCache
from robot.utils.dotdict import DotDict
from robot.api import logger
from os import getenv
import boto3, logging



class SessionManager(object):
    
    def __init__(self):
        self._builtin       = BuiltIn()
        self.logger         = logging.getLogger(__name__)
        self._cache         = ConnectionCache('No sessions.')
        self.session        = None

    def create_session_with_keys(self, region):
        self.logger.debug("Starting Create session with keys")
        session = boto3.Session(
            aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=region
        )
        self._builtin.log("Creating Session: %s" % region)
        self._cache.register(session, alias=region)
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
        logger.console(self._cache._connections)

    def _get_client(self, session, service):
        return session.client(service)

    def _get_resource(self, session, service):
        return session.resource(service)