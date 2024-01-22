import re
import parser
TOKEN_TYPES = [
    "IDENTIFIER", "NUMBER", "STRING", "OPERATOR", "KEYWORD", "WHITESPACE", "EOF"
]

KEYWORDS = ["if", "else", "while", "def", "return"]

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"Token({self.token_type}, {self.value})"

class Tokenizer:
    def __init__(self, input_str):
        self.input_str = input_str
        self.position = 0
        self.current_char = self.input_str[self.position]

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha():
                return self.make_identifier_or_keyword()

            if self.current_char.isdigit():
                return self.make_number()

            if self.current_char in ["+", "-", "*", "/"]:
                return self.make_operator()

            if self.current_char in ["\"", "\'"]:
                return self.make_string()

            self.position += 1
            self.current_char = self.input_str[self.position]

        return Token("EOF", None)

    def make_identifier_or_keyword(self):
        value = ""
        while self.current_char is not None and self.current_char.isalnum():
            value += self.current_char
            self.position += 1
            self.current_char = self.input_str[self.position]

        if value in KEYWORDS:
            return Token("KEYWORD", value)
        else:
            return Token("IDENTIFIER", value)

    def make_number(self):
        value = ""
        while self.current_char is not None and self.current_char.isdigit():
            value += self.current_char
            self.position += 1
            self.current_char = self.input_str[self.position]

        return Token("NUMBER", int(value))

    def make_operator(self):
        value = self.current_char
        self.position += 1
        self.current_char = self.input_str[self.position]

        return Token("OPERATOR", value)

    def make_string(self):
        value = ""
        quote_char = self.current_char
        self.position += 1
        self.current_char = self.input_str[self.position]

        while self.current_char is not None and self.current_char != quote_char:
            value += self.current_char
            self.position += 1
            self.current_char = self.input_str[self.position]

        self.position += 1
        self.current_char = self.input_str[self.position]

        return Token("STRING", value)

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.position += 1
            self.current_char = self.input_str[self.position]
