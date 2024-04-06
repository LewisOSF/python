import random

#account number - uniquie
#account name
#balance

# account = {
#     "account-number" : {
#         "account-name" : "James", "balance" : 0
#     },
# }

def account_exist(accs:dict, acc_num:str) -> bool:
    if acc_num in accs:
        return True
    else:
        return False

def deposit(accs:dict, acc_num:str, amt:float):
    if account_exist(accs, acc_num):
        current_bal = accs[acc_num]['balance']
        new_bal = current_bal + amt
        accs[acc_num]['balance'] = new_bal
        print(f"Deposit successful, new balance is {new_bal}")
    else:
        print(f"Account number {acc_num} not found!")

def withdrawl(accs:dict, acc_num:str, amt:float):
    if account_exist(accs, acc_num):
        current_bal = accs[acc_num]['balance']
        new_bal = current_bal - amt
        accs[acc_num]['balance'] = new_bal
        print(f"Withdrawl successful, new balance is {new_bal}")
    else:
        print(f"Account number {acc_num} not found!")

def check_balance(accs:dict, acc_num:str)->float:
    if account_exist(accs, acc_num):
        return accs[acc_num]['balance']
    else:
        print(f"Account number {acc_num} not found!")

def printBankAccounts(accs:dict):
    print("Account Number | Account Name | Balance")

    for a in accs:
        acc_number = str(a).ljust(14, " ")
        acc_name =  accs[a]['name'].ljust(12, " ")
        acc_bal = str(accs[a]['balance']).rjust(7, " ")
        print(f"{acc_number} | {acc_name} | {acc_bal}")

    return

def createAccount(accs:dict, acc_name):
    acc_num = str(random.randint(1,9999)).zfill(10)
    accs[acc_num] = {"name":acc_name, "balance":0}
    print(f"Account {acc_num} was created sucessfully for {acc_name}")
    return

accounts = {}

print("====== Welcome to the Banking App ======")
while True:
    print("\n=== What would you like to do today? ===")
    print("1. Create a new account")
    print("2. Make deposit")
    print("3. Make withdrawl")
    print("4. Check balance")
    print("5. Print all bank accounts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account_name = input("Enter Account Name: ")
        createAccount(accounts, account_name)
    elif choice == 2:
        print("\nMake Deposit")
        account_number = input("Enter Account No: ")
        amount = float(input("Enter Amount to Deposit: "))
        deposit(accounts, account_number, amount)
    elif choice == 3:
        print("\nMake Withdrawl")
        account_number = input("Enter Account No: ")
        amount = float(input("Enter Amount to Withdraw: "))
        withdrawl(accounts, account_number, amount)
    elif choice == 4:
        print("\nCheck Account Balance")
        account_number = input("Enter Account No: ")
        bal = check_balance(accounts, account_number)
        print(f"Account Balance for {account_number} is: {bal}")
    elif choice == 5:
        print("\nAll bank accounts")
        printBankAccounts(accounts)
    elif choice == 6:
        print("\nBye...")
        break
    else:
        print("Invalid selection")
