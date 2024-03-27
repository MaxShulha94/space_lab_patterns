from threading import Lock, Thread


class SingletonMeta(type):

    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:

            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    name = str()

    def __init__(self, name: str):
        self.name = name


def say_hello(name):
    singleton = Singleton(name)
    print(f'hello {singleton.name}!')


if __name__ == "__main__":

    say_hello('Yaroslav')
    say_hello('Oleh')
    process1 = Thread(target=say_hello, args=('Oleh',))
    process2 = Thread(target=say_hello, args=('Yaroslav',))
    process1.start()
    process2.start()
    print(SingletonMeta.__dict__)
