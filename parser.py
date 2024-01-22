
class Parser:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.current_token = self.tokenizer.get_next_token()

    def eat(self, token_type):
        if self.current_token.token_type == token_type:
            self.current_token = self.tokenizer.get_next_token()
        else:
            raise ValueError(f"Unexpected token type: {self.current_token.token_type}")

    def peek(self):
        if self.current_token < len(self.tokenizer):
            return self.current_token[self.current_token]
        else:
            return None
    def parse(self):
        self.expression()
        if self.peek().type != "EOF":
            raise Exception("Error: expected end of input but got " + self.peek().type)

    def expression(self):
        self.term()
        while self.peek().type in ["PLUS", "MINUS"]:
            token = self.peek()
            if token.type == "PLUS":
                self.eat(token.type)
                self.term()
                self.plus()
            elif token.type == "MINUS":
                self.eat(token.type)
                self.term()
                self.minus()

    def term(self):
        self.factor()
        while self.peek().type in ["MUL", "DIV"]:
            token = self.peek()
            if token.type == "MUL":
                self.eat(token.type)
                self.factor()
                self.multiply()
            elif token.type == "DIV":
                self.eat(token.type)