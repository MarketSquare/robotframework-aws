import boto3
import time


endpoint = "http://localhost:4566"
LOG_GROUP = 'test'
LOG_STREAM = 'test'


def send_cloudwatch_message(message):
    session = boto3.Session(
                aws_access_key_id="dummy",
                aws_secret_access_key="dummy",
                region_name="us-east-1"
            )
    logs = session.client('logs', endpoint_url=endpoint)
    timestamp = int(round(time.time() * 1000))
    logs.put_log_events(
        logGroupName=LOG_GROUP,
        logStreamName=LOG_STREAM,
        logEvents=[
            {
                'timestamp': timestamp,
                'message': time.strftime('%Y-%m-%d %H:%M:%S')+' %s' % message
            }
        ]
    )
