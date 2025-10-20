class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
        return phone_number.isdigit() and len(phone_number) == 10

    def __str__(self):
        return f"{self.name}: {self.phone_number}"


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if not Contact.validate_phone_number(phone_number):
            raise ValueError("Номер телефона должен содержать ровно 10 цифр!")
        new_contact = Contact(name, phone_number)
        cls.all_contacts.append(new_contact)
        return new_contact


if __name__ == "__main__":
    ContactList.add_contact("Андрей", "0557127145")
    ContactList.add_contact("Маша", "0222911351")

    print("Все контакты:")
    for contact in ContactList.all_contacts:
        print(contact)
