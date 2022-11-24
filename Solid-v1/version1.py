"""data maunging project"""
import re


class Weather():

    def __init__(self):
        self.weather_file = open("weather.dat", "r", encoding='utf-8')

    def show_minTemp(self):
        self.keyval = []
        self.maxval = []
        self.minval = []

        for index, data in enumerate(self.weather_file):
            if index == 0:
                continue
            if not data.split() or data.split()[0] == 'mo' or len(data.split()) == 1:
                continue

            result = re.sub(r'[!@#*$]', '', data.split()[1])
            result1 = re.sub(r'[!@#*$]', '', data.split()[2])

            # if len(data.split()[1])>2:
            #     self.maxval.append(int(data.split()[1][:2]))
            # if len(data.split()[2])>2:
            #     self.minval.append(int(data.split()[2][:2]))
            self.maxval.append(int(result))
            self.minval.append(int(result1))
            self.keyval.append(data.split()[0])
            # diff = data.split()[1]
            # print(,data.split()[1], data.split()[2])
        print(self.keyval)
        print(self.maxval)
        print(self.minval)

        self.diff_val = [abs(self.maxval[i]-self.minval[i])
                         for i in range(len(self.maxval))]
        print(self.diff_val)
        min_diff = min(self.diff_val)
        print(self.keyval[self.diff_val.index(min_diff)], min_diff)


class Football():

    def __init__(self):
        self.football_file = open("football.dat", "r", encoding='utf-8')

    def show_goals(self):
        # for index, data in enumerate(self.football_file):
        #     if index == 0:
        #         continue
        #     if len(data.split()) == 1:
        #         continue

        #     name = data.split()[1]
        #     diff = int(data.split()[6])-int(data.split()[8])
        #     print(name, diff)
        self.keyval = []
        self.maxval = []
        self.minval = []

        for index, data in enumerate(self.football_file):
            if index == 0:
                continue
            if not data.split() or data.split()[0] == 'mo' or len(data.split()) == 1:
                continue

            result = re.sub(r'[!@#*$]', '', data.split()[6])
            result1 = re.sub(r'[!@#*$]', '', data.split()[8])

            # if len(data.split()[1])>2:
            #     self.maxval.append(int(data.split()[1][:2]))
            # if len(data.split()[2])>2:
            #     self.minval.append(int(data.split()[2][:2]))
            self.maxval.append(int(result))
            self.minval.append(int(result1))
            self.keyval.append(data.split()[1])
            # diff = data.split()[1]
            # print(,data.split()[1], data.split()[2])
        print(self.keyval)
        print(self.maxval)
        print(self.minval)

        self.diff_val = [abs(self.maxval[i]-self.minval[i])
                         for i in range(len(self.maxval))]
        print(self.diff_val)
        min_diff = min(self.diff_val)
        print(self.keyval[self.diff_val.index(min_diff)], min_diff)


obj = Weather()
obj.show_minTemp()
obj_f = Football()
obj_f.show_goals()
