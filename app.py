print("====== Welcome to the Banking App ======")

while True:
    print("=== What would you like to do today? ===")
    print("1. Create a new account")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 2:
        break
    else:
        print("Invalid selection")
