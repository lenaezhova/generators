from algorithms.helpers.base_class import BaseClassForAlgoritms
import math


class NR(BaseClassForAlgoritms):
    def __init__(self, inputFileName, p1, p2, showLogs=True):
        super().__init__('nr', p1, p2, None, inputFileName, showLogs)

    def _generate_sequence_core(self):
        max_value = max(self.inputData) + 1
        normalized_data = [x / max_value for x in self.inputData]
        mu = self.p1
        sigma = self.p2

        u1, u2 = [], []
        for index, value in enumerate(normalized_data):
            if index % 2 == 0:
                u1.append(value)
            else:
                u2.append(value)

        min_length = min(len(u1), len(u2))
        u1 = u1[:min_length]
        u2 = u2[:min_length]

        results_cos = [int(mu + sigma * math.sqrt(-2 * math.log(1 - u)) * math.cos(2 * math.pi * v)) for u, v in zip(u1, u2)]
        results_sin = [int(mu + sigma * math.sqrt(-2 * math.log(1 - u)) * math.sin(2 * math.pi * v)) for u, v in zip(u1, u2)]

        self.results = results_cos + results_sin
