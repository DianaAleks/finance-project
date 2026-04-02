from datetime import date
from cowPrint import show_welcome
from storage import AccountStorage

#TODO: load the accounts in the right places 
def show_menu():
    print("1. Add transaction")
    print("2. View transactions")
    print("q. Quit")
    return input("Choose an option: ").strip().lower()

def add_transaction(account):
    today = date.today()
    t_type = input("'Withdraw' or 'Deposit': ").strip().lower()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    
    if t_type == "withdraw":
        account.withdraw(amount, today)
        #should save the changes made to the account (w)
    elif t_type == "deposit":
        account.deposit(amount, today)
        #should save the changes made to the account (w)
    else:
        print("Invalid transaction type")
    
# should incorperate saved accounts
def view_transactions(account):
    
    pass

def main():
    show_welcome()
    storage = AccountStorage()
    while True: # main program loop

        while True:
            name = input("Enter account name: ").strip().lower()
            if storage.load_account(name):
                print(f"\nWelcome back, {name}!")
                break  

            elif name is None:
                print(f"Account '{name}' not found.")

            create = input("Create account? (y/n): ").strip().lower()

            if create == "y":
                try:
                    intial_amount = float(input("Intial amount (DKK): ").strip())
                except ValueError:
                    print("Invalid amount. Setting balance to 0.")
                    intial_amount = 0

                storage.add_account(name, intial_amount)
                storage.save_account(name)
                print(f" Account '{name}' created!")
                break

            elif create != "y":
                print("You must create an account to continue.\n")

        actions = {
            "1": add_transaction,
            "2": view_transactions,
        }
        
        while True:
            choice = show_menu()

            if choice == "q":
                print("Goodbye!")
                return
               
            action = actions.get(choice)

            if action:
                action(storage.load_account(name))
            else:
                print("Invaild choice")
            
            input("\nPress enter to continue...")

if __name__ == "__main__":
    main()