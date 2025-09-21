from datetime import datetime

from common.obj.constants.log_level import LogLevel
from common.obj.constants.log_operation import LogOperation
from common.obj.constants.log_event import LogEvent
from common import constants as const

class Log:
    def __int__(self, level: LogLevel, operation: LogOperation, event: LogEvent) -> None:
        self.level = level
        self.operation = operation
        self.event = event

    def read_file_log(self):
        timestamp = datetime.now().isoformat()
        read_line = const.read_from_file
