from algorithms.helpers.base_class import BaseClassForAlgoritms


class RC4(BaseClassForAlgoritms):
    def __init__(self, key):
        super().__init__()
        self.key = key
        self.S = list(range(256))  # Инициализация S

    def _init_S(self):
        j = 0
        for i in range(256):
            j = (j + self.S[i] + self.key[i % len(self.key)]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]

    def _generate_sequence_core(self, count):
        self._init_S()
        i = j = 0
        for _ in range(count):
            i = (i + 1) % 256
            j = (j + self.S[i]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]
            t = self.S[(self.S[i] + self.S[j]) % 256]
            self.put_in_results(t)
