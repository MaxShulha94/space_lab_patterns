from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class UnderwearComponent(Component):
    def operation(self):
        return "Underwear type of cloth"


class Decorator(Component):
    def __init__(self, cloth: Component):
        self._cloth = cloth

    @abstractmethod
    def operation(self):
        pass


class ConcreteDecoratorOuterwear(Decorator):
    def operation(self):
        return f"Wearing outerwear type of cloth, on {self._cloth.operation()}"


class ConcreteDecoratorMiddle(Decorator):
    def operation(self):
        return f"Wearing middle type of cloth, on {self._cloth.operation()}"


if __name__ == "__main__":
    underwear_component = UnderwearComponent()
    print(underwear_component.operation())

    spring_wearing = ConcreteDecoratorMiddle(underwear_component)
    print(spring_wearing.operation())

    winter_wearing = ConcreteDecoratorOuterwear(spring_wearing)
    print(winter_wearing.operation())
