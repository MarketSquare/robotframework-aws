from robot.api import logger
from robot import utils
from botocore.exceptions import ClientError


class FatalError(RuntimeError):
    ROBOT_EXIT_ON_FAILURE = True

class KeywordError(RuntimeError):
    ROBOT_SUPPRESS_NAME = True

class ContinuableError(RuntimeError):
    ROBOT_CONTINUE_ON_FAILURE = True


class S3Manager(object):

    def __init__(self, access_key, secret_key):
        self.bucket = None
        self.access_key = access_key
        self.secret_key = secret_key

    def list_buckets(self):
        s3 = self.get_client()
        response = s3.list_buckets()
        if response:
            for _object in response.get('Buckets', []):
                yield _object['Name']

    def list_objects(self, bucket_name):
        s3 = self.get_client()
        response = s3.list_objects(Bucket=bucket_name)
        if response:
            for _object in response.get('Contents', []):
                yield _object['Key']

    def get_bucket(self, bucket_name):
        logger.console(self.access_key)
        s3 = self.r_session
        if s3 == None:
            s3 = self.get_resource()
        bucket = s3.Bucket(bucket_name)
        res = bucket in s3.buckets.all()
        if res == False:
            raise KeywordError("Bucket {} does not exist".format(bname))
        
    def get_object(self, bucket_name, obj):
        client = self.get_client()
        if self.client == None:
            client = self.get_client()
        resp = client.get_object(Bucket=bucket_name, Key=obj) 
        self._builtin.log("Returned Object: %s" % resp['Body'].read()) 

    def read_s3_object(self, bucket_name, key):
        if self.client() is None:
            s3 = get_client()
        s3 = self.client()
        response = s3.get_object(Bucket=bucket_name, Key=key)
        if response:
            return response['Body']

    def key_should_not_exist(self, bucket, key):
        client = self.get_client()
        try:
            res = client.head_object(Bucket=bucket, Key=key)
            if res['ResponseMetadata']['HTTPStatusCode'] == 200:
                raise KeywordError("Key: {}, already exists".format(key))
        except ClientError as e:
            self._builtin.log(e.response['Error']) 
            logger.console(e.response['Error'])
        return True

    def key_should_exist(self, bucket, key):
        client = self.client
        res = client.head_object(Bucket=bucket, Key=key)
        try:
            if res['ResponseMetadata']['HTTPStatusCode'] == 404:
                raise KeywordError("Key: {}, does not exist".format(key))
        except ClientError as e:
            self._builtin.log(e.response['Error']) 
            logger.console(e.response['Error'])
        return True

    def upload_file(self, bucket, path, key):
        client = self.get_client()
        try:
            file = client.upload_file(path, bucket, key)
        except ClientError as e:
            self._builtin.log(e.response['Error']) 
            logger.console(e.response['Error'])
        return True

    def download_file(self, bucket, path, key):
        client = self.get_client()
        try:
            file = client.download_file(bucket, key, path)
            self._builtin.log(file) 
        except ClientError as e:
            if e.response['Error']['Code'] == 404:
                self._builtin.log(e.response['Error']) 
                raise KeywordError("The bucket does not exist")
            else:
                raise

    def allowed_methods(self, bucket, methods=[]):
        client = self.get_client()
        try:
            response = client.get_bucket_cors(Bucket=bucket)
            obj = response['CORSRules'][0]
            aws_methods = obj['AllowedMethods']
            assert set(aws_methods) == set(methods)
        except ClientError as e:
            raise KeywordError("Error: " + e)


