import math
import random
from algorithms.helpers.base_class import BaseClassForAlgoritms


class LS(BaseClassForAlgoritms):
    def __init__(self, inputFileName, p1, p2):
        super().__init__('ls', p1, p2, None, inputFileName, showLogs=True)

    def _generate_sequence_core(self):
        max_value = max(self.inputData) + 1
        self.results = []

        for num in self.inputData:
            normalized = num / max_value
            if normalized == 0.0:
                normalized = random.uniform(0, 1)

            logit_transform = self.p1 + self.p2 * math.log(normalized / (1 - normalized))
            self.results.append(int(logit_transform))
