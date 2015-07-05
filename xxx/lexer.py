from rply import LexerGenerator

lg = LexerGenerator()

lg.add("PLUS", r"\+")
lg.add("MINUS", r"-")
lg.add("NUMBER", r"\d+")

lg.ignore(r"\s+")

lexer = lg.build()
