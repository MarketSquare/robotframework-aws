from AWSLibrary.keywords.session import SessionManager
import logging

library_logging = logging.getLogger('SessionManager')
library_logging.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
sh.setFormatter("%(asctime)s|%(levelname)s|%(pathname)s:%(funcName)s:%(lineno)-2s|%(message)s")
library_logging.addHandler(sh)


__all__ = [
    'SessionManager',
]

