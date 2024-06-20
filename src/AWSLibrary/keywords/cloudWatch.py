from AWSLibrary.librarycomponent import LibraryComponent
from robot.api.deco import keyword
from robot.api import logger
from datetime import datetime, timedelta
import time
import re


class CloudWatchKeywords(LibraryComponent):

    def __init__(self, library):
        LibraryComponent.__init__(self, library)
        self.endpoint_url = None

    @keyword('CloudWatch Logs Insights')
    def insights_query(self, log_group, query, start_time=60):
        """Executes a query on CloudWatch Insights and return the found results in a list.

        | =Arguments= | =Description= |
        | ``log_group`` | <str> Log group name. |
        | ``query`` | <str> Aws query log format. |
        | ``start_time`` | <str> The beginning of the time range to query from now to ago in minutes. |

        ---
        Use the same aws console ``query`` format in the argument, like this examples:

        - Filter only by a part of the message, return the timestamp and the message:
        | ``fields @timestamp, @message | filter @message like 'some string inside message to search' | sort @timestamp desc | limit 5``
        - Filter by json path and part of the message, return only the message:
        | ``fields @message | filter API.httpMethod = 'GET' and @message like 'Zp8beEeByQ0EDvg' | sort @timestamp desc | limit 20``
        - Find the 10 most expensive requests:
        | ``filter @type = "REPORT" | fields @requestId, @billedDuration | sort by @billedDuration desc | limit 10``

        For more information, see CloudWatch Logs Insights Query Syntax.
        https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html
        ---

        *Examples:*
        | ${logs} | CloudWatch Logs Insights | /aws/group-name | query |
        | ${logs} | CloudWatch Logs Insights | /aws/group-name | query | start_time=120 |
        """
        client = self.library.session.client('logs', endpoint_url=self.endpoint_url)
        time_behind = (datetime.now() - timedelta(minutes=start_time)).timestamp()
        query = client.start_query(logGroupName=log_group,
                                   startTime=int(time_behind),
                                   endTime=int(datetime.now().timestamp()),
                                   queryString=query)
        query_id = query['queryId']
        response = client.get_query_results(queryId=query_id)
        while response['status'] == 'Running':
            logger.debug("waiting for Logs Insights")
            time.sleep(0.5)
            response = client.get_query_results(queryId=query_id)
        return response['results']

    @keyword('CloudWatch Wait For Logs')
    def wait_for_logs(self, log_group, filter_pattern, regex_pattern, seconds_behind=60, timeout=30,
                      not_found_fail=False):
        """Wait until find the wanted log in cloudwatch.

        This keyword is used to wait in real time if the desired log appears inside the informed log group.
        It works in a similar way to the existing CloudWatch filter in "Live Tail".

        Return all the logs that match the informed regex in a list.

        | =Arguments= | =Description= |
        | ``log_group`` | <str> Log group name. |
        | ``filter_pattern`` | <str> Filter for CloudWatch. |
        | ``regex_pattern`` | <str> Regex pattern to search in filter results. |
        | ``seconds_behind`` | <str> How many seconds from now to ago, used to searching the logs. |
        | ``timeout`` | <str> Timeout in seconds to end the search. |
        | ``not_found_fail`` | <str> The beginning of the time range to query in minutes. |

        ---
        For ``filter_pattern`` use the same as aws console filter patterns in Live tail.
        https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html

        - Filter for json path in log:
        | {$.foo.bar = some_string_value}
        - Filter for json path with null value in log:
        | {$.foo.bar IS NULL}
        - Filter for INFO logs:
        | INFO
        - Filter for DEBUG logs:
        | DEBUG
        - Filter for anything in logs:
        | " "

        For ``regex_pattern`` use the same regular expressions that robot framework uses in BuildIn Library.
        ---

        Note: as boto3 takes some time to get the logs and apply the regex query to each one of them, depending on the
        amount of log found, the keyword execution time may be slightly longer than the timeout.

        *Examples:*
        | ${logs} | CloudWatch Wait For Logs | /aws/group_name | {$.foo.bar = id_value} | 2024.*filename |
        | ${logs} | CloudWatch Wait For Logs | /aws/group_name | INFO | \\\d+.*id_code | timeout=60 |
        | ${logs} | CloudWatch Wait For Logs | /aws/group_name | " " | \\\w+.*some_code | not_found_fail=${True} |
        """
        client = self.library.session.client('logs', endpoint_url=self.endpoint_url)
        stream_response = client.describe_log_streams(logGroupName=log_group,
                                                      orderBy='LastEventTime',
                                                      descending=True,
                                                      limit=1)
        latest_log_stream_name = stream_response["logStreams"][0]["logStreamName"]
        logger.info("The latest stream is: %s" % latest_log_stream_name)
        stream_response = client.describe_log_streams(logGroupName=log_group,
                                                      logStreamNamePrefix=latest_log_stream_name)
        logger.debug(stream_response)
        last_event = stream_response['logStreams'][0]['lastIngestionTime']
        logger.info("Last event: %s" % datetime.fromtimestamp(int(last_event) / 1000).strftime('%d-%m-%Y %H:%M:%S'))
        last_event_delay = last_event - seconds_behind * 1000
        logger.info("Starting the log search from: %s" % datetime.fromtimestamp(int(last_event_delay) / 1000)
                    .strftime('%d-%m-%Y %H:%M:%S'))
        events_match = []
        for i in range(int(timeout)):
            response = client.filter_log_events(logGroupName=log_group,
                                                startTime=last_event_delay,
                                                filterPattern=filter_pattern)
            logger.info("%s Total records found" % len(response["events"]))
            logger.debug(response["events"])
            for event in response["events"]:
                match_event = re.search(regex_pattern, event['message'])
                if match_event:
                    events_match.append(event['message'])
            if len(events_match) > 0:
                break
            else:
                time.sleep(1)
        if not_found_fail and len(events_match) == 0:
            raise Exception(f"Log not found in CloudWatch inside {log_group} for {filter_pattern} and {regex_pattern}")
        return events_match
