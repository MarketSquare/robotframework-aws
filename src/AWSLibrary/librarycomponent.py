class LibraryComponent(object):
    """
    This is the base class to be inherited by the keyword classes under AWSLibrary/keywords.
    It is a helper class that makes attributes from the AWSLibrary class available to the keyword classes.
    """

    def __init__(self, library):
        """
        :param library: The robotframework-aws library itself.
        """
        self.library = library
