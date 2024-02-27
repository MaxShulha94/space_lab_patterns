from abc import abstractmethod, ABC


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: 'Handler') -> 'Handler':
        pass

    @abstractmethod
    def handle(self, request) -> str:
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: None) -> str | None:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class CatHandler(AbstractHandler):
    def handle(self, request: None) -> str:
        if request == "Cat":
            return f"{request} say 'meow!'"
        else:
            return super().handle(request)


class CowHandler(AbstractHandler):
    def handle(self, request: None) -> str:
        if request == "Cow":
            return f"{request} say 'moo!'"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: None) -> str:
        if request == "Dog":
            return f"{request} say 'bark'!"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:

    for animal in ["Cat", "Dog", "Cow"]:

        result = handler.handle(animal)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {animal} said nothing.", end="")


if __name__ == "__main__":
    cat = CatHandler()
    cow = CowHandler()
    dog = DogHandler()

    cat.set_next(cow).set_next(dog)

    print("Chain: Cat > Dog > Cow")
    client_code(cat)
    print("\n")

    print("Subchain: Dog > Cow")
    client_code(cow)
