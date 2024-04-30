from algorithms.helpers.base_class import BaseClassForAlgoritms


class MT(BaseClassForAlgoritms):
    def __init__(self, module, seed):
        super().__init__()
        self.mt = [0] * 624
        self.index = 624
        self.module = module
        self.mt[0] = seed & 0xffffffff

        for i in range(1, 624):
            self.mt[i] = (0x6c078965 * (self.mt[i - 1] ^ (self.mt[i - 1] >> 30)) + i) & 0xffffffff

    def extract_number(self):
        if self.index >= 624:
            for i in range(624):
                x = (self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7fffffff)
                xA = x >> 1
                if x % 2 != 0:
                    xA ^= 0x9908b0df
                self.mt[i] = self.mt[(i + 397) % 624] ^ xA
            self.index = 0

        y = self.mt[self.index]
        y ^= (y >> 11)
        y ^= ((y << 7) & 0x9d2c5680)
        y ^= ((y << 15) & 0xefc60000)
        y ^= (y >> 18)

        self.index += 1
        self.put_in_results(y & 0xffffffff)
        return y & 0xffffffff

    def _generate_sequence_core(self, count):
        self.results = [self.extract_number() % self.module for _ in range(count)]
        self.results = self.results[-count:]
        self.get_results_info()
