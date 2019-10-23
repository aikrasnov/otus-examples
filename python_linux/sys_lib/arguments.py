import sys
print(sys.argv)

for i in range(len(sys.argv)):
    if i == 0:
        print("Function name: %s" % sys.argv[0])

    print("%d. argument: %s" % (i, sys.argv[i]))
