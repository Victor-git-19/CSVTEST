# CSV Parser

Cкрипт для обработки CSV-файла

## Возможности

- Фильтрация по значениям колонок (>, <, =)
- Агрегация числовых колонок (`avg`, `min`, `max`)
- Удобный вывод таблицы через [`tabulate`](https://pypi.org/project/tabulate/)
- Простое расширение (новые операции фильтрации, агрегации, сортировки и т.д.)
- Покрытие тестами (`pytest`)

## Установка

```bash
git clone https://github.com/Victor-git-19/CSVTEST.git
cd CSVTEST
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
