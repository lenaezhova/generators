import sys
import subprocess
import math
from algorithms.helpers import helpers
from algorithms.chi import CHI as chiAlgorithmClass
from algorithms.ser import SER as serAlgorithmClass
from algorithms.inter import INTER as interAlgorithmClass
from algorithms.part import PART as partAlgorithmClass
from algorithms.perm import PERM as permAlgorithmClass
from algorithms.mon import MON as monAlgorithmClass
from algorithms.con import CON as conAlgorithmClass
from algorithms.helpers.base_class import BaseClassForAlgoritms

inputFileNname = ''


def expected():
    global inputFileNname
    newClass = BaseClassForAlgoritms(inputFileNname)
    expectedValue = round(helpers.get_expected_value(newClass.inputData), 4)
    expectedError = round(helpers.get_expected_error(newClass.inputData), 4)
    print(f"Математическое ожидание: {expectedValue}")
    print(
        f"Среднеквадратичное отклонение: {expectedError}")
    print(f"Относительная погрешность математического ожидания: "
          f"{round(abs(expectedValue - 0.5) / expectedValue, 4)}")
    print(
        f"Относительная погрешность среднеквадратинчого отклонения: "
        f"{round(abs(expectedError - round(math.sqrt(1 / 12), 4)) / expectedError, 4)}")
    helpers.plot_stats(newClass.inputData, len(newClass.inputData))


def chi():
    global inputFileNname
    newCHI = chiAlgorithmClass(inputFileNname)
    newCHI.check_criterion()


def ser():
    global inputFileNname
    newSER = serAlgorithmClass(inputFileNname)
    newSER.check_criterion()


def inter():
    global inputFileNname
    newINTER = interAlgorithmClass(inputFileNname)
    newINTER.check_criterion()


def part():
    global inputFileNname
    newPART = partAlgorithmClass(inputFileNname)
    newPART.check_criterion()


def perm():
    global inputFileNname
    newPERM = permAlgorithmClass(inputFileNname)
    newPERM.check_criterion()


def mon():
    global inputFileNname
    newMON = monAlgorithmClass(inputFileNname)
    newMON.check_criterion()


def con():
    global inputFileNname
    newCON = conAlgorithmClass(inputFileNname)
    newCON.check_criterion()


def main():
    subprocess.run("printf '\033c'", shell=True)
    args = helpers.parse_args(sys.argv[1:])

    criterion = args.get('c').lower() if 'c' in args else None
    global inputFileNname
    inputFileNname = args.get('f', 'rnd.dat')

    if criterion == "chi":
        chi()
    elif criterion == "ser":
        ser()
    elif criterion == "inter":
        inter()
    elif criterion == "part":
        part()
    elif criterion == "perm":
        perm()
    elif criterion == "mon":
        mon()
    elif criterion == "con":
        con()
    else:
        expected()

    if 'h' in args:
        print("Доступные методы и параметры:")
        print("/f:<имя_файла> - имя файла с входной последовательностью")
        print("/с:<критерий> - код критерия")
        print("Доступные критерии: ")
        print("chi - критерий хи-квадрат")
        print("ser - критерий серий")
        print("inter - критерий интервалов")
        print("part - критерий разбиений")
        print("perm - критерий перестановок;")
        print("mon - критерий монотонности")
        print("con - критерий конфликтов")


if __name__ == "__main__":
    main()
