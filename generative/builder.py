from abc import abstractmethod, ABC


class Builder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_column(self) -> None:
        pass

    @abstractmethod
    def produce_arch(self) -> None:
        pass

    @abstractmethod
    def produce_window(self) -> None:
        pass


class GothicConcreteBuilder(Builder):


    def __init__(self) -> None:

        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> 'Product':

        product = self._product
        self.reset()
        return product

    def produce_column(self) -> None:
        self._product.add("Creates column in gothic style")

    def produce_arch(self) -> None:
        self._product.add("Creates arch in gothic style")

    def produce_window(self) -> None:
        self._product.add("Creates window in gothic style")


class ModernConcreteBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> 'Product':

        product = self._product
        self.reset()
        return product

    def produce_column(self) -> None:
        self._product.add("Creates column in modern style")

    def produce_arch(self) -> None:
        self._product.add("Creates arch in modern style")

    def produce_window(self) -> None:
        self._product.add("Creates window in modern style")


class BaroqueConcreteBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> 'Product':
        product = self._product
        self.reset()
        return product

    def produce_column(self) -> None:
        self._product.add("Creates column in baroque style")

    def produce_arch(self) -> None:
        self._product.add("Creates arch in baroque style")

    def produce_window(self) -> None:
        self._product.add("Creates window in baroque style")


class Product:


    def __init__(self) -> None:
        self.parts = []

    def add(self, part) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:


    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:

        self._builder = builder


    def build_minimal_viable_product(self) -> None:
        self.builder.produce_column()

    def build_full_featured_product(self) -> None:
        self.builder.produce_column()
        self.builder.produce_arch()
        self.builder.produce_window()


if __name__ == "__main__":

    director = Director()
    modern_builder = ModernConcreteBuilder()
    baroque_builder = BaroqueConcreteBuilder()
    gothic_builder = GothicConcreteBuilder()
    director.builder = gothic_builder

    print('Some gothic constructions', '\n')
    director.build_minimal_viable_product()
    gothic_builder.product.list_parts()
    print("\n")
    director.build_full_featured_product()
    gothic_builder.product.list_parts()
    print("\n")
    director.builder = baroque_builder
    print('Some baroque constructions', '\n')
    director.build_minimal_viable_product()
    baroque_builder.product.list_parts()
    print("\n")
    print('Some modern constructions', '\n')
    director.builder = modern_builder
    director.builder.produce_arch()
    director.builder.produce_window()
    modern_builder.product.list_parts()


