from enum import Enum, auto


class Error(Enum):
    NO_IP_AVAILABLE = auto()
    UNEXPECTED_ERROR = auto()
    FAILED_TO_ADD_PEER = auto()
