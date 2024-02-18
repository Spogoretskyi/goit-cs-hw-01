from Token.token import Token, Token_type, Parsing_error


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        """Переміщуємо 'вказівник' на наступний символ вхідного рядка"""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Означає кінець введення
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        """Пропускаємо пробільні символи."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Повертаємо ціле число, зібране з послідовності цифр."""
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """Лексичний аналізатор, що розбиває вхідний рядок на токени."""
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(Token_type.INTEGER, self.integer())

            if self.current_char == "+":
                self.advance()
                return Token(Token_type.PLUS, "+")

            if self.current_char == "-":
                self.advance()
                return Token(Token_type.MINUS, "-")

            if self.current_char == "*":
                self.advance()
                return Token(Token_type.MUL, "*")

            if self.current_char == "/":
                self.advance()
                return Token(Token_type.DIV, "/")

            if self.current_char == "(":
                self.advance()
                return Token(Token_type.LPAREN, "(")

            if self.current_char == ")":
                self.advance()
                return Token(Token_type.RPAREN, ")")

            raise Lexical_error("Помилка лексичного аналізу")

        return Token(Token_type.EOF, None)


class Lexical_error(Exception):
    pass
