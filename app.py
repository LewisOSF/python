import random

#account number - uniquie
#account name
#balance

# account = {
#     "account-number" : {
#         "account-name" : "James", "balance" : 0
#     },
# }

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
    print("2. Print all bank accounts")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account_name = input("Enter Account Name: ")
        createAccount(accounts, account_name)
    elif choice == 2:
        print("\nAll bank accounts")
        printBankAccounts(accounts)
    elif choice == 3:
        print("\nBye...")
        break
    else:
        print("Invalid selection")
