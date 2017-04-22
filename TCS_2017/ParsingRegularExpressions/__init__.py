from InputReader import InputReader
from OutputWriter import OutputWriter
from automaton import reg_exp_parse


def remove_extra_breakspaces(string):
    string = string.replace('q', ' q')
    string = string.replace(' ', '', 1)

    string_prev = ""
    while string_prev != string:
        string_prev = string
        string = string.replace('  ', ' ')

    return string


if __name__ == "__main__":
    input_reader = InputReader()
    output_writer = OutputWriter()

    cases_number = 1  # int(input_reader.read_one_line())
    for i in range(cases_number):
        reg_exp = input_reader.read_one_line()
        automaton = reg_exp_parse(reg_exp)

        test_cases_list = input_reader.read_test_cases_from_input_file()

        for j in range(len(test_cases_list)):
            result_string = ""
            result = automaton.validate(test_cases_list[j])

            if not result:  # for cases: result = False
                result = ""

            if j != len(test_cases_list) - 1:
                result += "\n"
            result_string += result

            result_string = remove_extra_breakspaces(result_string)

            output_writer.write_a_string(result_string)

    input_reader = input_reader.close_input_file()
    output_file = output_writer.close_output_file()
