from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class Leaf(Component):
    def __init__(self, name: str):
        self.name = name

    def operation(self):
        print(f"{self.name}")


class Composite(Component):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, component: Component):
        self.children.append(component)

    def remove(self, component: Component):
        self.children.remove(component)

    def operation(self):
        print(f"{self.name} info: ")
        for child in self.children:
            child.operation()


# Usage example:
if __name__ == "__main__":
    leaf1 = Leaf("Student 1")
    leaf2 = Leaf("Student 2")
    leaf3 = Leaf("Teacher 1")
    leaf4 = Leaf("Teacher 2")
    leaf5 = Leaf("Director")

    composite = Composite("School")
    composite.add(leaf1)
    composite.add(leaf2)
    composite.add(leaf3)
    composite.add(leaf4)
    composite.add(leaf5)

    composite.operation()
