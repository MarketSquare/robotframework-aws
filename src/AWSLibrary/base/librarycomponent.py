from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
import logging


class LibraryComponent(object):

    def __init__(self, state):
        self.state          = state
        self.dev_logger     = logging.getLogger(__name__)
        self.rb_logger      = logger
        self._builtin       = BuiltIn()