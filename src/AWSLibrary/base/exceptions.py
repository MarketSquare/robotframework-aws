import logging
from robot.api import logger


class FatalError(RuntimeError):
    def __init__(self, message):
        ROBOT_EXIT_ON_FAILURE = True
        self.logger = logging.getLogger(__name__)
        self.rb_logger = logger
        logger.error(f'Error: {RuntimeError}')
        self.logger.critical(f'Error: {RuntimeError} | Message: {message}')
        self.rb_logger.error(f'Error: {RuntimeError} | Message: {message}')
        

class KeywordError(RuntimeError):
    def __init__(self, message):
        ROBOT_SUPPRESS_NAME = True
        self.logger = logging.getLogger(__name__)
        self.rb_logger = logger
        logger.error(f'Error: {RuntimeError}')
        self.logger.critical(f'Error: {RuntimeError} | Message: {message}')
        self.rb_logger.error(f'Error: {RuntimeError} | Message: {message}')


class ContinuableError(RuntimeError):
    def __init__(self, message):
        ROBOT_CONTINUE_ON_FAILURE = True
        self.logger     = logging.getLogger(__name__)
        self.rb_logger  = logger
        logger.error(f'Error: {RuntimeError}')
        self.logger.critical(f'Error: {RuntimeError} | Message: {message}')
        self.rb_logger.error(f'Error: {RuntimeError} | Message: {message}')