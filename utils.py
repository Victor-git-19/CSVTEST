import csv
from typing import List, Dict


def read_csv(file_path: str) -> List[Dict[str, str]]:
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data
