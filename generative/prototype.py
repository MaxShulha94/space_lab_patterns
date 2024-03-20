import copy


class Prototype:
    def copy(self):
        return copy.copy(self)

    def deep_copy(self):
        return copy.deepcopy(self)


class Car(Prototype):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"


car_prototype = Car("Toyota", "Corolla")
ordinary_car_clone = copy.copy(car_prototype)
deep_car_clone = copy.deepcopy(car_prototype)
print('BEFORE CHANGES')
print(f'ORIGINAL PROTOTYPE: {car_prototype}, ID: {id(car_prototype)}')
print(f'COPY: {ordinary_car_clone}, ID: {id(ordinary_car_clone)}')
print(f'DEEP COPY: {deep_car_clone}, ID: {id(deep_car_clone)}')

