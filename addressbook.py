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

class Contact:
    """
    Description:
        Represents an individual contact with personal details.

    Parameters:
        first_name - First name of the contact.
        last_name - Last name of the contact.
        phone - Phone number (10 or 12 digits).
        email - Email address.
        address - Street address.
        city - City name.
        state - State name.
        zip_code - ZIP code (6 digits).

    Raises:
        ValueError: If any field is invalid.
    """
    def __init__(self, first_name, last_name, phone, email, address, city, state, zip_code):
        if not first_name or not last_name:
            raise ValueError("First and Last names cannot be empty.")
        if not re.match(r"^\d{10,12}$", phone):
            raise ValueError("Phone number must be 10 or 12 digits long.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        if not re.match(r"^\d{6}$", zip_code):
            raise ValueError("ZIP code must be 6 digits.")
        if not address:
            raise ValueError("Address cannot be empty.")
        if not city:
            raise ValueError("City cannot be empty.")
        if not state:
            raise ValueError("State cannot be empty.")

        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        logging.info(f"Contact created: {self.first_name} {self.last_name}")
    
    def __str__(self):
        """
        Description:
            Returns a formatted string representation of the contact.

        Returns:
            str: Formatted contact information.
        """
        return f"{self.first_name} {self.last_name} | {self.phone} | {self.email} | {self.address}, {self.city}, {self.state} {self.zip_code}"

class AddressBook:
    """
    Description:
        Manages a collection of contacts within an address book.

    Parameters:
        book_name (str): Name of the address book.
    """
    def __init__(self, book_name):
        self.book_name = book_name
        self.contacts = []
        logging.info(f"Address Book '{book_name}' created.")


    def add_contact(self, first_name, last_name, phone, email, address, city, state, zip_code):
        """
        Description:
            Adds a new contact to the address book.

        Parameters:
            first_name, last_name, phone, email, address, city, state, zip_code: Contact details.
        """
        # Check for duplicate contact by first and last name
        if self.find_contact(first_name, last_name):
            logging.warning(f"Contact '{first_name} {last_name}' already exists in {self.book_name}.")
            print(f"Contact '{first_name} {last_name}' already exists!")
            return
        try:
            contact = Contact(first_name, last_name, phone, email, address, city, state, zip_code)
            self.contacts.append(contact)
            logging.info(f"Contact '{first_name} {last_name}' added to {self.book_name}.")
        except ValueError as e:
            logging.error(f"Error adding contact: {e}")
            print(f"Error: {e}")

    def display_contacts(self):
        """
        Description:
            Displays all contacts in the address book.
        """
        if not self.contacts:
            print(f"{self.book_name} Address Book is empty.")
            logging.info(f"{self.book_name} Address Book is empty.")
            return
        print(f"\nContacts in {self.book_name}:")
        for contact in self.contacts:
            print(contact)
            logging.info(f"Displayed contact: {contact.first_name} {contact.last_name}")

    def find_contact(self, first_name, last_name):
        """
        Description:
            Finds and returns a contact by first and last name.

        Parameters:
            first_name - First name of the contact.
            last_name - Last name of the contact.

        Returns:
            Contact or None: The found contact or None.
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        return None

    def edit_contact(self, first_name, last_name):
        """
        Description:
            Edits an existing contact's details.

        Parameters:
            first_name - First name of the contact.
            last_name - Last name of the contact.
        """
        contact = self.find_contact(first_name, last_name)
        if contact:
            print("Enter new details (leave blank to keep current value):")
            new_phone = input(f"Phone ({contact.phone}): ").strip() or contact.phone
            new_email = input(f"Email ({contact.email}): ").strip() or contact.email
            new_address = input(f"Address ({contact.address}): ").strip() or contact.address
            new_city = input(f"City ({contact.city}): ").strip() or contact.city
            new_state = input(f"State ({contact.state}): ").strip() or contact.state
            new_zip = input(f"ZIP Code ({contact.zip_code}): ").strip() or contact.zip_code

            try:
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                contact.city = new_city
                contact.state = new_state
                contact.zip_code = new_zip
                logging.info(f"Contact '{first_name} {last_name}' updated.")
                print("Contact updated successfully.")
            except ValueError as e:
                logging.error(f"Error updating contact: {e}")
                print(f"Error: {e}")
        else:
            print("Contact not found.")

    def delete_contact(self, first_name, last_name):
        """
        Description:
            Deletes a contact from the address book.

        Parameters:
            first_name - First name of the contact.
            last_name - Last name of the contact.
        """
        contact = self.find_contact(first_name, last_name)
        if contact:
            self.contacts.remove(contact)
            logging.info(f"Contact '{first_name} {last_name}' deleted from {self.book_name}.")
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

class AddressBookSystem:
    """
    Description:
        Manages multiple address books.
    """
    def __init__(self):
        """
        Description:
            Initializes the Address Book System.
        """
        self.address_books = {}
        logging.info("Address Book System initialized.")

    def add_address_book(self, book_name):
        """
        Description:
            Adds a new address book to the system.

        Parameters:
            book_name (str): Name of the address book.
        """
        if book_name in self.address_books:
            print(f"Address Book '{book_name}' already exists!")
            logging.warning(f"Address Book '{book_name}' already exists!")
        else:
            self.address_books[book_name] = AddressBook(book_name)
            print(f"Address Book '{book_name}' created.")
            logging.info(f"Address Book '{book_name}' created.")

    def get_address_book(self, book_name):
        """
        Description:
            Retrieves an address book by name.

        Parameters:
            book_name (str): Name of the address book.

        Returns:
            AddressBook or None: The found address book or None.
        """
        return self.address_books.get(book_name, None)

    def display_all_books(self):
        """
        Description:
            Displays all address books in the system.
        """
        if not self.address_books:
            print("No Address Books available.")
            logging.info("No Address Books available.")
        else:
            print("\nAvailable Address Books:")
            for book_name in self.address_books:
                print(f"- {book_name}")
                logging.info(f"Displayed Address Book: {book_name}")

def main():
    """
    Description:
        Main function to interact with the Address Book System.
    """
    system = AddressBookSystem()
    
    while True:
        print("\n1. Add Address Book")
        print("2. Add Contact to Address Book")
        print("3. Display Contacts")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Display All Address Books")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_name = input("Enter Address Book name: ").strip()
            system.add_address_book(book_name)
        elif choice == "2":
            book_name = input("Enter Address Book name: ").strip()
            address_book = system.get_address_book(book_name)
            if address_book:
                first_name = input("Enter First Name: ").strip()
                last_name = input("Enter Last Name: ").strip()
                phone = input("Enter Phone Number: ").strip()
                email = input("Enter Email: ").strip()
                address = input("Enter Address: ").strip()
                city = input("Enter City: ").strip()
                state = input("Enter State: ").strip()
                zip_code = input("Enter ZIP Code (6 digits): ").strip()
                address_book.add_contact(first_name, last_name, phone, email, address, city, state, zip_code)
            else:
                print(f"Address Book '{book_name}' does not exist!")
        elif choice == "3":
            book_name = input("Enter Address Book name: ").strip()
            address_book = system.get_address_book(book_name)
            if address_book:
                address_book.display_contacts()
            else:
                print(f"Address Book '{book_name}' does not exist!")
        elif choice == "4":
            book_name = input("Enter Address Book name: ").strip()
            address_book = system.get_address_book(book_name)
            if address_book:
                first_name = input("Enter First Name of the contact to edit: ").strip()
                last_name = input("Enter Last Name of the contact to edit: ").strip()
                address_book.edit_contact(first_name, last_name)
            else:
                print(f"Address Book '{book_name}' does not exist!")
        elif choice == "5":
            book_name = input("Enter Address Book name: ").strip()
            address_book = system.get_address_book(book_name)
            if address_book:
                first_name = input("Enter First Name of the contact to delete: ").strip()
                last_name = input("Enter Last Name of the contact to delete: ").strip()
                address_book.delete_contact(first_name, last_name)
            else:
                print(f"Address Book '{book_name}' does not exist!")
        elif choice == "6":
            system.display_all_books()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
