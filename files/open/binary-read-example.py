import pickle


# Показать что будет если Foo не объявлен в этом пространстве
class Foo():
    pass

binary_file = open("pickled_foo.binary", "rb")
pickled_foo = pickle.load(binary_file)

print("unpickled foo num is: ", pickled_foo.bar)

binary_file.close()
