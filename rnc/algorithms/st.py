from algorithms.helpers.base_class import BaseClassForAlgoritms


def compute_divisor(data):
    return max(data) + 1


class ST(BaseClassForAlgoritms):
    def __init__(self, inputFileName, p1, p2):
        super().__init__('st', p1, p2, None, inputFileName, showLogs=True)

    def process_number(self, number, divisor):
        result = number / divisor
        result *= self.p2
        return int(result + self.p1)

    def _generate_sequence_core(self):
        divisor = compute_divisor(self.inputData)
        self.results = []
        for number in self.inputData:
            processed = self.process_number(number, divisor)
            self.results.append(processed)
