from algorithms.helpers.base_class import BaseClassForAlgoritms
import math


class EX(BaseClassForAlgoritms):
    def __init__(self, inputFileName, p1, p2):
        super().__init__('ex', p1, p2, None, inputFileName, showLogs=True)

    def _generate_sequence_core(self):
        max_value = max(self.inputData) + 1
        normalized_data = [x / max_value for x in self.inputData if x != 0]
        self.results = [int(self.p1 - self.p2 * math.log(x)) for x in normalized_data if x > 0]
