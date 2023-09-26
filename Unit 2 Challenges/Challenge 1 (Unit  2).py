''' Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the Bank Account class and test the deposit and withdrawal functionality. '''

class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        # Initialize private attributes
        self._account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        # Deposit money into the account
        if amount > 0:
            self.__account_balance += amount
            print("Deposited Amount ₹{}. New balance: ₹{}".format(amount, self.__account_balance))
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        # Withdraw money from the account
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print("Withdrew Amount ₹{}. New balance: ₹{}".format(amount, self.__account_balance))
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        # Display the account balance
        print("Account balance for Mr.{} (Account #{}): ₹{}".format(
            self.__account_holder_name, self._account_number, self.__account_balance))

# Create an instance of the BankAccount class
account = BankAccount(account_number="6578291717", account_holder_name="Ariharan", initial_balance=2334.0)
# Test deposit and withdrawal functionality
account.display_balance()
account.deposit(800.0)
account.withdraw(100.0)
