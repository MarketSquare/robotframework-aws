# from AWSLibrary.keywords.s3 import S3Manager
# from AWSLibrary.keywords.session import SessionManager
from robot.utils import ConnectionCache
import os
from AWSLibrary import AWSLibrary

a = os.environ["ACCESS_KEY"]
b = os.environ["SECRET_KEY"]


def main():
    lib = AWSLibrary()
    session = lib.create_session_with_keys('us-east-1', a, b)
    lib._cache.register(session, alias=session.region_name)
    lib._cache.switch(session.region_name)

if __name__ == "__main__":
    main()


