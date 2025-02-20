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
    Description: Represents a contact with personal details.
    
    Parameters:
        name - The name of the contact.
        phone - The phone number (10 or 12 digits long).
        email - The email address.
        address - The physical address.
    """
    def __init__(self, name, phone, email, address):
        """
        Description: Initializes a contact and validates inputs.
        
        Parameters:
            name - Contact's name.
            phone - Contact's phone number.
            email - Contact's email address.
            address - Contact's address.
        """
        if not name:
            raise ValueError("Name cannot be empty.")
        if not re.match(r"^\d{10,12}$", phone):
            raise ValueError("Phone number must be 10 or 12 digits long.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        logging.info(f"Contact created: {self.name}")
    
    def __str__(self):
        """
        Description: Returns a formatted string representation of the contact.
        
        Return:
             Formatted contact information.
        """
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"

class AddressBook:
    """
    Description: Manages contacts within an address book.
    
    Parameters:
        book_name - The name of the address book.
    """
    def __init__(self, book_name):
        """
        Description: Initializes an address book with a given name.
        
        Parameters:
            book_name (str): The name of the address book.
        """
        self.book_name = book_name
        self.contacts = []
        logging.info(f"Address Book '{book_name}' created.")

    def add_contact(self, name, phone, email, address):
        """
        Description: Adds a new contact after validation.
        
        Parameters:
            name : Contact's name.
            phone : Contact's phone number.
            email : Contact's email address.
            address : Contact's address.
        """
        try:
            contact = Contact(name, phone, email, address)
            self.contacts.append(contact)
            logging.info(f"Contact '{name}' added to {self.book_name}.")
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
            logging.info(f"Displayed contact: {contact.name}")

class AddressBookSystem:
    """
    Description: Manages multiple Address Books.
    """
    def __init__(self):
        """
        Description: Initializes the Address Book System.
        """
        self.address_books = {}
        logging.info("Address Book System initialized.")

    def add_address_book(self, book_name):
        """
        Description: Creates a new address book if it does not exist.
        
        Parameters:
            book_name (str): The name of the address book.
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
        Description: Retrieves an existing address book by name.
        
        Parameters:
            book_name (str): The name of the address book to retrieve.
        
        Return:
            AddressBook or None: The address book if found, otherwise None.
        """
        return self.address_books.get(book_name, None)

    def display_all_books(self):
        """
        Description: Displays all available address books.
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
    Description: Main function to interact with the Address Book System.
    """
    system = AddressBookSystem()
    
    while True:
        print("\n1. Add Address Book")
        print("2. Add Contact to Address Book")
        print("3. Display Contacts")
        print("4. Display All Address Books")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_name = input("Enter Address Book name: ").strip()
            system.add_address_book(book_name)
        elif choice == "2":
            book_name = input("Enter Address Book name: ").strip()
            address_book = system.get_address_book(book_name)
            if address_book:
                name = input("Enter Contact Name: ").strip()
                phone = input("Enter Phone Number: ").strip()
                email = input("Enter Email: ").strip()
                address = input("Enter Address: ").strip()
                address_book.add_contact(name, phone, email, address)
            else:
                print(f"Address Book '{book_name}' does not exist!")
                logging.warning(f"Attempted to add contact to non-existent Address Book '{book_name}'.")
        elif choice == "3":
            book_name = input("Enter Address Book name: ").strip()
            address_book = system.get_address_book(book_name)
            if address_book:
                address_book.display_contacts()
            else:
                print(f"Address Book '{book_name}' does not exist!")
                logging.warning(f"Attempted to display contacts of non-existent Address Book '{book_name}'.")
        elif choice == "4":
            system.display_all_books()
        elif choice == "5":
            print("Exiting...")
            logging.info("Address Book System exited.")
            break
        else:
            print("Invalid choice! Please try again.")
            logging.warning("Invalid menu choice entered.")

if __name__ == "__main__":
    main()
