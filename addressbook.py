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
    
    Parameters:
        first_name (str): First name of the contact.
        last_name (str): Last name of the contact.
        address (str): Address of the contact.
        city (str): City of residence.
        state (str): State of residence.
        zip_code (int): 6-digit ZIP code.
        phone (int): Phone number (10 or 12 digits).
        email (str): Email address.
    
    Raises:
        ValueError: If any of the input validations fail.
    """

    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
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
        Description:
            Returns a formatted string representation of the contact.
        
        Returns:
            str: Formatted contact details.
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
        Description:
            Initializes an empty address book.
        """
        self.contacts = {}
        logging.info("Address book initialized.")

    def add_contact(self, contact):
        """
        Description:
            Adds a new contact to the address book.
        
        Parameters:
            contact (ContactPerson): Contact object to be added.
        
        Raises:
            TypeError: If the provided contact is not a ContactPerson instance.
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
        Description:
            Edits an existing contact in the address book.
        
        Parameters:
            name (str): Full name of the contact to be edited.
            updated_contact (ContactPerson): Updated contact object.
        """
        try:
            if name in self.contacts:
                self.contacts[name] = updated_contact
                logging.info(f"Contact '{name}' updated successfully!")
            else:
                logging.warning(f"Contact '{name}' not found in the address book.")
        except Exception as e:
            logging.error(f"Error editing contact: {e}")
#edit option code
    def display_contacts(self):
        """
        Description:
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
    Description:
        Provides the main interface for the address book system.
    """

    @staticmethod
    def get_validated_input(prompt, validation_func, error_message):
        """
        Description:
            Gets user input and validates it using a provided function.
        
        Parameters:
            prompt (str): The message displayed to the user.
            validation_func (function): A function that validates the input.
            error_message (str): The error message displayed if validation fails.
        
        Returns:
            str: Validated user input.
        """
        while True:
            try:
                user_input = input(prompt).strip()
                if validation_func(user_input):
                    return user_input
                else:
                    logging.warning(error_message)
                    print(error_message)
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                print(f"Unexpected error: {e}")

    @staticmethod
    def create_contact():
        """
        Description:
            Collects user input and creates a new contact.
        
        Returns:
            ContactPerson: A newly created contact object. 
        """
        try:
            first_name = input("Enter First Name: ").strip()
            last_name = input("Enter Last Name: ").strip()
            address = input("Enter Address: ").strip()
            city = input("Enter City: ").strip()
            state = input("Enter State: ").strip()

            zip_code = AddressBookMain.get_validated_input(
                "Enter ZIP Code (6 digits): ",
                lambda z: z.isdigit() and len(z) == 6,
                "Invalid ZIP Code! It must be a 6-digit number."
            )

            phone = AddressBookMain.get_validated_input(
                "Enter Phone Number (10 or 12 digits): ",
                lambda p: p.isdigit() and len(p) in (10, 12),
                "Invalid Phone Number! It must be 10 or 12 digits long."
            )

            email = AddressBookMain.get_validated_input(
                "Enter Email: ",
                lambda e: re.match(r"[^@]+@[^@]+\.[^@]+", e),
                "Invalid Email! Please enter a valid email address."
            )

            return ContactPerson(first_name, last_name, address, city, state, int(zip_code), int(phone), email)

        except Exception as e:
            logging.error(f"Error creating contact: {e}")
            return None


def main():
    """
    Description:
        Entry point of the program. Manages address book operations.
    """
    logging.info("Address Book Application Started")
    
    address_book = AddressBook()
    
    while True:
        try:
            print("\nMenu:")
            print("1. Add Contact")
            print("2. Display Contacts")
            print("3. Edit Contact")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                contact = AddressBookMain.create_contact()
                if contact:
                    address_book.add_contact(contact)
            elif choice == "2":
                address_book.display_contacts()
            elif choice == "3":
                name = input("Enter full name of the contact to edit: ").strip()
                updated_contact = AddressBookMain.create_contact()
                if updated_contact:
                    address_book.edit_contact(name, updated_contact)
            elif choice == "4":
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