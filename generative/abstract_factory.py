from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def create_column(self):
        pass

    @abstractmethod
    def create_arch(self):
        pass


class GothicStyleFactory(AbstractFactory):

    def create_column(self):
        return GothicColumnProduct()

    def create_arch(self):
        return GothicArchProduct()


class RomanStyleFactory(AbstractFactory):

    def create_column(self):
        return RomanColumnProduct()

    def create_arch(self):
        return RomanArchProduct()


class AbstractColumnProduct(ABC):

    @abstractmethod
    def create_column_func(self) -> str:
        pass


class GothicColumnProduct(AbstractColumnProduct):
    def create_column_func(self) -> str:
        return "Gothic column was created."


class RomanColumnProduct(AbstractColumnProduct):
    def create_column_func(self) -> str:
        return "Roman column was created."


class AbstractArchProduct(ABC):

    @abstractmethod
    def create_arch_func(self) -> None:
        pass


class GothicArchProduct(AbstractArchProduct):
    def create_arch_func(self) -> str:
        return "Gothic arch was created."


class RomanArchProduct(AbstractArchProduct):
    def create_arch_func(self) -> str:
        return "Roman arch was created."


def client_code(factory: AbstractFactory) -> None:
    product_column = factory.create_column()
    product_arch = factory.create_arch()
    print(f"{product_column.create_column_func()}")
    print(f"{product_arch.create_arch_func()}")


if __name__ == "__main__":
    client_code(RomanStyleFactory())
    client_code(GothicStyleFactory())
