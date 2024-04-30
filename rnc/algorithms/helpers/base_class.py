from algorithms.helpers import helpers


class BaseClassForAlgoritms:
    def __init__(self, code, p1, p2, p3, inputFileName, showLogs):
        self.code = code
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.inputData = []
        self.results = []
        self.showLogs = showLogs
        self.initInputData(inputFileName)

    def initInputData(self, inputFileName):
        f = open(inputFileName, "r")
        self.inputData = list(map(int, (f.read()).split(',')))

    def generate_sequence(self):
        if self.showLogs:
            print(f"Начало генерации!")

        self._generate_sequence_core()

        if self.showLogs:
            print(f"Генерация завершена!")

    def _generate_sequence_core(self):
        raise NotImplementedError("Метод должен быть переопределен")

    def get_sequence(self):
        return self.results

    def write_sequence_in_file(self):
        fileName = 'distr-' + self.code + '.dat'
        helpers.write_numbers_to_file(self.results, fileName)
        print(f"Числа записаны в файл: {fileName}")
