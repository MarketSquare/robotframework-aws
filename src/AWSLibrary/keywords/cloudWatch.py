from AWSLibrary.librarycomponent import LibraryComponent
from robot.api.deco import keyword
from robot.api import logger
from datetime import datetime, timedelta
import time


class CloudWatchKeywords(LibraryComponent):

    def __init__(self, library):
        LibraryComponent.__init__(self, library)
        self.endpoint_url = None

    @keyword('CloudWatch Logs Insights')
    def insights_query(self, log_group, query, minutes_behind=60):
        """TODO
        """
        client = self.library.session.client('logs', endpoint_url=self.endpoint_url)
        time_behind = (datetime.now() - timedelta(minutes=minutes_behind)).timestamp()
        start_query_response = client.start_query(logGroupName=log_group,
                                                  startTime=int(time_behind),
                                                  endTime=int(datetime.now().timestamp()),
                                                  queryString=query,
                                                  limit=1)
        query_id = start_query_response['queryId']
        response = None
        logs = []
        while response is None or response['status'] == 'Running':
            time.sleep(1)
            logger.warn("dormiu")
            response = client.get_query_results(queryId=query_id)
            logs.append(response['results'])
        return logs
