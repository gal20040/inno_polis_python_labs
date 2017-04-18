class OutputWriter(object):
    def __init__(self):
        output_file_name = "output.txt"
        self.output_file = open(output_file_name, 'w')

    def close_output_file(self):
        self.output_file.close()
        self.output_file = None
        return None

    def write_a_string(self, string):
        self.output_file.write(string)
