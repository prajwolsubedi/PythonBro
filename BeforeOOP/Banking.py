#1. Show Balance
#2. Deposit
#3. Withdraw
def deposit(balance):
    amount = int(input("Enter the amount you want to deposit: "))
    balance += amount
    print(f"${amount} successfully added to your account. \nYour new balance is ${balance}")


def showBalance(balance):
    print(f"Your current balance is {balance}")


def withdraw(balance):
    amount = int(input("Enter the amount you want to withdraw: "))
    if(amount > balance):
        print("You cannot withdraw the amount greater than your balance.")
    else:
        balance -= amount
        print(f"${amount} successfully withdraw from your account. \nYour new balance is ${balance}")

def main():
    balance = 1000
    askInput = True
    print("Welcome to the Sarkar Bank.")
    while(askInput):
        print("Choose the operations you want to perform")
        operationChoosen = int(input(f" 1. Show Balance \n 2. Deposit \n 3. Withdraw \n 4. Exit \n" ))
        if(operationChoosen == 1):
            showBalance(balance)
        elif(operationChoosen == 2):
            deposit(balance)
        elif(operationChoosen == 3):
            withdraw(balance)
        elif (operationChoosen == 4):
            print("Thanks for using our bank.")
            return
        else:
            print("Invalid option please choose any 3 operation displayed here.")

if __name__ == '__main__':
    main()

