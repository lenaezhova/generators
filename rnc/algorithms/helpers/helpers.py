import random

def parse_args(args):
    parsed_args = {}
    for arg in args:
        if arg.startswith('/'):
            key, value = arg[1:].split(':', 1)
            parsed_args[key] = value
    return parsed_args

def write_numbers_to_file(numbers, file_name):
    # Преобразование всех чисел в строки для записи в файл
    number_strings = [str(number) for number in numbers]

    # Запись чисел в файл, разделяя их переводом строки
    with open(file_name, 'w') as f:
        f.write(','.join(number_strings))

