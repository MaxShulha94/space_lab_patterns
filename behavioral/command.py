from abc import abstractmethod, ABC


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class TurnOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class TurnOffCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class Light:

    def turn_on(self):
        print("Light turned on")

    def turn_off(self):
        print("Light turned off")


class LightSwitch:

    def execute_command(self, command):
        command.execute()


if __name__ == "__main__":
    light = Light()
    turn_on_command = TurnOnCommand(light)
    turn_off_command = TurnOffCommand(light)
    light_switch = LightSwitch()

    light_switch.execute_command(turn_on_command)
    light_switch.execute_command(turn_off_command)
