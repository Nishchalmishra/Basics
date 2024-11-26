def available_balance():
    print(f"Your available balance is {balance}")

def deposit():
    amount = int(input("Entered the amount to be deposited: "))
    return amount

def withdraw():
    amount = int(input("Entered the amount to be withdraw: "))
    return amount

balance = 0



is_running = True

while is_running:
    print("--------Banking Options---------")
    print("Press 1 for available balance")
    print("Press 2 for deposit")
    print("Press 3 for withdraw the money")
    print("Press 4 for quit")

    entered = int(input("Press a key: "))

    match entered:
        case 1:
            available_balance()
        case 2:
            balance += deposit()
        case 3:
            balance -= withdraw()
        case 4:
            is_running = False
        case _:
            print("Invalid input")


# if __name__ == "__main__":
#     main()