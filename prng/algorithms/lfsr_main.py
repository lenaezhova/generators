from algorithms.helpers.base_class import BaseClassForAlgoritms
import random


class LFSR(BaseClassForAlgoritms):
    def __init__(self, p, w, coeffs, initSequence=None):
        super().__init__()
        self.bits = initSequence
        if initSequence is None or len(initSequence) == 0:
            self.bits = [random.randint(0, 1) for _ in range(p)]
            self.bits.reverse()
        elif len(initSequence) < p:
            randomSequence = [random.randint(0, 1) for _ in range(p - len(initSequence))]
            randomSequence.reverse()
            self.bits = initSequence + randomSequence

        self.p = p
        self.w = w
        self.coeffs = coeffs

    def _generate_sequence_core(self, count):
        lengthCoef = len(self.coeffs)
        for i in range(count * self.w):

            newVal = sum(self.bits[i + self.coeffs[k]] for k in range(lengthCoef)) % 2
            self.bits.append(newVal)
            if i % (self.w - 1) == 0 and i != 0:
                converted_result = sum((2 ** idx) * bit for idx, bit in enumerate(self.bits[-self.w:]))
                self.put_in_results(converted_result)
