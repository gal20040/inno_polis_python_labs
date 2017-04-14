from TCS_2017.ParsingRegularExpressions.Automaton import Automaton
from TCS_2017.ParsingRegularExpressions.InputReader import InputReader
from TCS_2017.ParsingRegularExpressions.OutputWriter import OutputWriter

if __name__ == "__main__":
    input_reader = InputReader()
    output_writer = OutputWriter()

    cases_number = int(input_reader.read_one_line())
    for i in range(cases_number):
        reg_exp = input_reader.read_one_line()
        test_cases_list = input_reader.read_test_cases_from_input_file()

        automaton = Automaton(reg_exp)

        for j in range(len(test_cases_list)):
            result = automaton.compute_test(test_cases_list[j])
            output_writer.write_a_string(result + "\n")  # result_string

    input_reader.close_input_file()
    output_writer.close_output_file()
    input_reader = None
    output_file = None
