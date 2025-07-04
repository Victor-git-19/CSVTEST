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


def parse_agg(agg_str: str):
    if '=' not in agg_str:
        raise ValueError('Агрегация должна быть в формате колонка=операция')
    column, op = agg_str.split('=')
    column = column.strip()
    op = op.strip().lower()
    if op not in AGG_FUNCTIONS:
        raise ValueError(
            f"Поддерживаемые операции агрегации: {', '.join(AGG_FUNCTIONS)}")
    return column, AGG_FUNCTIONS[op]


def apply_agg(data: List[Dict[str, str]], column: str, agg_func):
    numbers = []
    for row in data:
        val = row.get(column)
        if val is None:
            continue
        try:
            numbers.append(float(val))
        except ValueError:
            pass
    if not numbers:
        return None
    return agg_func(numbers)


def main():
    parser = argparse.ArgumentParser(description='Обработчик CSV файлов')
    parser.add_argument('--file', help='Путь к CSV файлу')
    parser.add_argument('--where',
                        help='Условие фильтрации, например price>500')
    parser.add_argument('--aggregate',
                        help='Агрегация в формате колонка=операция')
    args = parser.parse_args()

    try:
        data = read_csv(args.file)
    except FileNotFoundError:
        print(f"Ошибка: файл '{args.file}' не найден.")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    if args.where:
        try:
            field, op_func, value = parse_filter(args.where)
            data = apply_filter(data, field, op_func, value)
        except ValueError as e:
            print(f'Ошибка фильтрации: {e}')
            return

    if args.aggregate:
        try:
            column, agg_func = parse_agg(args.aggregate)
            result = apply_agg(data, column, agg_func)
            if result is None:
                print(
                    f"Нет числовых данных для агрегации по колонке '{column}'")
                return
            table = [{f"{column}_{args.aggregate.split('=')[1]}": result}]
            print(tabulate(table, headers="keys", tablefmt="grid"))
        except ValueError as e:
            print(f"Ошибка агрегации: {e}")
        return

    if data:
        print(tabulate(data, headers='keys', tablefmt='grid'))
    else:
        print('Файл пуст!')


if __name__ == '__main__':
    main()
