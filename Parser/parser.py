from Lexer.lexer import Lexer
from Token.toke import TokenType
from Token.parsing_error import Parsing_error
from Token.lexical_error import Lexical_error
from AST.ast import AST
from AST.bin_op import BinOp


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

        while self.current_token.type in (TokenType.MUL,):
            token = self.current_token
            if token.type == TokenType.MUL:
                self.eat(TokenType.MUL)

            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def factor(self):
        """Парсер для 'factor' правил граматики."""
        token = self.current_token
        if token.type == TokenType.INTEGER:
            self.eat(TokenType.INTEGER)
            return Num(token)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node

    def expr(self):
        """Парсер для арифметичних виразів."""
        node = self.term()

        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node
