#Python slot Machine
import random

def spin_row(symbols):
    print("Spinning.....")
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("******************************")
    print(" | ".join(row))
    print("******************************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0


def main():
    balance = 100
    print("******************************")
    print("Welcome to Python Slot Machine")
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    print(f"Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("******************************")
    while balance > 0:
        bet = input("Place your bet amount: ")
        if not bet.isdigit():
            print("Enter a valid number")
            continue

        bet = int(bet)
        if bet > balance:
            print(f"You cannot bet amount more than your balance")
            continue

        # if bet < 10:
        #     print("Minimum bet amount is $10")
        #     continue

        row = spin_row(symbols)
        print_row(row)
        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print(f"Sorry you lost this round.")
        balance -= bet
        balance += payout
        print(f"Your current balance is ${balance}")
        #
        # play_again = input("Do you want to spin again? (Y/N): ").upper()
        #
        # if play_again != 'Y':
        #     break

    print("****************************")
    print(f"Game Over! Your final balance is ${balance}")


if __name__ == '__main__':
    main()