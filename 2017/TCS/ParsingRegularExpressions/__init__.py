# from FSAsimulator.Automaton import Automaton
# from FSAsimulator.OutputWriter import OutputWriter
# from FSAsimulator.InputReader import InputReader
#
# input_reader = InputReader()
# output_writer = OutputWriter()
#
# output_writer.write_a_string("ArtemGrodetskiy\n")
#
# cases_number = int(input_reader.read_one_line())
# for i in range(cases_number):
#     description_list = input_reader.read_description_from_input_file()
#     automaton = Automaton(description_list)
#
#     output_writer.write_a_string(str(i + 1))  # Test case number
#
#     test_cases_list = input_reader.read_test_cases_from_input_file()
#     result = automaton.compute_test(test_cases_list)
#     output_writer.write_a_string(result + "\n")  # result_string
#
# input_reader.close_input_file()
# output_writer.close_output_file()
# input_reader = None
# output_file = None
