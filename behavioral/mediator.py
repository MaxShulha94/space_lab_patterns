class Mediator:
    def send(self, message, sender):
        pass


class Chat(Mediator):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send(self, message, sender):
        for user in self.users:
            if sender == user:
                user.receive(message, sender)


class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send(self, message):
        self.mediator.send(message, self)

    def receive(self, message, sender):
        print(f"{sender}: {message}")

    def __str__(self):
        return f"{self.name}"


chat_room = Chat()

user1 = User("Pavlo", chat_room)
user2 = User("Borys", chat_room)
user3 = User("Alex", chat_room)

chat_room.add_user(user1)
chat_room.add_user(user2)
chat_room.add_user(user3)

user1.send("Hi everyone!")
user2.send("Hello, World!")
user3.send("Hey there!")
