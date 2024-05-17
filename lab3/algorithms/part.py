from algorithms.helpers.base_class import BaseClassForAlgoritms
import numpy as np
import scipy.stats
import math


class PART(BaseClassForAlgoritms):
    def __init__(self, inputFileName):
        super().__init__(inputFileName)

    def _check_criterion_core(self):
        d = 10
        k = 4
        self.inputData = [math.floor(x * d) % d for x in self.inputData]
        self.apply_partition_criterion(d, k)

    def apply_partition_criterion(self, d, k):
        n = len(self.inputData) // k
        counts = {i: 0 for i in range(1, k + 1)}
        for i in range(n):
            group = self.inputData[i * k:(i + 1) * k]
            unique_count = len(np.unique(group))
            counts[unique_count] += 1

        probs = {r: self.calculate_probability(r, k, d) for r in range(1, k + 1)}
        chi_squared = sum(((counts[r] - n * probs[r]) ** 2) / (n * probs[r]) for r in counts if n * probs[r] > 0)

        crit = round(scipy.stats.chi2.ppf(1 - 0.05, k - 1), 3)
        countArray = []
        for count in counts.values():
            countArray.append(np.round(count, 4))

        pobsArray = []
        for prob in probs.values():
            pobsArray.append(np.round(prob, 4))

        print(f"Подсчет числа групп 𝑘 из 𝑙 последовательных чисел, которые содержат точно 𝑟 различных чисел: "
              f"{countArray}.")
        print(f"Вероятности того, что группа из 𝑘 элементов содержит ровно 𝑟 различных элементов: {pobsArray}")
        print(f"k:{k}")
        print(f"хи-квадрат: {chi_squared}")
        print(f"Критическое значение хи-квадрат: {crit}")
        if chi_squared < crit:
            print(f"ППСЧ удовлетворяет критерию разбиений")
        else:
            print(f"ППСЧ не удовлетворяет критерию разбиений")

    def calculate_probability(self, r, k, d):
        stirling_numbers = self.stirling_second_kind(k, r)
        numerator = math.prod(range(d, d - r, -1))
        probability = (numerator / (d ** k)) * stirling_numbers
        return probability

    def stirling_second_kind(self, n, k):
        if n == k == 0:
            return 1
        if n == 0 or k == 0:
            return 0
        if k > n:
            return 0
        return k * self.stirling_second_kind(n - 1, k) + self.stirling_second_kind(n - 1, k - 1)
