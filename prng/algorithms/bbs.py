from algorithms.helpers.base_class import BaseClassForAlgoritms


class BBS(BaseClassForAlgoritms):
    def __init__(self, p, q, x_0):
        super().__init__()
        self.n = p * q
        self.x = pow(x_0, 2, self.n)

    def _generate_sequence_core(self, count):
        for _ in range(count):
            self.x = pow(self.x, 2, self.n)
            z_i = self.x & 1
            self.put_in_results(z_i)