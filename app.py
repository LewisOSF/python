import random
import uuid
from enum import Enum

# account = {
#     "account-number" : {
#         "account-name" : "James", "balance" : 0
#     },
# }

class Operation(Enum):
    DEPOSIT = 1
    WITHDRAW = 2

def account_exist(accs:dict, acc_num:str) -> bool:
    if acc_num in accs:
        return True
    else:
        print(f"Account number {acc_num} not found!")
        return False

def do_trans(accs:dict, acc_num:str, amt:float, opr:Operation):
    msg = ""
    if account_exist(accs, acc_num):
        current_bal = accs[acc_num]['balance']
        if opr == Operation.DEPOSIT:
            msg = "Deposit"
            new_bal = current_bal + amt
        elif opr == Operation.WITHDRAW:
            msg = "Withdraw"
            new_bal = current_bal - amt
        accs[acc_num]['balance'] = new_bal
        print(f"{msg} successful, new balance is {new_bal}")

def check_balance(accs:dict, acc_num:str)->float:
    if account_exist(accs, acc_num):
        return accs[acc_num]['balance']
    else:
        return 0

def printBankAccounts(accs:dict):
    print("Account Number | Account Name | Balance")

    for a in accs:
        acc_number = str(a).ljust(14, " ")
        acc_name =  accs[a]['name'].ljust(12, " ")
        acc_bal = str(accs[a]['balance']).rjust(7, " ")
        print(f"{acc_number} | {acc_name} | {acc_bal}")

    return

def createAccount(accs:dict, acc_name):
    acc_num = str(uuid.uuid4())[:8]
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
        do_trans(accounts, account_number, amount, Operation.DEPOSIT)
    elif choice == 3:
        print("\nMake Withdrawl")
        account_number = input("Enter Account No: ")
        amount = float(input("Enter Amount to Withdraw: "))
        do_trans(accounts, account_number, amount, Operation.WITHDRAW)
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
