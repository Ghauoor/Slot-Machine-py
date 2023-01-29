import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


ROWS = 3
COLS = 3


symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

    


#! Get the Deposite From User...
def deposite():
    while True:
        amount = input("What Would You Like To Deposite? $ ")
        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break
            else:
                print("Amount Must be Greater Then Zero")
        else:
            print("Enter a Number.")

    return amount


# ! Get the number of Lines...
def get_number_of_lines():
    while True:
        lines = input("Enter the Number of Lines to Bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the Valid Number Of Lines.")
        else:
            print("Enter a Number.")

    return lines


# ! Get the Bet


def get_bet():
    while True:
        amount = input("What Would You Like To Bet on each Line? $ ")
        if amount.isdigit():
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount Must be Between {MIN_BET} - {MAX_BET}")
        else:
            print("Enter a Number.")

    return amount


# ! Main Funcation
def main():
    balance = deposite()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > total_bet:
            print(
                f"You don't have enough to bet on that amount, Your Current Balance is: ${balance}"
            )
        else:
            break

    print(
        f"You are Betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}"
    )


main() 
