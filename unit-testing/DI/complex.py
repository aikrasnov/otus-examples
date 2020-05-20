# Импортируем единственный модуль.
# https://pypi.org/project/Inject/
# noinspection PyUnresolvedReferences
import inject


# Описываем опциональную конфигурацию


# noinspection PyUnresolvedReferences
def my_config(binder, CurrentUser=None):
    binder.install(my_config2)  # Импортируем другую конфигурацию
    binder.bind(Db, RedisDb('localhost:1234'))
    binder.bind_to_provider(CurrentUser, get_current_user)


# Создаем инжектор.
inject.configure(my_config)

# noinspection PyUnresolvedReferences
# Внедряем зависимости с помощью inject.instance и inject.attr
class User(object):
    db = inject.attr(Db)

    @classmethod
    def load(cls, id):
        return cls.db.load('user', id)

    def __init__(self, id):
        self.id = id

    def save(self):
        self.db.save('user', self)


# noinspection PyUnresolvedReferences
def foo(bar):
    cache = inject.instance(Cache)
    cache.save('bar', bar)


# Создаем нового пользователя и сохраняем
# во внедренную базу данных.
user = User(10)
user.save()