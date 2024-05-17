from algorithms.helpers.base_class import BaseClassForAlgoritms
import scipy.stats
import random


def print_results(chi, params):
    t, n, a, b, prpt, count, crit = params
    print(f"t: {t}.")
    print(f"n: {n}.")
    print(f"a: {a}.")
    print(f"b: {b}.")
    print(f"k: {t}.")
    print(f"pr, pt: {prpt}")
    print(f"хи-квадрат: {round(chi, 3)}.")
    print(f"Критическое значение хи-квадрат: {crit}.")
    print(f"Значения интервалов: {count}")
    if chi < crit:
        print(f"ППСЧ удовлетворяет критерию интервалов")
    else:
        print(f"ППСЧ не удовлетворяет критерию интервалов")


class INTER(BaseClassForAlgoritms):
    def __init__(self, inputFileName):
        super().__init__(inputFileName)

    def _check_criterion_core(self):
        self.main()

    def main(self):
        a = random.uniform(0, 1)
        b = random.uniform(0, 1)

        while not (0.2 < abs(a - b) < 0.4):
            a, b = random.uniform(0, 1), random.uniform(0, 1)

        if b < a:
            a, b = b, a
        a, b = round(a, 3), round(b, 3)
        p = b - a

        best_chisq = float('inf')
        best_parameters = None

        for t in range(8, 12):
            prpt = [round(p * ((1 - p) ** r), 3) for r in range(t)] + [round((1 - p) ** t, 4)]

            for n in range(1000, 2000):
                cr = [0] * (t + 1)
                r, s = 0, 0

                for j in range(len(self.inputData)):
                    if a <= self.inputData[j] < b:
                        index = min(r, t)
                        cr[index] += 1
                        r, s = 0, s + 1
                        if s >= n:
                            break
                    else:
                        r += 1

                chisq = sum(((c - n * prob) ** 2) / (n * prob) for c, prob in zip(cr, prpt) if n * prob != 0)

                if chisq < best_chisq:
                    best_chisq = chisq
                    crit = round(scipy.stats.chi2.ppf(1 - 0.05, t + 1), 3)
                    best_parameters = (t, n, a, b, prpt, cr, crit)

        print_results(best_chisq, best_parameters)
