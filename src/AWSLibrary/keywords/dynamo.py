from AWSLibrary.librarycomponent import LibraryComponent
from boto3.dynamodb.types import TypeDeserializer
from robot.api.deco import keyword
from robot.api import logger


class DynamoKeywords(LibraryComponent):

    def __init__(self, library):
        LibraryComponent.__init__(self, library)
        self.endpoint_url = None

    @keyword('Dynamo Set Endpoint Url')
    def dynamo_set_endpoint(self, url):
        """ The complete URL to use for the constructed Dynamo client. Normally, botocore will automatically construct
        the appropriate URL to use when communicating with a service. You can specify a complete URL
        (including the “http/https” scheme) to override this behavior.

        | =Arguments= | =Description= |
        | ``url`` | <str> The complete endpoint URL. |

        *Examples:*
        | Dynamo Set Endpoint Url | http://localhost:4566/ |
        """
        self.endpoint_url = url

    @keyword('Dynamo Query Table')
    def dynamo_query_table(self, table_name, partition_key, partition_value, sort_key=None, sort_value=None,
                           projection=None):
        """Queries a DynamoDB table based on the partition_key and his value. returns all the information found in a
        list of dictionaries.

        The result deserializes DynamoDB types to Python types:
        https://boto3.amazonaws.com/v1/documentation/api/latest/_modules/boto3/dynamodb/types.html

        | =Arguments= | =Description= |
        | ``table_name`` | <str> Name of the DynamoDB table. |
        | ``partition_key`` | <str> The key to search. |
        | ``partition_value`` | <str> Value of the partition key. |
        | ``sort_key`` | <str> (optional) The sort key to search. |
        | ``sort_value`` | <str> (optional) Value of the sort key. |
        | ``projection`` | <str> (optional) A string specifying the attributes to retrieve. |

        *Examples:*
        | Dynamo Query Table | library-books | book_id | 123 |
        | Dynamo Query Table | library-books | book_id | 123 | sort_key=book_code | sort_value=abc001 |
        | Dynamo Query Table | library-books | book_id | 123 | projection=value |
        """
        client = self.library.session.client('dynamodb', endpoint_url=self.endpoint_url)
        if sort_key is None:
            expression = {':value': {'S': partition_value}}
            condition = f'{partition_key} = :value'
        else:
            expression = {':partition_value': {'S': partition_value}, ':sort_value': {'S': sort_value}}
            condition = f'{partition_key} = :partition_value AND {sort_key} = :sort_value'
        query_params = {
            'ExpressionAttributeValues': expression,
            'KeyConditionExpression': condition,
            'TableName': table_name
        }
        if projection is not None:
            query_params['ProjectionExpression'] = projection
        logger.debug(projection)
        response = client.query(**query_params)
        logger.info(f"Found {response['Count']} items")
        # Deserializes DynamoDB types to Python types.
        if response['Items']:
            deserializer = TypeDeserializer()
            count = len(response['Items'])
            for index in range(count):
                dict_response = {k: deserializer.deserialize(v) for k, v in response['Items'][index].items()}
                response['Items'][index].update(dict_response)
        return response['Items']

    @keyword('Dynamo Put Item')
    def dynamo_update_item(self, table_name, json_dict):
        """Creates a new item, or replaces an old item with a new item. If an item that has the same partition key
        (primary key) as the new item already exists in the specified table, the new item completely replaces the
        existing item.

        | =Arguments= | =Description= |
        | ``table_name`` | <str> Name of the DynamoDB table. |
        | ``table_name`` | <dict> JSON dictionary representing the dynamo item. |

        *Examples:*
        | Dynamo Put Item | library-books | {"key": "value"} |
        """
        resource = self.library.session.resource('dynamodb', endpoint_url=self.endpoint_url)
        response = resource.Table(table_name).put_item(Item=json_dict)
        logger.info(response)

    @keyword('Dynamo Delete Item')
    def dynamo_delete_item(self, table_name, partition_key, partition_value, sort_key=None, sort_value=None):
        """Deletes a single item in a table by partition key (primary key) and sort key if provided.

        | =Arguments= | =Description= |
        | ``table_name`` | <str> Name of the DynamoDB table. |
        | ``partition_key`` | <str> The key to search. |
        | ``partition_value`` | <str> Value of the partition key. |
        | ``sort_key`` | <str> (optional) The sort key to search. |
        | ``sort_value`` | <str> (optional) Value of the sort key. |

        *Examples:*
        | Dynamo Delete Item | library-books | book_id | 123 |
        | Dynamo Delete Item | library-books | book_id | 123 | book_code | abc001 |
        """
        resource = self.library.session.resource('dynamodb', endpoint_url=self.endpoint_url)
        key = {partition_key: partition_value, sort_key: sort_value} if sort_key else {partition_key: partition_value}
        response = resource.Table(table_name).delete_item(Key=key)
        logger.info(response)

    @keyword('Dynamo Remove Key')
    def dynamo_remove_key(self, table_name, partition_key, partition_value, attribute_name,
                          sort_key=None, sort_value=None):
        """Removes a specific key in a DynamoDB item based on partition_key and sort key, if provided.

        | =Arguments= | =Description= |
        | ``table_name`` | <str> Name of the DynamoDB table. |
        | ``partition_key`` | <str> The key to search. |
        | ``partition_value`` | <str> Value of the partition key. |
        | ``attribute_name`` | <str> Key to remove, for nested keys use . to compose the path. |
        | ``sort_key`` | <str> (optional) The sort key to search. |
        | ``sort_value`` | <str> (optional) Value of the sort key. |

        *Examples:*
        | Dynamo Remove Key | library-books | book_id | 123 | quantity |
        | Dynamo Remove Key | library-books | book_id | 123 | book.value |
        | Dynamo Remove Key | library-books | book_id | 123 | quantity | sort_key=book_code | sort_value=abc001 |
        """
        resource = self.library.session.resource('dynamodb', endpoint_url=self.endpoint_url)
        expression, names = self._compose_expression(attribute_name, remove=True)
        logger.debug(f"UpdateExpression: {expression}")
        logger.debug(f"ExpressionAttributeNames: {names}")
        key = {partition_key: partition_value, sort_key: sort_value} if sort_key else {partition_key: partition_value}
        response = resource.Table(table_name).update_item(
            Key=key,
            UpdateExpression=expression,
            ExpressionAttributeNames=names
        )
        logger.info(response)

    @keyword('Dynamo Update Key')
    def dynamo_update_key(self, table_name, partition_key, partition_value, attribute_name, attribute_value,
                          sort_key=None, sort_value=None):
        """Update a specific key in a DynamoDB item based on partition_key and sort key, if provided.

        Arguments:
        - ``table_name``: name of the DynamoDB table.
        - ``partition_key``: the partition key to search.
        - ``value``: the value of partition key.
        - ``attribute_name``: the key to update. For nested keys, use . to compose the path
        - ``new_value``: the new value of the attribute_name.
        - ``sort_key``: the sort key to search. Default as None
        - ``sort_value``: the value of sort key. Default as None

        | =Arguments= | =Description= |
        | ``table_name`` | <str> Name of the DynamoDB table. |
        | ``partition_key`` | <str> The key to search. |
        | ``partition_value`` | <str> Value of the partition key. |
        | ``attribute_name`` | <str> Key to update. For nested keys, use . to compose the path. |
        | ``attribute_value`` | <str> The new value of the attribute_name. |
        | ``sort_key`` | <str> (optional) The sort key to search. |
        | ``sort_value`` | <str> (optional) Value of the sort key. |

        *Examples:*
        | Dynamo Update Key | library-books | book_id | 123 | quantity | 100 |
        | Dynamo Update Key | library-books | book_id | 123 | book.value | 15 |
        | Dynamo Update Key | library-books | book_id | 123 | quantity | 100 | sort_key=book_code | sort_value=abc001 |
        """
        resource = self.library.session.resource('dynamodb', endpoint_url=self.endpoint_url)
        expression, names = self._compose_expression(attribute_name)
        logger.debug(f"UpdateExpression: {expression}")
        logger.debug(f"ExpressionAttributeNames: {names}")
        key = {partition_key: partition_value, sort_key: sort_value} if sort_key else {partition_key: partition_value}
        result = resource.Table(table_name).update_item(
            Key=key,
            UpdateExpression=expression,
            ExpressionAttributeNames=names,
            ExpressionAttributeValues={':new_value': attribute_value}
        )
        return result

    @staticmethod
    def _compose_expression(attribute, remove=False):
        if "." not in attribute:
            expression = "SET #attr = :new_value" if not remove else "REMOVE #attr"
            names = {'#attr': attribute}
            return expression, names
        else:
            attr = ""
            names = {}
            keys = attribute.split(".")
            for index, key in enumerate(keys):
                attr = attr + ("#attr" + str(index) + ".")
                dict_key = "#attr" + str(index)
                dict_value = key
                names.update({dict_key: dict_value})
            expression = "SET " + attr[:-1] + " = :new_value" if not remove else "REMOVE " + attr[:-1]
            return expression, names
