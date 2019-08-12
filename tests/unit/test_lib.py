from AWSLibrary.base import LibraryComponent, keyword
from robot.api import logger


class library(LibraryComponent):

    @keyword
    def foo(self):
        self.info('foo')

    @keyword
    def bar(self, arg):
        self.info(arg)