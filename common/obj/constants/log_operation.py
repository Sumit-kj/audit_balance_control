from enum import Enum

class LogOperation(Enum):
    # Data Operation
    READ = 'ReadData'
    WRITE = 'WriteData'

    # Validation Error
    NULL_CHECK_FAIL = 'NullCheckFail'
    DUPLICATE_FOUND = 'DuplicateFound'
