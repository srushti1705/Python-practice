def atm():
    balance = 5000  

    print("Welcome to Simple ATM")

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Your balance is:", balance)

        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Amount deposited successfully.")

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance!")
            else:
                balance -= amount
                print("Withdrawal successful.")

        elif choice == "4":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid choice. Try again.")

atm()
