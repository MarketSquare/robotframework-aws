import logging


class FatalError(RuntimeError):

    def __init__(self, message):
        ROBOT_EXIT_ON_FAILURE = True
        self.logger     = logging.getLogger(__name__)
        self.logger.critical(f'Error: {RuntimeError}')

class KeywordError(RuntimeError):

    def __init__(self, message):
        ROBOT_SUPPRESS_NAME = True
        self.logger     = logging.getLogger(__name__)
        self.logger.critical(f'Error: {RuntimeError}')

class ContinuableError(RuntimeError):
    
    def __init__(self, message):
        ROBOT_CONTINUE_ON_FAILURE = True
        self.logger     = logging.getLogger(__name__)
        self.logger.critical(f'Error: {RuntimeError}')