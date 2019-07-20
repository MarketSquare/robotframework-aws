from robot.api import logger


class FatalError(RuntimeError):
    ROBOT_EXIT_ON_FAILURE = True

class KeywordError(RuntimeError):
    ROBOT_SUPPRESS_NAME = True


class S3Manager(object):

    def __init__(self, access_key, secret_key):
        self.bucket = None

    def list_buckets(self):
        client = self.get_client()
        if self.get_client == None:
            return "First set client"
        return client.list_buckets()

    def get_bucket(self, bname):
        logger.console(self.access_key)
        s3 = self.r_session
        if s3 == None:
            s3 = self.get_resource()
        bucket = s3.Bucket(bname)
        res = bucket in s3.buckets.all()
        if res == False:
            raise KeywordError("Bucket {} does not exist".format(bname))
        # return self.bucket

    def get_object(self, bucket_name, obj):
        client = self.get_client()
        if self.client == None:
            client = self.get_client()
        resp = client.get_object(Bucket=bucket_name, Key=obj) 
        self._builtin.log("Returned Object: %s" % resp['Body'].read()) 

    def upload_file(self):
        client = self.get_client()
        if s3 == None:
            s3 = self.get_resource()

        resp = client.put_object(Bucket=bucket_name,
                                    Key=obj,
                                    Body=request.files['myfile'],
                                    ServerSideEncryption='aws:kms',
                                    )
        s3 = self.r_session


