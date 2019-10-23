import sys

save_stderr = sys.stderr
fd = open("errors.txt", "w")
sys.stderr = fd

x = 10 / 0

# return to normal:
sys.stderr = save_stderr

fd.close()
