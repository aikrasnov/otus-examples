import sys

print(sys.argv)
print(sys.executable)
print(sys.path)
sys.path.append("/path/to/my/module")
print(sys.path)
print(sys.platform)
os = sys.platform
if os == "win32":
    pass
elif os.startswith('linux'):
    pass
sys.exit(0)
