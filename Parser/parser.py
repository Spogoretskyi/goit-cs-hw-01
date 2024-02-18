from Lexer.lexer import Lexer, Lexical_error
from Token.token import Token, Token_type, Parsing_error
from AST.ast import AST, Bin_op, Num


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise ParsingError("Помилка синтаксичного аналізу")

    def eat(self, token_type):
        """
        Порівнюємо поточний токен з очікуваним токеном і, якщо вони збігаються,
        'поглинаємо' його і переходимо до наступного токена.
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def term(self):
        """Парсер для 'term' правил граматики. У нашому випадку - це цілі числа."""
        node = self.factor()

        while self.current_token.type in (Token_type.MUL, Token_type.DIV):
            token = self.current_token
            if token.type == Token_type.MUL or token.type == Token_type.DIV:
                self.eat(token.type)

            node = Bin_op(left=node, op=token, right=self.factor())
        return node

    def factor(self):
        """Парсер для 'factor' правил граматики."""
        token = self.current_token
        if token.type == Token_type.INTEGER:
            self.eat(Token_type.INTEGER)
            return Num(token)
        elif token.type == Token_type.LPAREN:
            self.eat(Token_type.LPAREN)
            node = self.expr()
            self.eat(Token_type.RPAREN)
            return node

    def expr(self):
        """Парсер для арифметичних виразів."""
        node = self.term()

        while self.current_token.type in (
            Token_type.PLUS,
            Token_type.MINUS,
            Token_type.MUL,
            Token_type.DIV,
        ):
            token = self.current_token
            if token.type == Token_type.PLUS:
                self.eat(Token_type.PLUS)
            elif token.type == Token_type.MINUS:
                self.eat(Token_type.MINUS)
            elif token.type == Token_type.MUL:
                self.eat(Token_type.MUL)
            elif token.type == Token_type.DIV:
                self.eat(Token_type.DIV)

            node = Bin_op(left=node, op=token, right=self.term())

        return node


class Parsing_error(Exception):
    pass
