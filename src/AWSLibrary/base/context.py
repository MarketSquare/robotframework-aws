


class ContextManager(object):

    def __init__(self, state):
        self.state = state

    @property
    def session(self):
        return self.state.session

    @session.setter
    def session(self, value):
        self.state.session = value