


class LibraryComponent(object):

    def __init__(self, state):
        self.state = state
        
    @property
    def aws_session(self):
        return self.state.session

    @aws_session.setter
    def aws_session(self, value):
        self.state.session = value