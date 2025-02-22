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
        Represents a contact with detailed personal information.

    Attributes:
        first_name - First name of the contact.
        last_name -Last name of the contact.
        phone - Phone number of the contact.
        email - Email address of the contact.
        address - Physical address of the contact.
        city - City of the contact.
        state- State of the contact.
        zip_code - ZIP code of the contact.
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
            Returns a string representation of the contact.

        Returns:
            str: Formatted contact details.
        """
        return f"{self.first_name} {self.last_name} | {self.phone} | {self.email} | {self.address}, {self.city}, {self.state} {self.zip_code}"

class AddressBook:
    """
    Description:
        Represents an address book containing multiple contacts.

    Attributes:
        book_name (str): Name of the address book.
        contacts (list): List of Contact objects.
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
            first_name - First name of the contact.
            last_name - Last name of the contact.
            phone - Phone number.
            email - Email address.
            address - Physical address.
            city - City.
            state - State.
            zip_code - ZIP code.
        """
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

    def delete_contact(self, first_name, last_name):
        """
        Description:
            Deletes a contact from the address book.

        Parameters:
            first_name (str): First name of the contact to delete.
            last_name (str): Last name of the contact to delete.
        """
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                self.contacts.remove(contact)
                logging.info(f"Contact '{first_name} {last_name}' deleted from {self.book_name}.")
                print(f"Contact '{first_name} {last_name}' deleted.")
                return
        print(f"Contact '{first_name} {last_name}' not found.")
        logging.warning(f"Attempted to delete non-existent contact '{first_name} {last_name}'.")

    def edit_contact(self, first_name, last_name, new_phone=None, new_email=None, new_address=None, new_city=None, new_state=None, new_zip_code=None):
        """
        Description:
            Edits the details of an existing contact.

        Parameters:
            first_name (str): First name of the contact to edit.
            last_name (str): Last name of the contact to edit.
            new_phone (str, optional): New phone number.
            new_email (str, optional): New email address.
            new_address (str, optional): New physical address.
            new_city (str, optional): New city.
            new_state (str, optional): New state.
            new_zip_code (str, optional): New ZIP code.
        """
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                if new_phone:
                    if not re.match(r"^\d{10,12}$", new_phone):
                        print("Invalid phone number format.")
                        return
                    contact.phone = new_phone
                if new_email:
                    if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
                        print("Invalid email format.")
                        return
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                if new_city:
                    contact.city = new_city
                if new_state:
                    contact.state = new_state
                if new_zip_code:
                    if not re.match(r"^\d{6}$", new_zip_code):
                        print("Invalid ZIP code format.")
                        return
                    contact.zip_code = new_zip_code
                logging.info(f"Contact '{first_name} {last_name}' updated in {self.book_name}.")
                print(f"Contact '{first_name} {last_name}' updated.")
                return
        print(f"Contact '{first_name} {last_name}' not found.")
        logging.warning(f"Attempted to edit non-existent contact '{first_name} {last_name}'.")

class AddressBookSystem:
    """
    Description:
        Manages multiple address books.

    Attributes:
        address_books (dict): Dictionary to store multiple address books.
    """
    def __init__(self):
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
            AddressBook or None: The address book if found, else None.
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
        Main function to run the Address Book System.
    """
    system = AddressBookSystem()
    
    while True:
        print("\n1. Add Address Book")
        print("2. Add Contact to Address Book")
        print("3. Display Contacts")
        print("4. Delete Contact")
        print("5. Edit Contact")
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
                zip_code = input("Enter ZIP Code: ").strip()
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
                first_name = input("Enter First Name of Contact to Delete: ").strip()
                last_name = input("Enter Last Name of Contact to Delete: ").strip()
                address_book.delete_contact(first_name, last_name)
            else:
                print(f"Address Book '{book_name}' does not exist!")
        elif choice == "5":
            book_name = input("Enter Address Book name: ").strip()
            address_book = system.get_address_book(book_name)
            if address_book:
                first_name = input("Enter First Name of Contact to Edit: ").strip()
                last_name = input("Enter Last Name of Contact to Edit: ").strip()
                new_phone = input("Enter New Phone (leave blank to keep unchanged): ").strip()
                new_email = input("Enter New Email (leave blank to keep unchanged): ").strip()
                new_address = input("Enter New Address (leave blank to keep unchanged): ").strip()
                new_city = input("Enter New City (leave blank to keep unchanged): ").strip()
                new_state = input("Enter New State (leave blank to keep unchanged): ").strip()
                new_zip_code = input("Enter New ZIP Code (leave blank to keep unchanged): ").strip()
                address_book.edit_contact(
                    first_name, last_name, new_phone or None, new_email or None, new_address or None, new_city or None, new_state or None, new_zip_code or None
                )
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
