import random


def parse_args(args):
    parsed_args = {}
    for arg in args:
        if arg.startswith('/'):
            key, value = arg[1:].split(':', 1)
            parsed_args[key] = value
    return parsed_args


def bit_array_conversion(input_register):
    input_register = list(map(int, str(input_register)))
    input_register.reverse()

    return input_register



def bitwise_or(fb_rev, sb_rev):
    fb_rev_s, sb_rev_s = len(fb_rev), len(sb_rev)
    min_size = min(fb_rev_s, sb_rev_s)

    return [1 if fb_rev[i] == 1 or sb_rev[i] == 1 else 0 for i in range(min_size)] + (
        fb_rev[min_size:] if fb_rev_s > sb_rev_s else sb_rev[min_size:])


def xor(fb_rev, sb_rev):
    fb_rev_s, sb_rev_s = len(fb_rev), len(sb_rev)
    min_size = min(fb_rev_s, sb_rev_s)

    return [(fb_rev[i] + sb_rev[i]) % 2 for i in range(min_size)] + (
        fb_rev[min_size:] if fb_rev_s > sb_rev_s else sb_rev[min_size:])



def handle_input_params(inp):
    return inp.split(',')


def write_numbers_to_file(numbers, file_name):
    # Преобразование всех чисел в строки для записи в файл
    number_strings = [str(number) for number in numbers]

    # Запись чисел в файл, разделяя их переводом строки
    with open(file_name, 'w') as f:
        f.write(','.join(number_strings))


def xor(first_bits, second_bits):
    min_length = min(len(first_bits), len(second_bits))
    result = [(first_bits[i] ^ second_bits[i]) for i in range(min_length)]

    if len(first_bits) > len(second_bits):
        result.extend(first_bits[min_length:])
    else:
        result.extend(second_bits[min_length:])

    return result


def funcOr(list1, list2):
    min_length = min(len(list1), len(list2))
    result = [1 if list1[i] == 1 or list2[i] == 1 else 0 for i in range(min_length)]

    if len(list1) > len(list2):
        result.extend(list1[min_length:])
    else:
        result.extend(list2[min_length:])

    return result



def generate_prime_candidate(length):
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p


def is_prime(n, k=128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Найти r и s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 0
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def generate_prime_number(length=1024):
    p = 4
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p