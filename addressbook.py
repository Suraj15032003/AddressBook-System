import re

class ContactPerson:
    """
    Description:
        Represents a contact person with personal details.
    """

    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        try:
            if not first_name or not last_name:
                raise ValueError("First and last name cannot be empty.")

            self.first_name = first_name
            self.last_name = last_name
            self.address = address1
            self.city = city
            self.state = state
            
            if not str(zip_code).isdigit() or len(str(zip_code)) != 5:
                raise ValueError("ZIP code must be a 5-digit number.")
            self.zip_code = int(zip_code)

            if not str(phone).isdigit() or len(str(phone)) not in (10, 12):
                raise ValueError("Phone number must be 10 or 12 digits long.")
            self.phone = int(phone)

            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                raise ValueError("Invalid email format.")
            self.email = email

        except ValueError as e:
            print(f"Error creating contact: {e}")
            raise

    def __str__(self):
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Address: {self.address}, {self.city}, {self.state}, {self.zip_code}\n"
                f"Phone: {self.phone}\n"
                f"Email: {self.email}\n")


class AddressBook:
    """
    Description:
        Manages multiple contact entries in an address book.
    """

    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        """
        Adds a new contact to the address book.
        """
        try:
            if not isinstance(contact, ContactPerson):
                raise TypeError("Invalid contact type. Must be a ContactPerson instance.")

            full_name = f"{contact.first_name} {contact.last_name}"
            if full_name in self.contacts:
                print(f"Contact '{full_name}' already exists in the address book.")
            else:
                self.contacts[full_name] = contact
                print(f"\nContact '{full_name}' added successfully!\n")

        except Exception as e:
            print(f"Error adding contact: {e}")

    def display_contacts(self):
        """
        Displays all contacts in the address book.
        """
        try:
            if not self.contacts:
                print("\nAddress Book is empty!\n")
            else:
                for contact in self.contacts.values():
                    print(contact)
        except Exception as e:
            print(f"Error displaying contacts: {e}")


class AddressBookMain:
    """
    Provides the main interface for the address book system.
    """

    @staticmethod
    def get_validated_input(prompt, validation_func, error_message):
        """
        Handles input validation for various fields.
        """
        while True:
            try:
                user_input = input(prompt).strip()
                if validation_func(user_input):
                    return user_input
                else:
                    print(error_message)
            except Exception as e:
                print(f"Unexpected error: {e}")

    @staticmethod
    def create_contact():
        """
        Collects user input to create a new contact.
        """
        try:
            first_name = input("Enter First Name: ").strip()
            last_name = input("Enter Last Name: ").strip()
            address = input("Enter Address: ").strip()
            city = input("Enter City: ").strip()
            state = input("Enter State: ").strip()

            # Validate ZIP Code (5-digit)
            zip_code = AddressBookMain.get_validated_input(
                "Enter ZIP Code (5 digits): ",
                lambda z: z.isdigit() and len(z) == 5,
                "Invalid ZIP Code! It must be a 5-digit number."
            )

            # Validate Phone Number (10 or 12 digits)
            phone = AddressBookMain.get_validated_input(
                "Enter Phone Number (10 or 12 digits): ",
                lambda p: p.isdigit() and len(p) in (10, 12),
                "Invalid Phone Number! It must be 10 or 12 digits long."
            )

            # Validate Email
            email = AddressBookMain.get_validated_input(
                "Enter Email: ",
                lambda e: re.match(r"[^@]+@[^@]+\.[^@]+", e),
                "Invalid Email! Please enter a valid email address."
            )

            return ContactPerson(first_name, last_name, address, city, state, int(zip_code), int(phone), email)

        except Exception as e:
            print(f"Error creating contact: {e}")
            return None
"""
testing :
contact = ContactPerson("John", "Doe", "123 Main St", "New York", "NY", 10001, 9876543210, "john@example.com")
print(contact)

# Create an address book and add a contact
address_book = AddressBook()
address_book.add_contact(contact)

address_book.display_contacts()
"""

def main():
    """
    Entry point of the program. Manages address book operations.
    """
    print("\nWelcome to the Address Book System!\n")
    
    address_book = AddressBook()
    
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                contact = AddressBookMain.create_contact()
                if contact:
                    address_book.add_contact(contact)
            elif choice == "2":
                address_book.display_contacts()
            elif choice == "3":
                print("\nExiting Address Book. Goodbye!\n")
                break
            else:
                print("Invalid choice! Please select a valid option.")

        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
