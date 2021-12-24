from sly import Lexer, Parser

class DogeLexer(Lexer):
    
    # tokens
    tokens = { 
               
        ID, NUMBER, PLUS, MINUS, TIMES,
        DIVIDE, ASSIGN, LPAREN, RPAREN,
        # STRING, NAME

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
    # STRING  = r'\".*?\"'
    # NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

    def NUMBER(self, token):
        token.value = int(token.value)
        return token

   

class DogeParser(Parser):
    tokens = DogeLexer.tokens

    #Rules and grammar
    # @_('')
    # def statement(self, p):
    #     pass

    # @_('var_assign')
    # def statement(self, p):
    #     return p.var_assign

    # @_('NAME "=" expr')
    # def var_assign(self, p):
    #     return ('var_assign', p.NAME, p.expr)

    # @_('NAME "=" STRING')
    # def var_assign(self,  p):
    #     return ('var_assign', p.NAME, p.expr)
        
    @_('expr PLUS term')
    def expr(self, p):
        return p.expr + p.term

    @_('expr MINUS term')
    def expr(self, p):
        return p.expr - p.term

    @_('term')
    def expr(self, p):
        return p.term

    @_('term TIMES factor')
    def term(self, p):
        return p.term * p.factor

    @_('term DIVIDE factor')
    def term(self, p):
        return p.term/p.factor

    @_('factor')
    def term(self, p):
        return p.factor

    @_('NUMBER')
    def factor(self, p):
        return p.NUMBER

    # @_('NAME')
    # def expr(self, p):
    #     return ('var', p.NAME)

    @_('LPAREN expr RPAREN')
    def factor(self, p):
        return p.expr

    


if "__main__" == __name__:
    # lexer = DogeLexer()
    # data = "a = 1+2"
    # for tokens in lexer.tokenize(data):
    #     print(tokens)

    lexer = DogeLexer()
    parser = DogeParser()

    while True:
        try:
            text = input('dogescript>> ')
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break
    