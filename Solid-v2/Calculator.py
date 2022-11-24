import DataExtractor
import DataAnalyzer


class Calculator():
    def __init__(self, file_name, key_col, max_col, min_col):
        self.file_name = file_name
        self.key_col = key_col
        self.max_col = max_col
        self.min_col = min_col

    def calculate(self):
        extracter_obj = DataExtractor.DataExtractor(
            self.file_name, self.key_col, self.max_col, self.min_col)
        output = extracter_obj.extract()
        analyzer_obj = DataAnalyzer.DataAnalyzer(
            output[0], output[1], output[2])
        analyzer_obj.calculate_diff()
