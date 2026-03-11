class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} - Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def remove_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def list_contacts(self):
        for contact in self.contacts:
            print(contact)

# Example usage:
if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.add_contact(Contact("John Doe", "123-456-7890", "john.doe@example.com"))
    contact_book.add_contact(Contact("Jane Smith", "098-765-4321", "jane.smith@example.com"))
    contact_book.list_contacts()
    print(contact_book.find_contact("John Doe"))
    contact_book.remove_contact("Jane Smith")
    contact_book.list_contacts()