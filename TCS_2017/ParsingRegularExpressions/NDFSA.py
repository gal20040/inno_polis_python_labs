def init_ndfsa(start, end):

    return NDFSA(start, end)


class NDFSA(object):
    __result = ""

    def __init__(self, start, end):
        self.start = start
        self.end = end
        end.is_end = True

    def add_state(self, state, state_set, ancestors_names):
        if state not in state_set:
            state_set.add(state)
            state.ancestors_names = ancestors_names
            for eps in state.epsilon:
                if state.ancestors_names == "":
                    ancestors_names = state.name
                else:
                    ancestors_names = state.ancestors_names + state.name
                self.add_state(eps, state_set, ancestors_names)

    def validate(self, string):
        current_states = set()
        self.__result = ""
        ancestors_names = ""
        self.add_state(self.start, current_states, ancestors_names)

        for symbol in string:
            next_states = set()
            for state in current_states:
                if symbol in state.transitions.keys():
                    transition_state = state.transitions[symbol]
                    ancestors_names = state.ancestors_names + state.name
                    self.add_state(transition_state, next_states, ancestors_names)

            current_states = next_states

        for state in current_states:
            if state.is_end:
                if state.ancestors_names != "":
                    self.__result = state.ancestors_names
                self.__result += state.name
                return self.__result
        return False
