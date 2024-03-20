class Passport:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)


class PassportFactory:
    def __init__(self):
        self._passports = {}

    def get_passport(self, number):
        if number not in self._passports:
            self._passports[number] = Passport(number)
        return self._passports[number]


class Person:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

    def __str__(self):
        return f"Name: {self.name}, Passport Number: {self.passport_number.number}"


class PassportOffice:
    def __init__(self):
        self._passport_factory = PassportFactory()
        self._persons = []

    def register_person(self, name, passport_number):
        passport = self._passport_factory.get_passport(passport_number)
        person = Person(name, passport)
        if passport not in [p.passport_number for p in self._persons]:
            self._persons.append(person)
        else:
            print(f"{person.name}, this passport number ({person.passport_number}) is already registered.")

    def display_registered_persons(self):
        print('Registered persons:')
        for person in self._persons:
            print(person)


passport_office = PassportOffice()


passport_office.register_person("Dmytro Smith", "987")
passport_office.register_person("Ivan Johnson", "123")
passport_office.register_person("Dmytro Smith", "987")

passport_office.display_registered_persons()
