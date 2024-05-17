from algorithms.helpers.base_class import BaseClassForAlgoritms
import numpy as np
import scipy


def print_stats(Ej, chi_res, chi_critical, k):
    print(f"Ej: {Ej}.")
    print(f"k: {k}")
    print(f"хи-квадрат: {chi_res}.")
    print(f"Критическое значение хи-квадрат: {chi_critical}.")
    if 0 < chi_res < chi_critical:
        print(f"ППСЧ удовлетворяет критерию хи-квадрат")
    else:
        print(f"ППСЧ не удовлетворяет критерию хи-квадрат")


class CHI(BaseClassForAlgoritms):
    def __init__(self, inputFileName):
        super().__init__(inputFileName)

    def _check_criterion_core(self):
        d = self.inputData
        ints = self.intervals
        l = len(d)
        n = [0] * len(ints)

        for i in range(l):
            for j in range(len(ints)):
                if ints[j][0] <= d[i] < ints[j][1]:
                    n[j] += 1
                    break

        print("Интервал: кол-во чисел в интервале")
        for i in range(len(n)):
            print(f'{np.round(ints[i], 4)}: {n[i]}')

        Ej = round(l / len(ints), 3)
        print_stats(Ej,
                    round(sum([((n[j] - Ej) ** 2) / Ej for j in range(len(ints))]), 4),
                    round(scipy.stats.chi2.ppf(1 - 0.05, df=(len(ints) - 1)), 4),
                    len(ints))
