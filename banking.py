#Enhanced Python Banking app
#Project 7.3 Python Banking Application

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_info():
    """Create Bank Account dictionary"""
    print("Welcome to the Python Banking Application!")
    name = input("Please enter your name: ").title()
    savings = float(input("Please enter your initial savings account deposit: $"))
    checking = float(input("Please enter your initial checking account deposit: $"))
    
    bank_account = {
        "Name": name,
        "Savings": savings,
        "Checking": checking
    }
    
    return bank_account


def make_transaction(bank_account):
    """Make a deposit or withdrawal on the given account"""
    account_type = input("Which account would you like to access? (Savings/Checking): ").title()   
    action = input("What type of transaction would you like to make? ((d)Deposit or (w)Withdrawal): ").lower()
    money_amount = float(input("Enter the amount of money for the transaction: $"))

    if account_type == "Savings" or account_type == "Checking":
        if action.startswith('d'):
            make_deposit(bank_account, account_type, money_amount)
        elif action.startswith('w'):
            make_withdrawal(bank_account, account_type, money_amount)
        else:
            print("Invalid transaction type. Please try again.")
    else:
        print("Invalid account type. Please try again.")

def make_deposit(bank_account, account_type, money_amount):
    """Add money to a specific type of account"""
    bank_account[account_type] += money_amount
    print(f"\nDeposited ${money_amount} into {bank_account['Name']}'s {account_type} account.")
    

def make_withdrawal(bank_account, account_type, money_amount):
    """Withdraw money from a specific type of account"""
    #Check that the balance on the account will still be positive
    if bank_account[account_type] - money_amount >= 0:
        bank_account[account_type] -= money_amount             
        print(f"\nWithdrew ${money_amount} from {bank_account['Name']}'s {account_type} account.")
    else:
        print(f"Insufficient funds for this withdrawal. By withrawing ${money_amount}, the balance would go negative.")


def display_info(bank_account):
    """Display all key-value pairs in the bank account dictionary"""
    print("\n--- Bank Account Information ---")
    for key, value in bank_account.items():
        if key == "Name":
            print(f"{key}: {value}")
        else:
            print(f"{key}: ${value}")


def continue_banking():
    """Ask the user if they want to continue banking"""
    choice = input("Would you like to make another transaction? (y/n): ").lower()
    if choice != 'y':
        bank = False
    else:
        bank = True

    return bank

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main code to run the banking application

#create a bank account
my_account = get_info()
is_running = True

while is_running:
    display_info(my_account)
    make_transaction(my_account)
    is_running = continue_banking()

display_info(my_account)
print("Thank you for using the Python Banking Application. Goodbye!")
