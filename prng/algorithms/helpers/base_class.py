from algorithms.helpers import helpers


class BaseClassForAlgoritms:
    def __init__(self):
        self.results = []
        self.total_count = 0
        self.presentStep = 15
        self.last_reported_progress = -self.presentStep

    def generate_sequence(self, count):
        self.total_count = count
        print(f"Начало генерации!")
        self._generate_sequence_core(count)
        print(f"Генерация чисел завершена!")

    def _generate_sequence_core(self, count):
        raise NotImplementedError("Метод должен быть переопределен")

    def put_in_results(self, val):
        self.results.append(val)
        self.get_results_info()

    def get_results_info(self):
        current_progress = (len(self.results) / self.total_count) * 100

        if current_progress >= self.last_reported_progress + 15:
            self.last_reported_progress = int(current_progress // 15) * 15
            if self.last_reported_progress > 100:
                self.last_reported_progress = 100
            print(f"Генерация чисел: {self.last_reported_progress}%")
        return self.results

    def get_sequence(self):
        return self.results

    def write_sequence_in_file(self, fileName):
        helpers.write_numbers_to_file(self.results, fileName)
        print(f"Числа записаны в файл: {fileName}")
