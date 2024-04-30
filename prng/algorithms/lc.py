from algorithms.helpers.base_class import BaseClassForAlgoritms


class LC(BaseClassForAlgoritms):
    def __init__(self, m, a, c, X0):
        super().__init__()
        self.m = m  # модуль
        self.a = a  # множитель
        self.c = c  # приращение
        self.X0 = X0  # начальное значение

    def validate_input(self):
        if self.m <= 0:
            print("m должно быть больше 0")
            return False

        if not (0 <= self.a <= self.m and 0 <= self.c <= self.m and 0 <= self.X0 <= self.m):
            print("a, c, X0 должны соответствовать следующему условию: 0 <= a | c | X0 <= m")
            pass
            return False

        return True

    def _generate_sequence_core(self, count):
        if not self.validate_input():
            return

        Xprev = self.X0
        for i in range(count):
            self.put_in_results(Xprev)
            Xprev = (self.a * Xprev + self.c) % self.m
