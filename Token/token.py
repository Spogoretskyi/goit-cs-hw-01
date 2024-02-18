class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)})"


class Parsing_error(Exception):
    pass


class Token_type:
    INTEGER = "INTEGER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    MUL = "MUL"
    DIV = "DIV"
    EOF = "EOF"  # Означає кінець вхідного рядка
