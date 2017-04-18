from TCS_2017.ParsingRegularExpressions.parse import Lexer, Parser, Handler


def reg_exp_parse(reg_exp):

    lexer = Lexer(reg_exp)
    parser = Parser(lexer)
    elements = parser.parse()

    handler = Handler()

    ndfsa_stack = []

    for element in elements:
        handler.handlers[element.name](element, ndfsa_stack)

    # assert len(ndfsa_stack) == 1  # todo
    return ndfsa_stack.pop()
