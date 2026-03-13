class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        if len(phone_number) == 10:
            return True
        else:
            return False

class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            contact = Contact(name, phone_number)
            cls.all_contacts.append(contact)
        else:
            print("Неверный номер")

ContactList.add_contact("Виктория", "0700123456")
ContactList.add_contact("Даут", "0500456123")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)