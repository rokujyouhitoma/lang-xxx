from rply import ParserGenerator
from token import BoxInt

pg = ParserGenerator(["NUMBER", "PLUS", "MINUS"],
                     precedence=[("left", ['PLUS', 'MINUS'])],
                     cache_id="myparser")

@pg.production("main : expr")
def main(p):
    return p[0]

@pg.production("expr : expr PLUS expr")
@pg.production("expr : expr MINUS expr")
def expr_op(p):
    lhs = p[0].eval()
    rhs = p[2].eval()
    if p[1].gettokentype() == "PLUS":
        return BoxInt(lhs + rhs)
    elif p[1].gettokentype() == "MINUS":
        return BoxInt(lhs - rhs)
    else:
        raise AssertionError("This is impossible, abort the time machine!")

@pg.production("expr : NUMBER")
def expr_num(p):
    return BoxInt(int(p[0].getstr()))

parser = pg.build()
