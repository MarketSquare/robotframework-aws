from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.String import String
from robot.utils import ConnectionCache
from robot.utils.dotdict import DotDict
from robot.api import logger
import boto3


class SessionManager(object):
    
    def __init__(self, access_key, secret_key):
        self._builtin       = BuiltIn()
        self._cache         = ConnectionCache('No sessions.')
        self.session        = None
        self.r_session      = None
        self.client         = None
    

    def create_session(self, region, profile=None):
        # creds = dict(enumerate(args))
        # region = creds.get(0, kwargs.pop('region', None))

        if self.session == None:
            session = boto3.Session(
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
                region_name=region
                )
            self.session = session
        
        
        self._builtin.log("Creating Session: %s" % region)
        self._cache.register(session, alias=region)
        return self.session

    def delete_session(self, region):
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
        self._cache._aliases['x-%s-x' % region] = self._cache._aliases.pop(region)

    def delete_all_sessions(self):
        """ Delete All Sessions """
        self._cache.empty_cache()


    def get_client(self, service='s3'):
        if self.client == None:
            client = boto3.client(service,
                    aws_access_key_id=self.access_key,
                    aws_secret_access_key=self.secret_key,
                    region_name = self.session.region_name
                )
            self.client = client
        return self.client

    def get_resource(self, resource='s3'):
        session = self.session

        if self.session == None:
            session = self.create_session()

        r_session = session.resource(resource)
        self.r_session = r_session
        return self.r_session
