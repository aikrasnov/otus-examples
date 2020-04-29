import sys

print("argv: ", sys.argv)
print("executable", sys.executable)
print("path: ", sys.path)
print('\n\n\n')

sys.path.append("/path/to/my/module")
print('\n\n\n')
print("updated path", sys.path)
print('\n\n\n')

print("platform: ", sys.platform)


if sys.platform == "win32":
    pass
elif sys.platform.startswith('linux'):
    pass

sys.exit(0)
