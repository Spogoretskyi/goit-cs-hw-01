from Lexer.lexer import Lexer, Lexical_error
from Parser.parser import Parser, Parsing_error
from Token.token import Token, Token_type
from AST.ast import AST, Bin_op, Num


class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def visit_Bin_op(self, node):
        if node.op.type == Token_type.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == Token_type.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == Token_type.MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == Token_type.DIV:
            return self.visit(node.left) / self.visit(node.right)

    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.expr()
        return self.visit(tree)

    def visit(self, node):
        method_name = "visit_" + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f"Немає методу visit_{type(node).__name__}")
