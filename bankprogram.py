# Show balance
# Deposit
# Withdraw
# Exit

# 1. Show Balance
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

# 2. Deposit
def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("That's not a valid amount\n")
        return 0
    else:
        return amount

# 3. Withdraw 
def withdraw(balance):
    amount = float(input("enter amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient Funds Try Again!")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount


def main():

    balance = 0
    is_running = True

    while is_running:
        print("\nBanking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit\n")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Invalid Choice Please try again!")

    print("Thank you! Have a nice day!\n")

if __name__ == '__main__':
    main()