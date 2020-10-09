file = open('example.txt', 'r')

# чтение всего файла
# print(file.read())

# количество символов
# print(file.read(20))
# file.seek(0)
# print(file.read(20))
#
# построчно
# print(file.readline())
# print(file.readline())
#
# список
# print(file.readlines())
#
# построчно
for item in file:
    print(item)

# Не забыть рассказать, почему важно закрывать
file.close()
