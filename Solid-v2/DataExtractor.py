"""Data Extractor"""
import re


class DataExtractor():
    """A class to extract data"""

    def __init__(self, filename, key_col, max_col, min_col):
        self.file = open(filename, "r", encoding='utf-8')
        self.key_col = key_col
        self.max_col = max_col
        self.min_col = min_col

    def extract(self):
        self.keyval = []
        self.maxval = []
        self.minval = []

        for index, data in enumerate(self.file):
            if index == 0:
                continue
            if not data.split() or data.split()[0] == 'mo' or len(data.split()) == 1:
                continue

            result = re.sub(r'[!@#*$]', '', data.split()[self.max_col])
            result1 = re.sub(r'[!@#*$]', '', data.split()[self.min_col])

            self.maxval.append(int(result))
            self.minval.append(int(result1))
            self.keyval.append(data.split()[self.key_col])
        # print(self.keyval)
        # print(self.maxval)
        # print(self.minval)

        return self.keyval, self.maxval, self.minval
