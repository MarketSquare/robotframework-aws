from robot.libraries.BuiltIn import BuiltIn
import logging


class LibraryComponent(object):

    def __init__(self, state):
        self.state          = state
        self.logger         = logging.getLogger(__name__)
        self._builtin       = BuiltIn()

    def info(self, msg, html=False):
        self.logger.info(msg, html)

    def debug(self, msg, html=False):
        self.logger.debug(msg, html)