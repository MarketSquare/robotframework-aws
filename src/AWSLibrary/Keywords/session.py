from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.String import String
from robot.utils import ConnectionCache
import boto3


class SessionManager(object):
    
    def __init__(self, access_key, secret_key):
        self._builtin       = BuiltIn()
        self._cache         = ConnectionCache('No sessions.')
        self.session        = None
        self.r_session      = None
        self.client         = None
    

    def create_session(self, *args, **kwargs):
        creds = dict(enumerate(args))
        region = creds.get(0, kwargs.pop('region', None))
    
        if self.session == None:
            session = boto3.Session(
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
                region_name=region
                )
            self.session = session
        return self.session

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
