import sys

# Sample user database
users = {
    "Alice": {"balance": 2000, "pin": 4321, "transaction_history": []},
    "Bob": {"balance": 1500, "pin": 1234, "transaction_history": []},
    "Charlie": {"balance": 3000, "pin": 5678, "transaction_history": []}
}

def atm_simulator():
    name = input("Enter your name: ").capitalize()
    if name not in users:
        print("User not found. Please try again.")
        sys.exit()
    print(f"\nHello, {name}!")
    print("Welcome to the ATM program")
    user = users[name]

    while True:
        print("\nPlease choose an option:")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Funds")
        print("4. Transfer Funds")
        print("5. Change PIN")
        print("6. View Transaction History")
        print("7. Exit")
        option = input("Enter your choice (1-7): ")

        if option == "1":
            print(f"Your current balance is: ${user['balance']}")
            user['transaction_history'].append(f"Checked balance: ${user['balance']}")

        elif option == "2":
            if verify_pin(user['pin']):
                amount = int(input("Enter the amount to withdraw: "))
                if amount > user['balance']:
                    print("Insufficient balance.")
                else:
                    user['balance'] -= amount
                    print(f"Withdrawal successful. New balance: ${user['balance']}")
                    user['transaction_history'].append(f"Withdrew ${amount}. New balance: ${user['balance']}")

        elif option == "3":
            if verify_pin(user['pin']):
                amount = int(input("Enter the amount to deposit: "))
                user['balance'] += amount
                print(f"Deposit successful. New balance: ${user['balance']}")
                user['transaction_history'].append(f"Deposited ${amount}. New balance: ${user['balance']}")

        elif option == "4":
            if verify_pin(user['pin']):
                recipient = input("Enter the recipient's name: ").capitalize()
                if recipient not in users:
                    print("Recipient not found.")
                else:
                    amount = int(input("Enter the amount to transfer: "))
                    if amount > user['balance']:
                        print("Insufficient balance.")
                    else:
                        user['balance'] -= amount
                        users[recipient]['balance'] += amount
                        print(f"Transfer successful. New balance: ${user['balance']}")
                        user['transaction_history'].append(f"Transferred ${amount} to {recipient}. New balance: ${user['balance']}")
                        users[recipient]['transaction_history'].append(f"Received ${amount} from {name}. New balance: ${users[recipient]['balance']}")

        elif option == "5":
            if verify_pin(user['pin']):
                new_pin = int(input("Enter your new PIN: "))
                user['pin'] = new_pin
                print("PIN changed successfully.")
                user['transaction_history'].append("PIN changed successfully.")

        elif option == "6":
            print("\nTransaction History:")
            if user['transaction_history']:
                for entry in user['transaction_history']:
                    print(f"- {entry}")
            else:
                print("No transactions yet.")

        elif option == "7":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


def verify_pin(correct_pin, max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        entered_pin = int(input("Enter your PIN: "))
        if entered_pin == correct_pin:
            return True
        else:
            attempts += 1
            print(f"Incorrect PIN. Attempts remaining: {max_attempts - attempts}")
    print("Too many incorrect attempts. Returning to main menu.")
    return False


atm_simulator()
