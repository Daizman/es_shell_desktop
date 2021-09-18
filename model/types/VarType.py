from enum import Enum


class VarType(Enum):
    INFERRED = 1
    REQUESTED = 2
    OUTPUT_REQUESTED = 3
