# python3 rnc.py /d:st /p1:0 /p2:100 /f:base.dat
# python3 rnc.py /d:tr /p1:0 /p2:100 /f:base.dat
# python3 rnc.py /d:ex /p1:0 /p2:100 /f:base.dat
# python3 rnc.py /d:nr /p1:0 /p2:100 /f:base.dat
# python3 rnc.py /d:gm /p1:0 /p2:100 /p3:2 /f:base.dat
# python3 rnc.py /d:ln /p1:0 /p2:10 /f:base.dat
# python3 rnc.py /d:ls /p1:0 /p2:100 /f:base.dat
# python3 rnc.py /d:bi /p1:50 /p2:0.5 /f:base.dat

import sys
from algorithms.st import ST as stAlgorithmClass
from algorithms.tr import TR as trAlgorithmClass
from algorithms.ex import EX as exAlgorithmClass
from algorithms.nr import NR as nrAlgorithmClass
from algorithms.gm import GM as gmAlgorithmClass
from algorithms.ln import LN as lnAlgorithmClass
from algorithms.ls import LS as lsAlgorithmClass
from algorithms.bi import BI as biAlgorithmClass
from algorithms.helpers import helpers


def st(inputFilename, p1, p2):
    newST = stAlgorithmClass(inputFilename, p1, p2)
    newST.generate_sequence()
    newST.write_sequence_in_file()


def tr(inputFilename, p1, p2):
    newTR = trAlgorithmClass(inputFilename, p1, p2)
    newTR.generate_sequence()
    newTR.write_sequence_in_file()


def ex(inputFilename, p1, p2):
    newEX = exAlgorithmClass(inputFilename, p1, p2)
    newEX.generate_sequence()
    newEX.write_sequence_in_file()


def nr(inputFilename, p1, p2):
    newNR = nrAlgorithmClass(inputFilename, p1, p2)
    newNR.generate_sequence()
    newNR.write_sequence_in_file()


def gm(inputFilename, p1, p2, p3):
    newGM = gmAlgorithmClass(inputFilename, p1, p2, p3)
    newGM.generate_sequence()
    newGM.write_sequence_in_file()


def ln(inputFilename, p1, p2):
    newLN = lnAlgorithmClass(inputFilename, p1, p2)
    newLN.generate_sequence()
    newLN.write_sequence_in_file()


def ls(inputFilename, p1, p2):
    newLS = lsAlgorithmClass(inputFilename, p1, p2)
    newLS.generate_sequence()
    newLS.write_sequence_in_file()


def bi(inputFilename, p1, p2):
    newBI = biAlgorithmClass(inputFilename, p1, p2)
    newBI.generate_sequence()
    newBI.write_sequence_in_file()


def main():
    args = helpers.parse_args(sys.argv[1:])  # Передаем аргументы без имени скрипта
    method = args.get('d').lower() if 'd' in args else None
    inputFileName = args.get('f')
    p1 = args.get('p1')
    p2 = args.get('p2')

    if not method:
        method = 'st'

    if not inputFileName:
        inputFileName = 'default.dat'

    if not p1:
        p1 = 0

    if not p2:
        p2 = 100

    p1, p2 = float(p1), float(p2)

    print("python3 rnc.py /d:bi /p1:0 /p2:100 /f:base.dat")
    if method == "st":
        st(inputFileName, p1, p2)
    elif method == "tr":
        tr(inputFileName, p1, p2)
    elif method == "ex":
        ex(inputFileName, p1, p2)
    elif method == "nr":
        nr(inputFileName, p1, p2)
    elif method == "gm":
        p3 = args.get('p3')
        p3 = float(p3)
        gm(inputFileName, p1, p2, p3)
    elif method == "ln":
        ln(inputFileName, p1, p2)
    elif method == "ls":
        ls(inputFileName, p1, p2)
    elif method == "bi":
        bi(inputFileName, p1, p2)
    else:
        print("Неизвестный метод:", method)

    if 'h' in args:
        print("Доступные методы и параметры:")
        print("/f:<имя_файла> - имя файла с входной последовательностью.")
        print("/d:<распределение> - код распределения для преобразования последовательности")
        print("Распределение: st, tr, ex, nr, gm, ln, ls, bi")
        print("/p1:<параметр1> - 1-й параметр, необходимый, для генерации ПСЧ заданного распределения")
        print("/p2:<параметр2> - 2-й параметр, необходимый, для генерации ПСЧ заданного распределения")
        print("/p3:<параметр3> - 3-й параметр, необходимый, для генерации ПСЧ гамма-распределением")


if __name__ == "__main__":
    main()
