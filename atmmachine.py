Balance=100000

def check_balance():
    print(f"your Balance:Rs{Balance}")


def deposit(amount):
    global Balance
    Balance+=amount
    print(f"{amount}deposited")
    print(f"your new balance:rs{Balance}")


def withdraw(amount):
    global Balance
    if amount>Balance:
        print(f"insufficient balance")
    else:
        Balance-=amount
        print(f"{amount}withdrawn")
        print(f"your new balance:rs{Balance}")

check_balance()
deposit(5000)
withdraw(2000)