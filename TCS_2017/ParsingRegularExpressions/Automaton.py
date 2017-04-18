# class Automaton(object):
#     def __init__(self, reg_exp):
#         # self.array_of_states = self.parse_initial_description_to_array(description_list[0])
#         #
#         self.array_of_alphabet = {0, 1}
#
#         self.reg_exp = reg_exp
#         self.parse_reg_exp()
#         #
#         # self.array_of_final_states = self.parse_initial_description_to_array(description_list[3])
#         #
#         # self.matrix_of_transitions = self.parse_transitions_to_matrix(description_list[4])
#
#     def parse_reg_exp(self):
#         pass
#
#     # def parse_initial_description_to_array(self, string):
#     #     comma_sign = ","
#     #     begin_from = 0
#     #     comma_position = 0
#     #     temp_array = []
#     #
#     #     while comma_position != -1:
#     #         comma_position = string.find(comma_sign, begin_from)
#     #         if comma_position != -1:
#     #             substring = string[begin_from:comma_position]
#     #             temp_array.append(substring)
#     #             begin_from = comma_position + 1
#     #         else:
#     #             substring = string[begin_from:]
#     #             temp_array.append(substring)
#     #
#     #     return temp_array
#     #
#     # def parse_transitions_to_matrix(self, string):
#     #     states_quantity = len(self.array_of_states)
#     #     matrix_of_transitions = [[""] * states_quantity for i in range(states_quantity)]
#     #
#     #     comma_sign = ","
#     #     left_parenthesis = "("
#     #     right_parenthesis = ")"
#     #     arrow_sign = "->"
#     #     comma_position = 0
#     #     begin_from = 0
#     #     zero = 0
#     #
#     #     while comma_position != -1:
#     #         comma_position = string.find(comma_sign, begin_from)
#     #         if comma_position != -1:
#     #             substring = string[begin_from:comma_position]
#     #
#     #         else:
#     #             substring = string[begin_from:]
#     #
#     #         left_parenthesis_position = substring.find(left_parenthesis, zero)
#     #         right_parenthesis_position = substring.find(right_parenthesis, zero)
#     #         arrow_sign_position = substring.find(arrow_sign, zero)
#     #
#     #         from_state = substring[:left_parenthesis_position]
#     #         char = substring[left_parenthesis_position + 1:right_parenthesis_position]
#     #         to_state = substring[arrow_sign_position + 2:]
#     #
#     #         """get indexes of states"""
#     #         from_state_index = self.get_index_of_array_value(from_state)
#     #         to_state_index = self.get_index_of_array_value(to_state)
#     #
#     #         if matrix_of_transitions[from_state_index][to_state_index] == "":
#     #             matrix_of_transitions[from_state_index][to_state_index] = char
#     #         else:
#     #             matrix_of_transitions[from_state_index][to_state_index] += char
#     #
#     #         begin_from = comma_position + 1
#     #
#     #     return matrix_of_transitions
#     #
#     # def get_index_of_array_value(self, value):
#     #     for i in range(len(self.array_of_states)):
#     #         if self.array_of_states[i] == value:
#     #             return i
#
#     def compute_test(self, test_case):
#         result_string = "False"
#     #     arrow = "->"
#     #     for test_string in test_cases_list:
#     #         current_state = self.initial_state
#     #         all_transitions = current_state
#     #         zero = 0
#     #
#     #         for letter in test_string:
#     #             current_state_index = self.get_index_of_array_value(current_state)
#     #             """run for all cells in row with index=current_state_index"""
#     #             for j in range(len(self.array_of_states)):
#     #
#     #                 """check if there is LETTER in that cell"""
#     #                 if self.matrix_of_transitions[current_state_index][j].find(letter, zero) != -1:
#     #                     current_state = self.array_of_states[j]
#     #                     all_transitions = all_transitions + arrow + current_state
#     #                     break
#     #
#     #         result = "False"
#     #         for state in self.array_of_final_states:
#     #             if current_state == state:
#     #                 result = "True"
#     #
#     #         result_string = result_string + "\n" + result + "," + all_transitions
#     #
#         return result_string
