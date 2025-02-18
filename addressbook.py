address_book ={}

def create_contact():

    """This function allows the user to create a contact in the address book.
    It collects details such as first name, last name, address, city, state, 
    ZIP code, phone number, and email, and stores them in a dictionary."""

    first_name =input("Enter First Name: ").strip()
    last_name =input("Enter Last Name: ").strip()
    address =input("Enter Address: ").strip()
    city =input("Enter City: ").strip()
    state =input("Enter State: ").strip()
    zip_code =input("Enter ZIP Code: ").strip()
    phone =input("Enter Phone Number: ").strip()
    email =input("Enter Email: ").strip()
  
    contact_name =(f"{first_name} {last_name}")

    address_book[contact_name] ={
        "Address":address,
        "City":city,
        "State":state,
        "ZIP":zip_code,
        "Phone":phone,
        "Email":email
    }

    print(f"\nContact '{contact_name}' added successfully. \n")
    print(address_book[contact_name])

def main():
    print("Welcome to Address Book")
    create_contact()

if __name__=="__main__":
    main()