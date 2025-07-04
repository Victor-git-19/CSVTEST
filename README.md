# CSV Parser

Cкрипт для обработки CSV-файла

## Возможности

- Фильтрация по значениям колонок (>, <, =)
- Агрегация числовых колонок (`avg`, `min`, `max`)
- Удобный вывод таблицы через (`tabulate`)
- Простое расширение (новые операции фильтрации, агрегации, сортировки и т.д.)
- Покрытие тестами (`pytest`)

## Установка

```bash
git clone https://github.com/Victor-git-19/CSVTEST.git
cd CSVTEST
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Запуск

```bash
# Запуск с обязательным указанием файла CSV
python main.py path/to/data.csv

# Запуск с фильтрацией (например, выбрать товары с ценой больше 500)
python main.py data.csv --filter "price>500"

# Запуск с агрегацией (например, среднее значение цены)
python main.py data.csv --agg "price=avg"

# Совместное использование фильтрации и агрегации (минимальная цена среди товаров бренда xiaomi)
python main.py data.csv --filter "brand=xiaomi" --agg "price=min"
```