from abc import ABC, abstractmethod


class TransportFactory(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Transport {product.operation()} was created!"

        return result


class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class JetFactory(TransportFactory):
    def factory_method(self) -> Product:
        return JetProduct()


class MotoFactory(TransportFactory):
    def factory_method(self) -> Product:
        return MotoProduct()


class JetProduct(Product):
    def operation(self) -> str:
        return "Horten Ho 229"


class MotoProduct(Product):
    def operation(self) -> str:
        return "Yamaha SR400"


def client_code(creator: TransportFactory) -> None:
    print(f"Factory is working!.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    client_code(JetFactory())
    print("\n")
    client_code(MotoFactory())
