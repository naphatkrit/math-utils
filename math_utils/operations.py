from enum import Enum

class OperationTypes(Enum):
    add = 1
    subtract = 2


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


operations_map = {
    OperationTypes.add: add,
    OperationTypes.subtract: subtract,
}
