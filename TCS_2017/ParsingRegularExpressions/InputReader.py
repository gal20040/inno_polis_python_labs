class InputReader(object):
    def __init__(self, input_file_name):
        self.input_file = open(input_file_name, 'r')  # 'r' - open for reading

    def read_one_line(self):
        return self.input_file.readline().replace('\n', '')

    # returns list with test cases
    def read_test_cases_from_input_file(self):
        test_case_number = int(self.read_one_line())

        test_cases_list = []
        """read test strings for the ndfsa"""
        for j in range(test_case_number):
            test_cases_list.append(self.read_one_line())

        return test_cases_list

    # returns list with test cases and results
    def read_test_cases_and_results_from_input_file(self):
        test_case_number = int(self.read_one_line())

        test_cases_list = []
        """read test strings for the ndfsa"""
        for j in range(test_case_number):
            test_cases_list.append([self.read_one_line(), self.read_one_line()])

        return test_cases_list

    def close_input_file(self):
        self.input_file.close()
        self.input_file = None
        return None
