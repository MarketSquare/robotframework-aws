


class LibraryComponent(object):

    def __init__(self, state):
        self.state = state
        
    def info(self, msg, html=False):
        logger.info(msg, html)

    def debug(self, msg, html=False):
        logger.debug(msg, html)