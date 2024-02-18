class AST:
    pass


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Bin_op(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
