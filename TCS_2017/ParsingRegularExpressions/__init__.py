from TCS_2017.ParsingRegularExpressions.InputReader import InputReader
from TCS_2017.ParsingRegularExpressions.OutputWriter import OutputWriter
from TCS_2017.ParsingRegularExpressions.automaton import reg_exp_parse

if __name__ == "__main__":
    input_reader = InputReader()
    output_writer = OutputWriter()

    cases_number = int(input_reader.read_one_line())
    for i in range(cases_number):
        reg_exp = input_reader.read_one_line()
        automaton = reg_exp_parse(reg_exp)

        test_cases_list = input_reader.read_test_cases_from_input_file()

        for j in range(len(test_cases_list)):
            result = automaton.validate(test_cases_list[j])
            # result = automaton.compute_test(test_cases_list[j])
            output_writer.write_a_string(str(result) + "\n")  # result_string

    input_reader = input_reader.close_input_file()
    output_file = output_writer.close_output_file()
