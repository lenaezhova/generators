# python3 prng.py /g:lc /inp:10,8,9,7 /n:1000 /f:lc.dat
# python3 prng.py /g:add /inp:10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 /n:1000 /f:add.dat
# python3 prng.py /g:5r /inp:30,22,13,14,15,1,0,1,0 /n:1000 /f:5r.dat
# python3 prng.py /g:lfsr /inp:1000011111,1110111111101011100010101010,5 /n:1000 /f:lfsr.dat
# python3 prng.py /g:nfsr /inp:10111,1111011001,10111011000001,11,10111011,11111000111001,1010010101010110101011100001 /n:1000 /f:nfsr.dat
# python3 prng.py /g:mt /inp:1000,110 /n:1000 /f:mt.dat
# python3 prng.py /g:rc4 /inp:$stream /n:1000 /f:rc4.dat
# stream=$(python3 -c "import random; input=''.join([str(random.randint(1, 1024)) + ('' if i == 255 else ',') for i in range(256)]); print(input)")
#  python3 prng.py /g:rc4 /inp:$stream /n:1000 /f:rc4.dat

# python3 prng.py /g:rsa /inp:1000,31,2,3 /n:1000 /f:rsa.dat
# python3 prng.py /g:bbs /inp:1000 /n:1000 /f:bbs.dat

import sys
from algorithms.lc import LC as lcAlgorithmClass
from algorithms.add import ADD as addAlgorithmClass
from algorithms.lfsr_main import LFSR as lfsrAlgorithmClass
from algorithms.mt import MT as mtAlgorithmClass
from algorithms.rc4 import RC4 as rc4AlgorithmClass
from algorithms.rsa import RSA as rsaAlgorithmClass
from algorithms.bbs import BBS as bbsAlgorithmClass
from algorithms.helpers import helpers
from math import gcd
import random


def lc(count, filename, *input_params):
    m, a, c, X0 = map(int, input_params)
    LC = lcAlgorithmClass(m, a, c, X0)
    LC.generate_sequence(count)
    LC.write_sequence_in_file(filename)


def add(count, filename, *input_params):
    m, index_small, index_old = map(int, input_params[:3])
    sequence_init = list(map(int, input_params[3:]))
    ADD = addAlgorithmClass(m, index_small, index_old, sequence_init)
    ADD.generate_sequence(count)
    ADD.write_sequence_in_file(filename)


def fiveR(count, filename, *input_params):
    p, q1, q2, q3, w = map(int, input_params[:5])
    sequence_init = list(map(int, input_params[5:]))
    LCFRbasic = lfsrAlgorithmClass(p, w, [0, q1, q2, q3], sequence_init)
    LCFRbasic.generate_sequence(count)
    LCFRbasic.write_sequence_in_file(filename)


def lfsr(count, filename, *input_params):
    vec, init = [([int(bit) for bit in str(int(param))][::-1]) for param in input_params[:2]]
    w = int(input_params[2])
    LCFRbasic = lfsrAlgorithmClass(0, w, [i for i in range(len(vec)) if vec[i] == 1], init)
    LCFRbasic.generate_sequence(count)
    LCFRbasic.write_sequence_in_file(filename)


def nfsr(count, filename, *input_params):
    R1, R2, R3 = [([int(bit) for bit in str(int(param))][::-1]) for param in input_params[:3]]
    w = int(input_params[3])
    X1, X2, X3 = [([int(bit) for bit in str(int(param))][::-1]) for param in input_params[4:]]
    R = helpers.funcOr(helpers.funcOr(helpers.xor(R1, R2), helpers.xor(R2, R3)), R3)
    X = helpers.funcOr(helpers.funcOr(helpers.xor(X1, X2), helpers.xor(X2, X3)), X3)
    LCFRbasic = lfsrAlgorithmClass(0, w, [i for i in range(len(R)) if R[i] == 1], X)
    LCFRbasic.generate_sequence(count)
    LCFRbasic.write_sequence_in_file(filename)


def mt(count, filename, *input_params):
    m, x = map(int, input_params[:2])
    mt_instance = mtAlgorithmClass(m, x)
    mt_instance.generate_sequence(count)
    mt_instance.write_sequence_in_file(filename)


def rc4(count, filename, *input_params):
    key = list(map(int, input_params[0].split(',')))
    rc4_instance = rc4AlgorithmClass(key)
    rc4_instance.generate_sequence(count)
    rc4_instance.write_sequence_in_file(filename)


def rsa(count, filename, *input_params):
    n, e, x_0, w = map(int, input_params)
    bit_length = n.bit_length() // 2
    p = helpers.generate_prime_number(bit_length)
    q = helpers.generate_prime_number(bit_length)
    n = p * q
    f = (p - 1) * (q - 1)

    if not 1 < e < f or gcd(e, f) != 1:
        print("Значение 'e' некорректно и будет перевыбрано.")
        e = random.randrange(2, f)
        while gcd(e, f) != 1:
            e = random.randrange(2, f)
        print(e)

    if not 1 < x_0 < n:
        print(
            f"Значение 'x_0' некорректно (x_0 = {x_0}). Будет выбрано случайное значение в диапазоне от 1 до {n - 1}.")
        x_0 = random.randrange(1, n)

    rsa_instance = rsaAlgorithmClass(n, e, x_0, w)
    rsa_instance.generate_sequence(count)
    rsa_instance.write_sequence_in_file(filename)


def bbs(count, filename, *input_params):
    p = 127
    q = 131
    x_0 = int(input_params[0])

    n = p * q
    if gcd(x_0, n) != 1:
        raise ValueError(f"Начальное значение x_0 должно быть взаимно простым с n={n}.")

    bbs_instance = bbsAlgorithmClass(p, q, x_0)
    bbs_instance.generate_sequence(count)
    bbs_instance.write_sequence_in_file(filename)


def main():
    args = helpers.parse_args(sys.argv[1:])  # Передаем аргументы без имени скрипта

    input_params = helpers.handle_input_params(args['inp']) if 'inp' in args else []
    method = args.get('g').lower() if 'g' in args else None
    count = int(args.get('n', 10000))
    filename = args.get('f', 'rnd.dat')

    if method == "lc":
        lc(count, filename, *input_params)
    elif method == "add":
        add(count, filename, *input_params)
    elif method == "5r":
        fiveR(count, filename, *input_params)
    elif method == "lfsr":
        lfsr(count, filename, *input_params)
    elif method == "nfsr":
        nfsr(count, filename, *input_params)
    elif method == "mt":
        mt(count, filename, *input_params)
    elif method == "rc4":
        rc4(count, filename, *input_params)
    elif method == "rsa":
        rsa(count, filename, *input_params)
    elif method == "bbs":
        bbs(count, filename, *input_params)
    else:
        print("Неизвестный метод:", method)

    if 'h' in args:
        print("Доступные методы и параметры:")
        print("lc, add, br, lfsr, nfsr, mt, rc4, rsa, bbs")
        print("Используйте /n для указания количества чисел и /f для имени файла.")


if __name__ == "__main__":
    main()
