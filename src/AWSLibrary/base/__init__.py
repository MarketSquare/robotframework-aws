from .librarycomponent import LibraryComponent
import logging

FORMAT = "%(asctime)s|%(levelname)s|%(pathname)s:%(funcName)s:%(lineno)-2s|%(message)s"

logger = logging.getLogger('root')
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
sh.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(sh)


__all__ = [
    LibraryComponent,
]
