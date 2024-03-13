from abc import ABC, abstractmethod


class Figure:

    def __init__(self, implementation: 'Color') -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return f"{self.implementation.operation_implementation()}"


class Circle(Figure):

    def __init__(self, implementation: 'Color') -> None:
        super().__init__(implementation)
        self.implementation = implementation

    def operation(self) -> str:
        return f"This is {self.implementation.operation_implementation()} circle"


class Triangle(Figure):

    def __init__(self, implementation: 'Color') -> None:
        super().__init__(implementation)
        self.implementation = implementation

    def operation(self) -> str:
        return f"This is {self.implementation.operation_implementation()} triangle"


class Color(ABC):

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class WhiteColor(Color):
    def operation_implementation(self) -> str:
        return "white"


class RedColor(Color):
    def operation_implementation(self) -> str:
        return "red"


def client_code(abstraction: Figure) -> None:

    print(abstraction.operation(), end="")


if __name__ == "__main__":


    implementation = WhiteColor()
    abstraction = Triangle(implementation)
    client_code(abstraction)

    print("\n")

    implementation = RedColor()
    abstraction = Circle(implementation)
    client_code(abstraction)

    print("\n")

    implementation = RedColor()
    abstraction = Triangle(implementation)
    client_code(abstraction)
