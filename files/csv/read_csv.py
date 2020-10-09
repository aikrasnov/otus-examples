import csv
from csv import DictReader

with open('foo.csv') as f:
    reader = csv.reader(f)

    # Извлекаем заголовок
    header = next(reader)

    # Итерируемся по данным делая из них словари
    for row in reader:
        print(dict(zip(header, row)))


print('\n\n\n\n\n\n\n\n\n\n')
print("######")
print('\n\n\n\n\n\n\n\n\n\n')


with open('foo.csv') as f:
    reader = DictReader(f)

    # Итерируемся по данным делая из них словари
    for row in reader:
        print(row)
