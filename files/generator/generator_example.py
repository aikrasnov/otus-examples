def squares(start, stop):
    for i in range(start, stop):
        value = yield i * i
        print("passed to generator", value)


foo = squares(1, 5)

print("\n")
print("squares() type is", type(squares))
print("foo type is", type(foo))

# print(next(foo))
# print(next(foo))
# print(next(foo))
#
# foo.send("bar")

# показать дефолт
# next(foo)
# next(foo)
# next(foo)
# next(foo)
# next(foo)

for i in foo:
    print(i)
