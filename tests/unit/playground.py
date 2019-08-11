from robot.utils import ConnectionCache
import os
from AWSLibrary import AWSLibrary
import boto3

from os import getenv
a = getenv('ACCESS_KEY')
b = getenv('SECRET_KEY')

def main():
    lib = AWSLibrary()
    lib.download_file_from_s3("zappastaticbin", "test.html", "static/downloaded_test.html")


if __name__ == "__main__":
    main()


