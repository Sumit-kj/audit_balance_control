from enum import Enum

class LogEvent(Enum):
    EXTRACT = 'EXTRACT'
    LOAD = 'LOAD'
    TRANSFORM = 'TRANSFORM'
