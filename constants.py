import operator

OPERATORS = {
    '>': operator.gt,
    '<': operator.lt,
    '=': operator.eq,
}


AGG_FUNCTIONS = {
    'avg': lambda numbers: sum(numbers) / len(numbers) if numbers else None,
    'min': min,
    'max': max,
}
