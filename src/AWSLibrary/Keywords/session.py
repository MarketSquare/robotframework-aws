from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.String import String
from robot.utils import ConnectionCache
import boto3


class SessionManager(object):
    
    def __init__(self, access_key, secret_key):
        self._builtin       = BuiltIn()
        self._cache         = ConnectionCache('No sessions.')
        self.access_key     = access_key
        self.secret_key     = secret_key
        self.session        = None
        self.s3_session     = None
        self.client         = None
    
    def get_session(self, *args, **kwargs):

        
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

    def get_s3_session(self):
        print(self.session.access_key, "44e4")
        if self.session == None:
            session = self.get_session()
            if session is None:
                return None # Raise some error
            s3_session = session.resource("s3")
            self.s3_session = s3_session
        return self.s3_session

    
    def list_buckets(self):
        client = self.get_client()
        if self.get_client == None:
            return "First set client"
        
        return client.list_buckets()

