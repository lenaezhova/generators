from algorithms.helpers.base_class import BaseClassForAlgoritms


class RSA(BaseClassForAlgoritms):
    def __init__(self, n, e, x_0, w):
        super().__init__()
        self.n = n
        self.e = e
        self.x = x_0
        self.w = w

    def _generate_sequence_core(self, count):
        for _ in range(count):
            self.x = pow(self.x, self.e, self.n)
            z_i = self.x & ((1 << self.w) - 1)
            self.put_in_results(z_i)
