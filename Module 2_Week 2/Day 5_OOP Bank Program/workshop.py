# OOP Banking System

'''
    Overview:
        - Users can create accounts
        - Perform transactions like deposits, withdrawals, and balance inquiries
        - Basic Validation (Ensuring that withdrawals do not exceed the account balance)
'''

# 1. Create a BankAccount class: Represent an account with attributes such as the account holder's name, balance, and methods to perform transactions
class BankAccount:
    # constructor method
    def __init__(self, account_holder, balance=0.00):
        self.account_holder = account_holder
        self.balance = balance
        
    # methods to perform the transactions (deposit, withdrawal, check_balance)
    
    # deposit method
    def deposit(self, deposit_amount):
        if (deposit_amount > 0):
            self.balance += round(deposit_amount, 2)
            print(f"${deposit_amount} added to your account! Your new balance is: {self.balance}")
        else:
            print("Deposit must be greater than zero!")
    
    # withdrawal method
    def withdrawal(self, withdrawal_amount):
        if withdrawal_amount > 0:
            if self.balance > withdrawal_amount:
                string_withdraw_amount = str(withdrawal_amount)
                index_of_point = string_withdraw_amount.index(".")
                sliced = string_withdraw_amount[index_of_point + 1:]
                num_of_decimals = len(sliced)
                if num_of_decimals > 2:
                    print("Please enter amount with 2 decimals.")
                else:    
                    self.balance -= withdrawal_amount
                    print(f"${withdrawal_amount} was deducted from your account! Your new balance is: {self.balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Withdraw amount must be greater than zero!")
    
    # check_balance method
    def check_balance(self):
        print(f"Account Holder: {self.account_holder}, Current Balance: {self.balance}")

# 2. Create a Bank class: Will manage multiple accounts, allowing users to open new accounts and interact with their account.
class Bank:
    # constructor method
    def __init__(self):
        self.accounts = {}
        
    # create_account method
    def create_account(self, account_holder):
        if account_holder not in self.accounts:
            new_account = BankAccount(account_holder)
            self.accounts[account_holder] = new_account
            print(f"Account created for {account_holder}!")
        else:
            print(f'Account already exists for {account_holder}!')

    # get_account method
    def get_account(self, account_holder):
        if account_holder in self.accounts:
            return self.accounts[account_holder]
        else:
            print(f"Account for {account_holder} does not exist!")


# Create a CLI(also known as a "runner") to interact with the bank system
def runner():
    # create an instance of the Bank class
    bank = Bank()
    # while loop for continuous interactivity
    while True:
        # print valid options to the command line
        print('''
                ************ Bank Menu ************
                1. Create Account
                2. Deposit Money
                3. Withdrawal Money
                4. Check balance
                5. Exit
''')
        # ask the user for input
        choice = int(input('What would you like to do today? (Choose a number) '))

        if (choice == 1):
            name = input("What is the name of the Account Holder? ")
            bank.create_account(name)
        elif choice == 2:
            name = input("What is the name of the Account Holder? ")
            account = bank.get_account(name)
            if account:
                amount = float(input("How much would you like to deposit? "))
                account.deposit(amount)
        elif choice == 3:
            name = input("What is the name of the Account Holder? ")
            account = bank.get_account(name)
            if account:
                amount = float(input("How much would you like to withdraw? "))
                account.withdrawal(amount)
        elif choice == 4:
            name = input("What is the name of the Account Holder? ")
            account = bank.get_account(name)
            if account:
                account.check_balance()
        elif choice == 5:
            print('Thank you for Banking with us! Have a good day!')
            break
        else:
            print("Invalid choice! Please try again! Choose a number between 1 - 5!")
# run our program :D
runner()