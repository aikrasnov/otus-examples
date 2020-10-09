import time

file = open('example.txt', 'w')
# time.sleep(20)

file.write("This is from write-example!\n")
file.writelines(["\nthis", "is", "multiline\n"])

# Не забыть рассказать, почему важно закрывать
file.close()