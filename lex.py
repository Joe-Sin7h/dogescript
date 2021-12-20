from sly import Lexer

class DogeLexer(Lexer):
    
    # tokens
    tokens = { 
               
        ID, NUMBER, PLUS, MINUS, TIMES,
        DIVIDE, ASSIGN, LPAREN, RPAREN 
    }
    
    ignore = ' \t'

 
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    ASSIGN  = r'='
    LPAREN  = r'\('
    RPAREN  = r'\)'

    def NUMBER(self, token):
        token.value = int(token.value)

        return token


if "__main__" == __name__:
    lexer = DogeLexer()
    data = "a = 1+2"
    for tokens in lexer.tokenize(data):
        print(tokens)
    
    
        