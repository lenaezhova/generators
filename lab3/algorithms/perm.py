from algorithms.helpers.base_class import BaseClassForAlgoritms
import scipy.stats
import math
import itertools


class PERM(BaseClassForAlgoritms):
    def __init__(self, inputFileName):
        super().__init__(inputFileName)

    def _check_criterion_core(self):
        t = 3
        self.evaluate_permutations(t)

    def evaluate_permutations(self, t):
        n = len(self.inputData) // t
        f = math.factorial(t)
        uj = {i: 0 for i in range(f)}
        crit = round(scipy.stats.chi2.ppf(1 - 0.05, f - 1), 3)
        permutations = list(itertools.permutations(range(t)))
        perm_index = {perm: i for i, perm in enumerate(permutations)}
        for i in range(n):
            group = self.inputData[i * t: (i + 1) * t]
            if len(set(group)) == t:
                sorted_indices = tuple(sorted(range(t), key=lambda x: group[x]))
                if sorted_indices in perm_index:
                    index = perm_index[sorted_indices]
                    uj[index] += 1
        Ej = 1 / f
        chi = sum((uj[i] - n * Ej) ** 2 / (n * Ej) for i in range(f))

        ujArray = []
        for i in range(len(uj)):
            ujArray.append(uj[i])

        print(f"uj: {ujArray}.")
        print(f"Ej: {Ej}.")
        print(f"k: {f + 1}")
        print(f"хи-квадрат: {chi}.")
        print(f"Критическое значение хи-квадрат: {crit}.")
        if chi < crit:
            print(f"ППСЧ удовлетворяет критерию перестановок")
        else:
            print(f"ППСЧ не удовлетворяет критерию перестановок")
