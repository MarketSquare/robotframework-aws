


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
        
        resp = client.get_object(Bucket=bucket_name, Key=obj)  
        print(resp['Body'].read())
        return resp


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


