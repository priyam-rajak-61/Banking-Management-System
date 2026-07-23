from database import get_connection
from decimal import Decimal, InvalidOperation

#============= ACCOUNT CREATE ===============#

class BankAccount:

    def create_account(self):

        while True:
            first_name = input("Enter First Name: ").strip()
            if first_name:
                break
            print("First Name cannot be empty")

        while True:
            last_name = input("Enter Last Name: ").strip()
            if last_name:
                break
            print("Last Name cannot be empty")

        while True:
            address = input("Enter Address: ").strip()
            if address:
                break
            print("Address cannot be empty")

        while True:
            mobile = input("Enter Mobile Number: ").strip()
            if mobile and len(mobile) == 10 and mobile.isdigit():
                break
            print("Invalid Mobile Number")

        while True:
            dob = input("Enter Date of Birth (YYYY-MM-DD): ").strip()
            if dob:
                break
            print("Date of Birth cannot be empty")

        while True:
            aadhaar = input("Enter Aadhaar Number: ").strip()
            if aadhaar and len(aadhaar) == 12 and aadhaar.isdigit():
                break
            print("Invalid Aadhaar Number")

        email = input("Enter Email (Optional): ").strip()
        if email == "":
            email = None

        while True:
            password = input("Create Password: ").strip()
            if password:
                break
            print("Password cannot be empty")

        while True:
            try:
                balance = float(input("Initial Deposit: "))
                if balance >= 500:
                    break
                print("Minimum Deposit is Rs.500")
            except ValueError:
                print("Enter a valid amount")

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO accounts
        (First_name, Last_name, Address, Mobile_number,
        Date_of_birth, Aadhaar_number, Email,
        Password, Balance)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            first_name, last_name, address, mobile,
            dob, aadhaar, email, password, balance
        )

        cursor.execute(query, values)
        conn.commit()

        account_number = cursor.lastrowid
        print("Account Created Successfully")
        print(f"Your Account Number: {account_number:06d}")

        cursor.close()
        conn.close()
