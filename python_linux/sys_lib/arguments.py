import sys
print("list: ", sys.argv)

for i in range(len(sys.argv)):
    print(f"{i}. argument: {sys.argv[i]} {type(sys.argv[i])}")
