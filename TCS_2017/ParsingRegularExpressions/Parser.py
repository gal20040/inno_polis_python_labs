import NDFSA

LEFT_PARENTHESIS = 'LEFT_PARENTHESIS'
RIGHT_PARENTHESIS = 'RIGHT_PARENTHESIS'
STAR_MARK = 'STAR_MARK'
ALTERNATION = 'ALTERNATION'
CONCATENATION = 'CONCATENATION'
CONCAT_VALUE = '\x08'
PLUS_MARK = 'PLUS_MARK'
QUESTION_MARK = 'QUESTION_MARK'
CHAR = 'CHAR'
NONE = 'NONE'
EMPTY_VALUE = ''
Q_SIGN = 'q'


def reg_exp_parse(reg_exp):

    lexer = Lexer(reg_exp)
    parser = Parser(lexer)
    elements = parser.parse()

    handler = Handler()

    ndfsa_stack = []

    for element in elements:
        handler.handlers[element.name](element, ndfsa_stack)

    assert len(ndfsa_stack) == 1
    return ndfsa_stack.pop()


class Element:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Lexer:
    def __init__(self, reg_exp):
        self.reg_exp = reg_exp
        self.quantifiers = {'(': LEFT_PARENTHESIS,
                            ')': RIGHT_PARENTHESIS,
                            '*': STAR_MARK,
                            '|': ALTERNATION,
                            CONCAT_VALUE: CONCATENATION,
                            '+': PLUS_MARK,
                            '?': QUESTION_MARK}
        self.current_element_index = 0
        self.reg_exp_length = len(self.reg_exp)

    def get_element(self):
        if self.current_element_index < self.reg_exp_length:
            element = self.reg_exp[self.current_element_index]
            self.current_element_index += 1
            if element in self.quantifiers.keys():
                element = Element(self.quantifiers[element], element)
            else:
                element = Element(CHAR, element)
            return element
        else:
            return Element(NONE, EMPTY_VALUE)


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.all_elements = []
        self.current_element = self.lexer.get_element()

    def get_next_element(self, name):
        if self.current_element.name == name:
            self.current_element = self.lexer.get_element()
        else:
            raise ParseError

    def parse(self):
        self.expression()
        return self.all_elements

    def expression(self):
        self.term()
        if self.current_element.name == ALTERNATION:
            curr_elem = self.current_element
            self.get_next_element(ALTERNATION)
            self.expression()
            self.all_elements.append(curr_elem)

    def term(self):
        self.factor()
        if self.current_element.value not in ')|':
            self.term()
            self.all_elements.append(Element(CONCATENATION, CONCAT_VALUE))

    def factor(self):
        self.primary()
        if self.current_element.name in [STAR_MARK, PLUS_MARK, QUESTION_MARK]:
            self.all_elements.append(self.current_element)
            self.get_next_element(self.current_element.name)

    def primary(self):
        if self.current_element.name == LEFT_PARENTHESIS:
            self.get_next_element(LEFT_PARENTHESIS)
            self.expression()
            self.get_next_element(RIGHT_PARENTHESIS)
        elif self.current_element.name == CHAR:
            self.all_elements.append(self.current_element)
            self.get_next_element(CHAR)


class ParseError(Exception):
    pass


class State:
    def __init__(self, name):
        self.ancestors_names = ""
        self.epsilon = []
        self.is_end = False
        self.name = name
        self.transitions = {}

    def __str__(self):
        return self.name


class Handler:
    def __init__(self):
        self.state_counter = 0
        self.handlers = {ALTERNATION:   self.handle_alt,
                         CHAR:          self.handle_char,
                         CONCATENATION: self.handle_concat,
                         PLUS_MARK:     self.handle_rep,
                         STAR_MARK:     self.handle_rep,
                         QUESTION_MARK: self.handle_qmark}

    def create_state(self):
        state = State(Q_SIGN + str(self.state_counter))
        self.state_counter += 1
        return state

    def handle_char(self, element, ndfsa_stack):
        state0 = self.create_state()
        state1 = self.create_state()
        state0.transitions[element.value] = state1
        ndfsa = NDFSA.init_ndfsa(state0, state1)
        ndfsa_stack.append(ndfsa)

    @staticmethod
    def handle_concat(element, ndfsa_stack):
        ndfsa2 = ndfsa_stack.pop()
        ndfsa1 = ndfsa_stack.pop()
        ndfsa1.end.is_end = False
        if len(ndfsa1.end.epsilon) == 0:

            for transition_symbol in ndfsa2.start.transitions.keys():
                transition_state = ndfsa2.start.transitions[transition_symbol]
                if transition_state not in ndfsa1.end.transitions.keys():
                    ndfsa1.end.transitions[transition_symbol] = transition_state

            for ndfsa2_eps in ndfsa2.start.epsilon:
                ndfsa1.end.epsilon.append(ndfsa2_eps)

        else:
            ndfsa1.end.epsilon.append(ndfsa2.start)
        ndfsa = NDFSA.init_ndfsa(ndfsa1.start, ndfsa2.end)
        ndfsa_stack.append(ndfsa)

    def handle_alt(self, element, ndfsa_stack):
        ndfsa2 = ndfsa_stack.pop()
        ndfsa1 = ndfsa_stack.pop()
        state0 = self.create_state()
        state0.epsilon.append(ndfsa1.start)
        state0.epsilon.append(ndfsa2.start)
        state3 = self.create_state()
        ndfsa1.end.epsilon.append(state3)
        ndfsa2.end.epsilon.append(state3)
        ndfsa1.end.is_end = False
        ndfsa2.end.is_end = False
        ndfsa = NDFSA.init_ndfsa(state0, state3)
        ndfsa_stack.append(ndfsa)

    def handle_rep(self, element, ndfsa_stack):
        ndfsa1 = ndfsa_stack.pop()
        state0 = self.create_state()
        state1 = self.create_state()
        state0.epsilon.append(ndfsa1.start)
        if element.name == STAR_MARK:
            state0.epsilon.append(state1)
        ndfsa1.end.epsilon.extend([state1, ndfsa1.start])
        ndfsa1.end.is_end = False
        ndfsa = NDFSA.init_ndfsa(state0, state1)
        ndfsa_stack.append(ndfsa)

    @staticmethod
    def handle_qmark(element, ndfsa_stack):
        ndfsa1 = ndfsa_stack.pop()
        ndfsa1.start.epsilon.append(ndfsa1.end)
        ndfsa_stack.append(ndfsa1)
