from rply import ParserGenerator
from token import Number
from operator import Add, Sub, Mul, Div


pg = ParserGenerator(['NUMBER', 'PLUS', 'MINUS', 'MUL', 'DIV'],
                     precedence=[('left', ['PLUS', 'MINUS']),
                                 ('left', ['MUL', 'DIV'])],
                     cache_id='xxxparser')

@pg.production('main : expr')
def main(p):
    return p[0]

@pg.production('expr : expr PLUS expr')
@pg.production('expr : expr MINUS expr')
@pg.production('expr : expr MUL expr')
@pg.production('expr : expr DIV expr')
def expr_op(p):
    left = p[0]
    op = p[1]
    right = p[2]
    if op.gettokentype() == 'PLUS':
        return Add(left, right)
    elif op.gettokentype() == 'MINUS':
        return Sub(left, right)
    elif op.gettokentype() == 'MUL':
        return Mul(left, right)
    elif op.gettokentype() == 'DIV':
        return Div(left, right)
    else:
        raise AssertionError('Not supported.')

@pg.production('expr : NUMBER')
def expr_num(p):
    return Number(int(p[0].getstr()))

@pg.error
def error_handler(token):
    raise ValueError("Ran into a %s where it was't expected Error." % token.gettokentype())

parser = pg.build()
