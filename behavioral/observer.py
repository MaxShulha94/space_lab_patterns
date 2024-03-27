class Subject:

    def __init__(self):
        self._state = None
        self._observers = []

    def attach(self, observer):

        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):

        self._observers.remove(observer)

    def notify(self):

        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):

        self._state = state
        self.notify()


class Observer:

    def update(self, state):
        pass


class ConcreteObserverA(Observer):

    def update(self, state):
        print("ConcreteObserverA: Received new state -", state)


class ConcreteObserverB(Observer):

    def update(self, state):
        print("ConcreteObserverB: Received new state -", state)


if __name__ == "__main__":
    subject = Subject()

    observer1 = ConcreteObserverA()
    observer2 = ConcreteObserverB()
    subject.attach(observer1)
    subject.attach(observer2)

    subject.set_state('Hello!')

    subject.detach(observer2)
    subject.set_state('Hello World!')

