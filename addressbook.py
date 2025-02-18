address_book = {}

def create_contact():
    """
    Description:
      This function allows the user to create a contact in the address book.
      It collects details such as first name, last name, address, city, state, 
      ZIP code, phone number, and email, and stores them in a dictionary.
    
    Parameters:
      Takes user inputs.
    
    Returns:
      None
    """
    
    try:
        first_name = input("Enter First Name: ").strip()
        last_name = input("Enter Last Name: ").strip()
        address = input("Enter Address: ").strip()
        city = input("Enter City: ").strip()
        state = input("Enter State: ").strip()

        while True:
            try:
                zip_code = int(input("Enter ZIP Code: ").strip())
                if len(str(zip_code)) != 5:  # Assuming a 5-digit ZIP code
                    raise ValueError("ZIP Code must be a 5-digit number.")
                break
            except ValueError as e:
                print(f" Invalid ZIP Code! {e}. Please enter again.")

      
        while True:
            try:
                phone = int(input("Enter Phone Number: ").strip())
                if len(str(phone)) not in (10, 12):  
                    raise ValueError("Phone Number must be 10 or 12 digits long.")
                break
            except ValueError as e:
                print(f" Invalid Phone Number! {e}. Please enter again.")

        # Handling Email input
        while True:
            email = input("Enter Email: ").strip()
            if "@" in email and "." in email:
                break
            else:
                print("Invalid Email! Please enter a valid email address.")

       
        contact_name = (f"{first_name} {last_name}")
        address_book[contact_name] = {
            "Address": address,
            "City": city,
            "State": state,
            "ZIP": zip_code,
            "Phone": phone,
            "Email": email
        }

        print(f"\nContact '{contact_name}' added successfully!\n")
        print(address_book[contact_name])

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():

    print("Welcome to Address Book")
    create_contact()


if __name__ == "__main__":
    main()