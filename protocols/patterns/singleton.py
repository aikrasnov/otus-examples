class Sigleton:
    foo = 1
    bar = 2


# TODO: разобрать
def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class MyClass:
    pass

class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

class MyClassSecond(Singleton):
    pass

# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python