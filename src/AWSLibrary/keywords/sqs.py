import botocore
from AWSLibrary.librarycomponent import LibraryComponent
from robot.api import logger
from robot.api.deco import keyword
from mypy_boto3_sqs import SQSClient


class SQSKeywords(LibraryComponent):
    
    def __init__(self, library):
        LibraryComponent.__init__(self, library)
        self.endpoint_url = None
    
    @keyword('SQS Set Endpoint Url')
    def sqs_set_endpoint(self, url):
        """ The complete URL to use for the constructed S3 client. Normally, botocore will automatically construct the
        appropriate URL to use when communicating with a service. You can specify a complete URL
        (including the “http/https” scheme) to override this behavior.

        | =Arguments= | =Description= |
        | ``url`` | <str> The complete endpoint URL. |

        *Examples:*
        | SQS Set Endpoint Url | http://localhost:4566/ |
        """
        self.endpoint_url = url
    
    @keyword('Send Message To SQS')
    def send_message_to_sqs(self, queue_name: str, message_body: str, message_attributes=None):
        """ Send a Message to Queue

        | =Arguments= | =Description= |
        | ``queue_name`` | <str> The queue name. |
        | ``message_body`` | <str> message to send. |
        | ``message_attributes`` | <Optional> Metadata to send. |

        *Example 1:*
        | Send Message To SQS | queue_name | Hello World! |
        
        *Example 2:*
        | ${example_type} | Create Dictionary | StringValue | 123 | DataType | String |
        | ${message_attributes} | Create Dictionary | Example | ${order_type} |
        | Send Message To SQS | sqs_name | Hello World! | ${message_attributes} |
        """
        sqs = self._get_sqs_client()
        queue_url = self._get_queue_url(queue_name)
        if message_attributes is None:
            message_attributes = {}

        try:
            response = sqs.send_message(
                QueueUrl=queue_url,
                MessageBody=message_body,
                MessageAttributes=message_attributes
            )
            logger.info(f"Message sent. Message Details: {response}")
        except botocore.exceptions.ClientError as e:
            raise Exception(e)
        
    @keyword('Receive Messages From SQS')
    def receive_messages_from_sqs(self, queue_name: str, max_number: int = 10, wait_time: int = 10) -> list:
        """ Recieve Messages From Queue

        | =Arguments= | =Description= |
        | ``queue_name`` | <str> The queue name. |
        | ``max_number`` | <Optional int> Max number of messages to receive. |
        | ``wait_time`` | <Optional int> Wait untill to get the messages. |

        *Example:*
        | ${messages_list} | Receive Messages From SQS | queue_name |
        | Log List | ${messages_list} |
        """
        sqs = self._get_sqs_client()
        queue_url = self._get_queue_url(queue_name)
        try:
            response = sqs.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=max_number,
                WaitTimeSeconds=wait_time,
                MessageAttributeNames=['All']
            )
            messages = response.get('Messages', [])
            logger.info(f"Received {len(messages)} message(s).")
            return messages
        except botocore.exceptions.ClientError as e:
            raise Exception(e)
        
    @keyword('Delete All Messages In SQS')
    def purge_sqs(self, queue_name: str):
        """
        Delete All Messages In SQS
        
        | =Arguments= | =Description= |
        | ``queue_name`` | <str> The queue name. |

        *Example:*
        | Delete All Messages In SQS | queue_name |
        """
        sqs = self._get_sqs_client()
        queue_url = self._get_queue_url(queue_name)
        try:
            # Purge the queue (delete all messages)
            sqs.purge_queue(QueueUrl=queue_url)
            logger.info(f"Queue '{queue_name}' has been purged successfully.")
        except botocore.exceptions.ClientError as e:
            raise Exception(f"An error occurred while purging the queue: {e}")
        
    def _get_sqs_client(self) -> SQSClient:
        """Retrieve the SQS client."""
        return self.library.session.client('sqs', endpoint_url=self.endpoint_url)

    def _get_queue_url(self, queue_name: str) -> str:
        """Retrieve the queue URL for the given queue name."""
        try:
            sqs = self._get_sqs_client()
            return sqs.get_queue_url(QueueName=queue_name)['QueueUrl']
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'AWS.SimpleQueueService.NonExistentQueue':
                raise Exception(f"Queue name '{queue_name}' not found.")
            else:
                raise Exception(f"An error occurred while getting the queue URL: {e}")
