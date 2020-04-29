import sys

print("Coming through stdout")
save_stdout = sys.stdout

fd = open("test.txt","w")

sys.stdout = fd
print("This line goes to test.txt")

sys.stdout = save_stdout
fd.close()
print("done")
