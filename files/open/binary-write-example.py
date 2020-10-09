import pickle
import random


class Foo():

    def __init__(self):
        self.bar = random.randint(10, 100)


foo = Foo()

pickled_foo = pickle.dumps(foo)

print("original foo num is: ", foo.bar)
print("original foo type is: ", type(foo))
print("foo pickled type is: ", type(pickled_foo))

binary_file = open("pickled_foo.binary", "wb")
binary_file.write(foo)