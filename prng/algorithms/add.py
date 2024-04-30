from algorithms.helpers.base_class import BaseClassForAlgoritms


class ADD(BaseClassForAlgoritms):
    def __init__(self, m, index_small, index_old, sequence_begin):
        super().__init__()
        self.m = m  # модуль
        self.index_small = index_small  # младший индекс
        self.index_old = index_old  # старший индекс
        self.sequence_begin = sequence_begin  # последовательность начальных значений

    def _generate_sequence_core(self, count):
        self.results = self.sequence_begin

        for i in range(count):
            self.put_in_results((self.results[self.index_old - self.index_small + i] + self.results[i]) % self.m)

        self.results = self.results[-count:]
