import re

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not re.match(r'^\d{10}$', value):
            raise ValueError("Номер телефону має бути 10-значним.")

class Record:
    def __init__(self, name_value):
        self.name = Name(name_value)
        self.phones = []

    def add_phone(self, phone_value):
        try:
            phone = Phone(phone_value)
            self.phones.append(phone)
        except ValueError as e:
            print(e)

    def remove_phone(self, phone_value):
        self.phones = [phone for phone in self.phones if phone.value != phone_value]

    def edit_phone(self, old_phone_value, new_phone_value):
        self.remove_phone(old_phone_value)
        self.add_phone(new_phone_value)

    def search_phone(self, phone_value):
        for phone in self.phones:
            if phone.value == phone_value:
                return phone
        return None

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def find_records_by_name(self, name_value):
        return [record for record in self.records if record.name.value == name_value]

    def remove_record_by_name(self, name_value):
        self.records = [record for record in self.records if record.name.value != name_value]

    def print_records(self):
        for record in self.records:
            print(f"Name: {record.name.value}")
            for phone in record.phones:
                print(f"Phone: {phone.value}")
            print("-" * 10)


address_book = AddressBook()

record1 = Record("John")
record1.add_phone("1234567890")
record1.add_phone("1112223333")
address_book.add_record(record1)

record2 = Record("Jane")
record2.add_phone("5555555555")
address_book.add_record(record2)

print("All records:")
address_book.print_records()

print("\nFinding record by name 'John':")
john_records = address_book.find_records_by_name("John")
for record in john_records:
    print(f"Name: {record.name.value}")
    for phone in record.phones:
        print(f"Phone: {phone.value}")

print("\nRemoving record by name 'Jane':")
address_book.remove_record_by_name("Jane")
address_book.print_records()
