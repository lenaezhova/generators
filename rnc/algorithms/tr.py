from algorithms.helpers.base_class import BaseClassForAlgoritms
import random


class TR(BaseClassForAlgoritms):
    def __init__(self, inputFileName, p1, p2):
        super().__init__('tr', p1, p2, None, inputFileName, showLogs=True)

    def _generate_sequence_core(self):
        max_value = max(self.inputData) + 1
        normalized_data = [x / max_value for x in self.inputData]
        u1, u2 = [], []
        for index, value in enumerate(normalized_data):
            if index % 2 == 0:
                u1.append(value)
            else:
                u2.append(value)
        min_length = min(len(u1), len(u2))
        u1 = u1[:min_length]
        u2 = u2[:min_length]
        self.results = [int(self.p1 + self.p2 * (first + second - 1)) for first, second in zip(u1, u2)]
