# STANDARD IMPORTS
from enum import IntEnum


class InternalCode(IntEnum):
    SUCCESS = 200
    VALUE_ERROR = 10
    DATA_NOT_FOUND = 99
    INTERNAL_SERVER_ERROR = 500
    DATA_NOT_INSERTED_ON_DATABASE = 89
    PLAYWRIGHT_ERROR = 79

    def __repr__(self):
        return self.value
    