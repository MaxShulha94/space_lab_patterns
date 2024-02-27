class NormalTemperature:
    def __init__(self, normal_temperature):
        self.normal_temperature = normal_temperature

    def info(self) -> str:
        return f"Wished temperature in the room is {self.normal_temperature} Celsius."


class Correction:
    def too_heat(self) -> str:
        return "Current temperature is lower! Turn on heater."

    def too_cold(self) -> str:
        return "Current temperature is higher! Turn on conditioner."


class TemperatureAdapter(NormalTemperature, Correction):
    def __init__(self, normal_temperature, current_temperature):
        super().__init__(normal_temperature)
        self.current_temperature = current_temperature

    def change_temperature(self):
        if self.current_temperature < self.normal_temperature:
            return self.too_heat()
        elif self.current_temperature > self.normal_temperature:
            return self.too_cold()
        else:
            return "Temperature is normal."


def client_code(normal: NormalTemperature):
    print(normal.info(), end="")


if __name__ == "__main__":
    normal_temperature = int(input('Enter comfortable temperature in celsius: '))
    current_temperature = int(input('Enter current temperature in your room: '))
    normal_t = NormalTemperature(normal_temperature)
    client_code(normal=normal_t)
    print("\n")

    temperature_adapter = TemperatureAdapter(normal_temperature, current_temperature)
    temperature_adapter.info()
    result = temperature_adapter.change_temperature()

    print(result)
