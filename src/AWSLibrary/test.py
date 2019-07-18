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

class S3Manager(object):

    def __init__(self):
        self.bucket = None

    def list_buckets(self):
        client = self.get_client()
        if self.get_client == None:
            return "First set client"
        return client.list_buckets()

    def get_bucket(self, bname):
        s3 = self.r_session
        if s3 == None:
            s3 = self.get_resource()
        self.bucket = s3.Bucket(bname)
        return self.bucket

    def get_object(self, bucket_name, obj):
        client = self.get_client()
        if self.client == None:
            client = self.get_client()
        
        bucket = bucket_name
        resp = client.get_object(Bucket=bucket_name, Key=obj)  
        print(resp['Body'].read())
        return resp
     

class AWSLibrary(SessionManager, S3Manager):

    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key
        super(AWSLibrary, self).__init__(access_key, secret_key)


def main():
    aws = AWSLibrary("AKIAVXUJU3VU6VEYSHJD", "PQxrDqUwjC9wtetHSICI1OKBW1cGSE8ar8Sxce9f")
    aws.create_session('us-east-1')
    print(aws.get_bucket('zappastaticbin'))
    print(aws.get_object('zappastaticbin', 'static/js/jquery.cookie.js'))
    # client = aws.get_client()
    # response = client.list_objects(Bucket='zappastaticbin')
    # for content in response['Contents']:
    #     obj_dict = client.get_object(Bucket='zappastaticbin', Key=content['Key'])
    #     print(content['Key'], obj_dict['LastModified'])


if __name__ == '__main__':
    main()
