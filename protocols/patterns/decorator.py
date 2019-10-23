from functools import wraps

def deco(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("simple deco here")
        return fn(*args, **kwargs)
    return wrapper


@deco
def decorated_fn():
    pass


def foo():
    pass

another_decorated_fn = deco(foo)
