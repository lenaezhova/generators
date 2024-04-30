from algorithms.helpers.base_class import BaseClassForAlgoritms
import math


class GM(BaseClassForAlgoritms):
    def __init__(self, inputFileName, p1, p2, p3):
        super().__init__('gm', p1, p2, p3, inputFileName, showLogs=True)

    def _generate_sequence_core(self):
        max_value = max(self.inputData) + 1
        normalized_data = [x / max_value for x in self.inputData if x > 0]
        u1, u2 = [], []
        for index, value in enumerate(normalized_data):
            if index % 2 == 0:
                u1.append(value)
            else:
                u2.append(value)
        min_length = min(len(u1), len(u2))
        u1 = u1[:min_length]
        u2 = u2[:min_length]

        if 1 > self.p3 > 0:
            self.results = [int(self.p1 + self.p2 * (1 + u * math.sin(math.pi * self.p3)) / (u ** self.p3 - 1) * v) for u, v in zip(u1, u2)]
        elif 1 <= self.p3 <= 2:
            self.results = [int(self.p1 + self.p2 * (1 + u * math.sin(math.pi * self.p3)) / (u ** self.p3 - 1) * v) for u, v in zip(u1, u2)]
        else:
            self.results = [int(self.p1 + self.p2 * (u - v) / (u + v)) for u, v in zip(u1, u2)]
