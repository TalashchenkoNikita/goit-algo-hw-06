from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class PhoneNotValid(Exception):
    pass


class Phone(Field):
    def __init__(self, value):
        self.value = value if len(value) == 10 else None
        try:
            if self.value is None:
                raise PhoneNotValid
        except PhoneNotValid:
            print("Номер телефону не є дійсним")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        for phone_num in self.phones:
            if phone_num.value == phone:
                self.phones.remove(phone_num)

    def edit_phone(self, phone, new_phone):
        for i, phone_num in enumerate(self.phones):
            if phone_num.value == phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, phone):
        for contact in self.phones:
            if contact.value == phone:
                return contact

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

