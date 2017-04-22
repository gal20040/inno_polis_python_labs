import unittest

import Parser
from __init__ import remove_redundant_breakspaces
from InputReader import InputReader


class TestRegex(unittest.TestCase):
    def base(self, file_name):
        input_reader = InputReader(file_name)

        reg_exp = input_reader.read_one_line()
        while reg_exp != "":
            ndfsa = Parser.reg_exp_parse(reg_exp)

            test_cases_list = input_reader.read_test_cases_and_results_from_input_file()

            for j in range(len(test_cases_list)):
                result_string = ndfsa.validate(test_cases_list[j][0])

                if not result_string:  # for cases: result = False
                    result_string = ""

                result_string = remove_redundant_breakspaces(result_string)
                test_case_result = test_cases_list[j][1]
                self.assertEqual(result_string, test_case_result)

                print(reg_exp + " " + test_case_result, "pass")

            reg_exp = input_reader.read_one_line()

        input_reader.close_input_file()

    def test_basic(self):
        self.base('tests.txt')

if __name__ == '__main__':
    unittest.main()
