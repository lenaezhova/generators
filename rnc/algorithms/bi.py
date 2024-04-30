import math
import random
from algorithms.helpers.base_class import BaseClassForAlgoritms


def generate_binomials(n, p):
    binomials = []
    q = 1 - p
    bin_coeff = 1
    for k in range(n + 1):
        if k > 0:
            bin_coeff = bin_coeff * (n - k + 1) / k
        prob = bin_coeff * (p ** k) * (q ** (n - k))
        binomials.append(prob)
    return binomials


class BI(BaseClassForAlgoritms):
    def __init__(self, inputFileName, n, p):
        super().__init__('bi', n, p, None, inputFileName, showLogs=True)
        self.n = int(n)
        self.p = float(p)

    def _generate_sequence_core(self):
        max_value = max(self.inputData) + 1
        normalized_data = [x / max_value for x in self.inputData]
        binomials = generate_binomials(self.n, self.p)
        for u in normalized_data:
            sum_p = 0
            for k, binom in enumerate(binomials):
                sum_p += binom
                if sum_p >= u:
                    self.results.append(k)
                    break
