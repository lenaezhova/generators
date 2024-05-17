from algorithms.helpers.base_class import BaseClassForAlgoritms

def display_conflicts(conflicts_info):
    if len(conflicts_info) == 0:
        print(f"ППСЧ не удовлетворяет критерию конфликтов")
    else:
        print(f"ППСЧ удовлетворяет критерию конфликтов")
        scale_d, factor_m, m_val, n, conflict_count = conflicts_info[0]
        print(f"Кол-во возникших конфликтов: {conflict_count}")
        print(f"Множитель для m: {factor_m}.")
        print(f"n: {n}.")
        print(f"m: {m_val}.")
        print(f"d: {scale_d}.")


class CON(BaseClassForAlgoritms):
    def __init__(self, file_input):
        super().__init__(file_input)

    def _check_criterion_core(self):
        self.analyze_conflicts(self.inputData)

    def analyze_conflicts(self, sequence):
        valid_results = []
        for dim in range(8, 20 + 1):
            n = len(sequence) // dim
            for scale_d in range(2, 8 + 1):
                scaled_seq = [int(x * scale_d) for x in sequence]
                unique_words, conflict_count = set(), 0
                for i in range(n):
                    word = tuple(scaled_seq[i * dim:(i + 1) * dim])
                    if word in unique_words:
                        conflict_count += 1
                    else:
                        unique_words.add(word)
                for factor_m in range(16, 128 + 1):
                    m_val = n * factor_m
                    probabilities = [0] * (n + 1)
                    probabilities[1] = current_max = current_min = 1

                    for index in range(1, n):
                        current_min += 1
                        for jj in range(current_min, current_max - 1, -1):
                            fraction = jj / m_val
                            probabilities[jj] = fraction * probabilities[jj] + (1 + 1 / m_val - fraction) * \
                                                probabilities[
                                                    jj - 1]
                            if probabilities[jj] < 1e-20:
                                probabilities[jj] = 0
                                if jj == current_min:
                                    current_min -= 1
                                    continue
                                if jj == current_max:
                                    current_max += 1

                    p, t, jindex = 0, 0, current_max - 1
                    conflict_thresholds = []
                    while t != len(self.table) - 1:
                        while p <= self.table[t] and jindex < n:
                            jindex += 1
                            p += probabilities[jindex] if jindex < len(probabilities) else 0
                        conflict_thresholds.append((n - jindex - 1, round(1 - p, 3)))
                        t += 1
                    conflict_prob = conflict_thresholds
                    if conflict_count > 0 and conflict_prob[-3][0] <= conflict_count <= conflict_prob[2][0]:
                        valid_results.append((scale_d, factor_m, m_val, n, conflict_count))

        display_conflicts(valid_results)
