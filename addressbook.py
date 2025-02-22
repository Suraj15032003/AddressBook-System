import re
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("address_book.log"),  # Store logs in a file
        logging.StreamHandler()  # Display logs in console
    ]
)

class ContactPerson:
    """
    Description:
        Represents a contact person with personal details.
    """
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        """
        Initializes a contact person with the given details and validates inputs.
        """
        try:
            if not first_name or not last_name:
                raise ValueError("First and last name cannot be empty.")

            if not isinstance(zip_code, int) or len(str(zip_code)) != 6:
                raise ValueError("ZIP code must be a 6-digit number.")

            if not isinstance(phone, int) or len(str(phone)) not in (10, 12):
                raise ValueError("Phone number must be 10 or 12 digits long.")

            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                raise ValueError("Invalid email format.")

            self.first_name = first_name
            self.last_name = last_name
            self.address = address
            self.city = city
            self.state = state
            self.zip_code = zip_code
            self.phone = phone
            self.email = email

            logging.info(f"Contact created: {self.first_name} {self.last_name}")

        except ValueError as e:
            logging.error(f"Error creating contact: {e}")
            raise

    def __str__(self):
        """
        Returns a formatted string representation of the contact.
        """
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
        """
        Initializes an empty address book.
        """
        self.contacts = {}
        logging.info("Address book initialized.")

    def add_contact(self, contact):
        """
        Adds a new contact to the address book.
        """
        try:
            if not isinstance(contact, ContactPerson):
                raise TypeError("Invalid contact type. Must be a ContactPerson instance.")

            full_name = f"{contact.first_name} {contact.last_name}"
            if full_name in self.contacts:
                logging.warning(f"Contact '{full_name}' already exists.")
            else:
                self.contacts[full_name] = contact
                logging.info(f"Contact '{full_name}' added successfully!")
        except Exception as e:
            logging.error(f"Error adding contact: {e}")

    def edit_contact(self, name, updated_contact):
        """
        Edits an existing contact in the address book.
        """
        try:
            if name in self.contacts:
                self.contacts[name] = updated_contact
                logging.info(f"Contact '{name}' updated successfully!")
            else:
                logging.warning(f"Contact '{name}' not found in the address book.")
        except Exception as e:
            logging.error(f"Error editing contact: {e}")
    
    def delete_contact(self, name):
        """
        Deletes a contact from the address book.
        """
        try:
            if name in self.contacts:
                del self.contacts[name]
                logging.info(f"Contact '{name}' deleted successfully!")
                print(f"Contact '{name}' has been deleted.")
            else:
                logging.warning(f"Contact '{name}' not found in the address book.")
                print(f"Contact '{name}' not found.")
        except Exception as e:
            logging.error(f"Error deleting contact: {e}")

    def display_contacts(self):
        """
        Displays all contacts in the address book.
        """
        try:
            if not self.contacts:
                logging.info("Address book is empty.")
                print("\nAddress Book is empty!\n")
            else:
                for contact in self.contacts.values():
                    print(contact)
                    logging.info(f"Displayed contact: {contact.first_name} {contact.last_name}")
        except Exception as e:
            logging.error(f"Error displaying contacts: {e}")

class AddressBookMain:
    """
    Main application class for managing the address book.
    """
    @staticmethod
    def create_contact():
        """
        Prompts user for contact details and creates a new ContactPerson object.
        """
        try:
            first_name = input("Enter First Name: ").strip()
            last_name = input("Enter Last Name: ").strip()
            address = input("Enter Address: ").strip()
            city = input("Enter City: ").strip()
            state = input("Enter State: ").strip()

            zip_code = input("Enter ZIP Code (6 digits): ").strip()
            phone = input("Enter Phone Number (10 or 12 digits): ").strip()
            email = input("Enter Email: ").strip()

            return ContactPerson(first_name, last_name, address, city, state, int(zip_code), int(phone), email)
        except Exception as e:
            logging.error(f"Error creating contact: {e}")
            return None

    @staticmethod
    def add_multiple_contacts(address_book):
        """
        Allows the user to add multiple contacts one at a time.
        """
        while True:
            contact = AddressBookMain.create_contact()
            if contact:
                address_book.add_contact(contact)
            more = input("Do you want to add another contact? (y/n): ").strip().lower()
            if more != 'y':
                break

def main():
    """
    Main function to run the Address Book application.
    """
    logging.info("Address Book Application Started")
    address_book = AddressBook()
    
    while True:
        try:
            print("\nMenu:")
            print("1. Add Contact")
            print("2. Add Multiple Contacts")
            print("3. Display Contacts")
            print("4. Edit Contact")
            print("5. Delete Contact")  
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                contact = AddressBookMain.create_contact()
                if contact:
                    address_book.add_contact(contact)
            elif choice == "2":
                AddressBookMain.add_multiple_contacts(address_book)
            elif choice == "3":
                address_book.display_contacts()
            elif choice == "4":
                name = input("Enter full name of the contact to edit: ").strip()
                updated_contact = AddressBookMain.create_contact()
                if updated_contact:
                    address_book.edit_contact(name, updated_contact)
            elif choice == "5": 
                name = input("Enter full name of the contact to delete: ").strip()
                address_book.delete_contact(name)
            elif choice == "6":
                logging.info("Exiting Address Book. Goodbye!")
                print("\nExiting Address Book. Goodbye!\n")
                break
            else:
                logging.warning("Invalid choice! Please select a valid option.")
                print("Invalid choice! Please select a valid option.")
        except Exception as e:
            logging.critical(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
