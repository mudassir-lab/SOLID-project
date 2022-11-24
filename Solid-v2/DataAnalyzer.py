"""Analyzer"""


class DataAnalyzer():
    '''A class to analyse data'''

    def __init__(self, key_val, max_val, min_val):
        self.difflist = []
        self.key_val = key_val
        self.max_val = max_val
        self.min_val = min_val

    def calculate_diff(self):
        self.diff_val = [abs(self.max_val[i]-self.min_val[i])
                         for i in range(len(self.max_val))]
        # print(self.diff_val)
        min_diff = min(self.diff_val)
        print(self.key_val[self.diff_val.index(min_diff)], min_diff)
