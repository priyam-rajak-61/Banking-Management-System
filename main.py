from account import BankAccount

bank = BankAccount()

while True:

    print("\n===== BANKING MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Login Account")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        bank.login_account()

    elif choice == "3":
        print("Thank You")
        break

    else:
        print("Invalid Choice")