import subprocess
import time

# nothing
# p1 = subprocess.Popen(['ping', '-c 2', "ya.ru"])
# print("Команда запущена!")
# time.sleep(2)
# output = p1.communicate()
# print(output)

# time.sleep(30)
# print("\n\n\n\n####\n\n\n\n")
#
# # stdout
# file = open("result.txt", "wb")
# p2 = subprocess.Popen(['ping', '-c 2', "ya.ru"], stdout=file)
# print("Команда запущена!")
# output = p2.communicate()
# print(output)
#
#
# time.sleep(30)
# print("\n\n\n\n####\n\n\n\n")
#
# # stderr
# p3 = subprocess.Popen(['ping', '-c 2', "foo.bar.ru"], stdout=subprocess.PIPE)
# print("Команда запущена!")
# output = p3.communicate()
# print(output)
#
#
# # stderr -- 2
# time.sleep(30)
# print("\n\n\n\n####\n\n\n\n")

p4 = subprocess.Popen(['ping', '-c 2', "foo.bar.ru"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("Команда запущена!")
output = p4.communicate()
print(output)
