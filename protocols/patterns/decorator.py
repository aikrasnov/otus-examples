# Декоратор -- это не встроенная особенность питона, а паттерн проектирования доступный в любом ЯП. В питоне есть удобный синтаксис, чтобы немного упростить работу с декораторами. Суть этого паттерна в оборачивании функции, другой функцией. 

# Например, 

def deco(fn):  # функция-декоратор получает как аргумент декорируюемую функцию.
    def wrapper(*args, **kwargs):  # функция-обертка, получает аргументы который предназначенны декорируемомой функции.
        print('Hello from deco!')
        return fn(*args, **kwargs)
    return wrapper # возвращаем обертку, которая будет вызываться вместо декорируемой функции


def foo(): 
    print('Hello from foo!')


decorated_foo = deco(foo) # применяем декоратор
print(decorated_foo) # <function deco.<locals>.wrapper at 0x7f4242942158> в decorated_foo сохранен wrapper из deco, который вызывает foo
decorated_foo() # вызываем декорируемую версию foo, напечатает Hello from deco!, и затем Hello from foo!


# Единственное, что делает @ позволяет не писать явно
decorated_foo = deco(foo)

# А сделать это автоматически.
@deco
def foo():
    pass

# @ просто вызовет функцию deco с аргументом foo.
# В качестве декоратора можно использовать любой callable объект
class ClassDeco:
    def __call__(self, fn):
        print('Hello from ClassDeco!')
        return fn

@ClassDeco() # @ требует инстанса, а не класса. Иначе foo будет передан в __init__, а не __call__. 
def foo():
    print('Hello from foo!')

foo()


# Чтобы передать в декоратор аргументы, нужно добавить еще одну функцию. Функция будет принимать аргументы, сохранять их, и возвращать функцию, которая принимает функцию, и возвращает обертку.
def deco_with_args(bar): # аргументы декоратора
    def deco(fn): # декоратор
        def wrapper(*args, **kwargs): # функция-обертка
           print(f'Hello from deco with bar: {bar}')
           return fn(*args, **kwargs)
        return wrapper
    return deco


def another_foo():
    print('Hello from another_foo')

decorated_foo = deco_with_args("lolkek")(another_foo) # сначала передаем аругменты в deco_with_args, затем функцию в deco
print(decorated_foo) # <function deco_with_args.<locals>.deco.<locals>.wrapper at 0x7f0c74b83d40>
decorated_foo() 
# напечатает
# Hello from deco with bar: lolkek
# Hello from another_foo


# Так же можно сделать и с @
@deco_with_args('Cheburek') # тут после имени функции нужно будет добавить () и аргументы
def foo():
    print('Hello from foo with Cheburek!')

foo()

# Hello from deco with bar: Cheburek
# Hello from foo with Cheburek!
