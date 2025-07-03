import argparse
from tabulate import tabulate
from typing import List, Dict

from constants import OPERATORS, AGG_FUNCTIONS
from utils import read_csv


def parse_filter(filter_str: str):
    for op in OPERATORS:
        if op in filter_str:
            field, value = filter_str.split(op)
            return field.strip(), OPERATORS[op], value.strip()
    raise ValueError('Недопустимый формат фильтра!')


def apply_filter(data: List[Dict[str, str]],
                 field: str, op_func, value: str) -> List[Dict[str, str]]:
    filtered = []
    for row in data:
        cell_value = row.get(field)
        if cell_value is None:
            continue

        try:
            cell_value = float(cell_value)
            value = float(value)
        except ValueError:
            pass
        if op_func(cell_value, value):
            filtered.append(row)
    return filtered


def main():
    parser = argparse.ArgumentParser(description='CSV Processor')
    parser.add_argument('file', help='Path to CSV file')
    parser.add_argument('--filter', help='Filter condition, e.g. price>500')
    args = parser.parse_args()

    data = read_csv(args.file)

    if args.filter:
        try:
            field, op_func, value = parse_filter(args.filter)
            data = apply_filter(data, field, op_func, value)
        except ValueError as e:
            print(f'Ошибка фильтрации: {e}')
            return

    if data:
        print(tabulate(data, headers='keys', tablefmt='grid'))
    else:
        print('File is emty!')


if __name__ == '__main__':
    main()
