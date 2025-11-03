#NAME - AVNI BHAMBANI : ENROLLMENT NO. - 2502140017

bank_accounts = {'101': {'name':'Avni Bhambani','type': 'Savings','balance': 350000,'password': 'avni123','transactions': []},
'102': {'name': 'Sanjhal Jain','type': 'Current','balance': 400245,'password': 'sanjhal123','transactions': []},
'103': {'name': 'Satvik','type': 'Savings','balance':30000,'password': 'Satvik','transactions': []}
}
ACCOUNT_TYPES = ('savings', 'current')

#creating account
def create_account():    #def function helps to declare allowing us to reuse code for specific task
    acc_num = input("Enter Account Number: ")
    if acc_num in bank_accounts:
        print("Account already exists!")
        return           #return helpss to terminate its execution and send a value back to the caller
    name = input("Enter Account Holder Name: ")
    acc_type = input("Enter Account Type (savings/current): ")
    if acc_type not in ACCOUNT_TYPES:
        print("Invalid account type!")
        return
    password = input("Set a Password: ")
    bank_accounts[acc_num] = {
        'name': name,
        'type': acc_type,
        'balance': 0.0,
        'password': password,
        'transactions': []
    }
    print("Account created successfully!")

#deposit amount
def deposit_funds():
    acc_num = input("Enter Account Number: ")
    if acc_num not in bank_accounts:
        print("Account not found!")
        return
    password = input("Enter Password: ")
    if password != bank_accounts[acc_num]['password']:
        print("Incorrect password!")
        return
    amount = float(input("Enter Amount to Deposit: "))
    bank_accounts[acc_num]['balance'] += amount
    bank_accounts[acc_num]['transactions'].append(f"Deposit: +{amount}")
    print(" Amount deposited successfully")

#withdrawal of amount
def withdraw_funds():
    acc_num = input("Enter Account Number: ")
    if acc_num not in bank_accounts:
        print("Account not found!")
        return
    password = input("Enter Password: ")
    if password != bank_accounts[acc_num]['password']:
        print("Incorrect password!")
        return
    amount = float(input("Enter Amount to Withdraw: "))   #float is used because amount could be in decimals
    if amount > bank_accounts[acc_num]['balance']:
        print("Insufficient balance")
        return
    bank_accounts[acc_num]['balance'] -= amount
    bank_accounts[acc_num]['transactions'].append(f"Withdrawal: -{amount}")
    print("Withdrawal successful")

#veiwing full bank statement
def view_report():
    if not bank_accounts:
        print("No accounts found.")
        return
    total_bank_balance = 0
    for acc_num, details in bank_accounts.items():
        print(f"\nAccount No: {acc_num}")
        print(f"Name: {details['name']}")
        print(f"Type: {details['type']}")
        print(f"Balance: ₹{details['balance']}")
        total_bank_balance += details['balance']
    print(f"\n Total Bank Balance: ₹{total_bank_balance}")

#searching specific account and its details
def search_account():
    acc_num = input("Enter Account Number: ")
    if acc_num in bank_accounts:
        details = bank_accounts[acc_num]
        print(f"Name: {details['name']}")
        print(f"Type: {details['type']}")
        print(f"Balance: ₹{details['balance']}")
        print(f"Transactions: {details['transactions']}")
    else:
        print("Account not found!")

#close account
def close_account():
    acc_num = input("Enter Account Number: ")
    if acc_num in bank_accounts:
        del bank_accounts[acc_num]
        print("Account closed successfully!")
    else:
        print("Account not found!")

#MAIN MENU
def main_menu():
    while True:
        print("\nBANK MANAGEMENT SYSTEM ")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View All Accounts Report")
        print("5. Search Account")
        print("6. Close Account")
        print("7. Exit")

        choice = input("Enter your choice : ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_funds()
        elif choice == '3':
            withdraw_funds()
        elif choice == '4':
            view_report()
        elif choice == '5':
            search_account()
        elif choice == '6':
            close_account()
        elif choice == '7':
            print("end")
            break
        else:
            print("Invalid choice")

main_menu()




