class SubsystemA:
    def operation_a(self) -> str:
        return "Subsystem A operation"


class SubsystemB:
    def operation_b(self) -> str:
        return "Subsystem B operation"


class SubsystemC:
    def operation_c(self) -> str:
        return "Subsystem C operation"


class Facade:
    def __init__(self) -> None:
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()
        self._subsystem_c = SubsystemC()

    def operation(self) -> str:
        results = ["Facade initializes subsystems:", self._subsystem_a.operation_a(), self._subsystem_b.operation_b(), self._subsystem_c.operation_c()]
        return "\n".join(results)


def client_code(facade: Facade) -> None:
    print(facade.operation())


if __name__ == "__main__":
    facade = Facade()
    client_code(facade)
