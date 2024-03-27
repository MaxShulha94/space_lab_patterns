class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f'hello {self.name}!'


if __name__ == "__main__":
    s1 = Singleton('Oleh')
    s2 = Singleton('Yaroslav')
    print(s1.say_hello())
    print(s2.say_hello())
