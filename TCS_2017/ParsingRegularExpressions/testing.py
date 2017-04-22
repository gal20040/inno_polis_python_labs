import unittest
from TCS_2017.ParsingRegularExpressions.automaton import reg_exp_parse


class TestRegex(unittest.TestCase):
    def base(self, file_name):
        with open(file_name) as file:
            self.text = file.readlines()
        
        for line in self.text:
            llist = line.split()
            reg_exp = None
            true_string = None
            false_string = None
            if len(llist) == 2:
                [reg_exp, true_string] = llist
            elif len(llist) == 3:
                [reg_exp, true_string, false_string] = llist
            automaton = reg_exp_parse(reg_exp)

            result = automaton.validate(true_string)
            if result is False:
                self.assertEqual(False, True)

            if false_string:
                result = automaton.validate(false_string)
                if result is not False:
                    self.assertEqual(True, False)

            print(line, "pass")
    
    def test_basic(self):
        self.base('test_suite.dat')

if __name__ == '__main__':
    unittest.main()
