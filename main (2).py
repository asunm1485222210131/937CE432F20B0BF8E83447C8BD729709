class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self._account_number = account_number  # Private attribute for account number
        self._account_holder_name = account_holder_name  # Private attribute for account holder name
        self._account_balance = initial_balance  # Private attribute for account balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self._account_balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._account_balance:
                self._account_balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self._account_balance}")
            else:
                print("Insufficient funds to withdraw.")
        else:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")

    def display_balance(self):
        print(f"Account Balance for {self._account_holder_name}: ${self._account_balance}")

# Create an instance of the BankAccount class
account = BankAccount("123456789", "John Doe", 1000)

# Test the deposit and withdrawal functionality
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)  # This should print "Insufficient funds to withdraw."
account.display_balance()