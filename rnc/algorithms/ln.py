from algorithms.helpers.base_class import BaseClassForAlgoritms
from algorithms.nr import NR as nrAlgorithmClass
import math


class LN(BaseClassForAlgoritms):
    def __init__(self, inputFileName, p1, p2):
        super().__init__('ln', p1, p2, None, inputFileName, showLogs=True)
        newNR = nrAlgorithmClass(inputFileName, 0, 1, showLogs=False)
        newNR.generate_sequence()
        self.results = newNR.results

    def _generate_sequence_core(self):
        self.results = [int(self.p1 + math.exp(self.p2 - z)) for z in self.results]
