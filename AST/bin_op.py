from ast import AST


class Bin_op(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
