from enum import Enum, auto


class Error(Enum):
    NO_IP_AVAILABLE = auto()
    UNEXPECTED_ERROR = auto()
