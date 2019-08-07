# from AWSLibrary.keywords.s3 import S3Manager
# from AWSLibrary.keywords.session import SessionManager
from robot.utils import ConnectionCache
import os
from AWSLibrary import AWSLibrary
import configparser
import boto3


a = os.environ.get("AWS_ACCESS_KEY_ID")
b = os.environ.get("AWS_SECRET_ACCESS_KEY")


def main():
    lib = AWSLibrary()
    session = lib.create_session_with_keys('us-east-1')
    print(session, "--")
   

if __name__ == "__main__":
    main()


