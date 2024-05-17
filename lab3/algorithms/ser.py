from algorithms.helpers.base_class import BaseClassForAlgoritms
import math
import scipy.stats


def calculate_chi(matches, est):
    return sum(((matches[key] - est) ** 2) / est for key in matches)


class SER(BaseClassForAlgoritms):
    def __init__(self, inputFileName):
        super().__init__(inputFileName)
        self.d = 4
        self.inputData = list(map(lambda x: math.floor(x * self.d) % self.d, self.inputData))

    def _check_criterion_core(self):
        self.main()

    def main(self):
        k = self.d ** 2
        pairs, chi_stat = {(i, j): 0 for i in range(self.d) for j in range(self.d)}, 0
        Ej = round(len(self.inputData) / (2 * k), 3)

        self.calculate_pairs(pairs)

        self.print_series_results(pairs,
                                  Ej,
                                  round(scipy.stats.chi2.ppf(1 - 0.05, k - 1), 3),
                                  round(calculate_chi(pairs, Ej), 3))

    def calculate_pairs(self, pairs):
        for i in range(0, len(self.inputData), 2):
            if i + 1 < len(self.inputData):
                pairs[(self.inputData[i], self.inputData[i + 1])] += 1

    def print_series_results(self, pairs, Ej, chi_crit, chi_result):
        keys = pairs.keys()
        keysArray = []
        for key in keys:
            keysArray.append(key)
        values = pairs.values()
        valuesArray = []
        for value in values:
            valuesArray.append(value)
        print("Пара: кол-во чисел")
        for i in range(len(keysArray)):
            print(f'{keysArray[i]}: {valuesArray[i]}')
        print(f"Ej: {Ej}.")
        print(f"d: {self.d}.")
        print(f"k: {self.d ** 2}.")
        print(f"хи-квадрат: {chi_result}.")
        print(f"Критическое значение хи-квадрат: {chi_crit}.")
        if chi_result < chi_crit:
            print(f"ППСЧ удовлетворяет критерию серий")
        else:
            print(f"ППСЧ не удовлетворяет критерию серий")
