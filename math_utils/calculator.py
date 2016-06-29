from math_utils.operations import operations_map


class Calculator(object):

    def __init__(self):
        self.value = 0

    def set(self, value):
        self.value = value

    def operate(self, op_type, x):
        self.value = operations_map[op_type](self.value, x)
