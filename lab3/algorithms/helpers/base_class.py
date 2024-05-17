import numpy as np
import math


def randomize_if_one(d, i):
    return round(np.random.uniform(), 3) if d[i] == 1.0 else d[i]


def create_intervals(d):
    l, r = min(d), max(d)
    num = math.ceil(math.log(len(d)))
    step = round((r - l) / num, 4)
    return [(l + i * step, l + (i + 1) * step) for i in range(num)]


class BaseClassForAlgoritms:
    def __init__(self, inputFileName):
        self.table = (0.01, 0.05, 0.25, 0.50, 0.75, 0.95, 0.99, 1.00)
        self.inputData = []
        self.initInputData(inputFileName)
        self.intervals = []
        self._data_processing()

    def _data_processing(self):
        u = np.unique(self.inputData)
        self.calc_intervals(u)

    def calc_intervals(self, u):
        le, cri = len(self.inputData), 10
        if len(u) > cri:
            self.inputData = [randomize_if_one(self.inputData, i) for i in range(le)]
            self.intervals = create_intervals(self.inputData)
        else:
            self.inputData = [self.inputData[i] if self.inputData[i] != 1.0 else self.inputData[i] - 0.01 for i in range(le)]
            u = np.unique(self.inputData)
            self.intervals = [(val - 0.01, val + 0.01) for val in u]

    def initInputData(self, inputFileName):
        f = open(f'tests/{inputFileName}.dat', "r")
        self.inputData = list(map(float, (f.read()).split(',')))

    def check_criterion(self):
        self._check_criterion_core()

    def _check_criterion_core(self):
        raise NotImplementedError("Метод должен быть переопределен")
