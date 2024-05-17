from algorithms.helpers.base_class import BaseClassForAlgoritms
import scipy.stats as ss


class MON(BaseClassForAlgoritms):
    def __init__(self, inp_file):
        super().__init__(inp_file)

    def _check_criterion_core(self):
        dta = {}
        ix = 0

        m = 1
        while ix < len(self.inputData) - 1:
            if self.inputData[ix] < self.inputData[ix + 1]:
                m += 1
            else:
                dta[m] = dta.get(m, 0) + 1
                m, ix = 1, ix + 1
            ix += 1

        n = len(dta)
        crit_val = round(ss.chi2.ppf(1 - 0.05, n), 3)

        Ej = []

        count = 1
        for i in range(1, n + 1):
            count *= i
            Ej.append(round(1 / count - 1 / (count * (i + 1)), 4))

        t_vals = sum(dta.values())
        Ej = [round(t_vals * Ej[j], 3) for j in range(n)]

        chi_val = round(sum(((dta[j + 1] - Ej[j]) ** 2) / Ej[j] for j in range(n)), 3)

        print(f"Ej: {Ej}.")
        print(f"k: {n + 1}")
        print(f"хи-квадрат: {chi_val}.")
        print(f"Критическое значение хи-квадрат: {crit_val}.")
        if chi_val < crit_val:
            print(f"ППСЧ удовлетворяет критерию монотонности")
        else:
            print(f"ППСЧ не удовлетворяет критерию монотонности")
