import boto3
import os
import sys


class S3Reader(object):

    def __init__(self, Bucket="", Key=""):
        self.client = boto3.client("s3")
        self.BucketName = bucket
        self.Key = key
        self.response = self.client.list_objects(Bucket=self.BucketName)

    @property
    def get_object(self):

        return [x.get("Key", None) for x in self.response.get("Contents", None)]

