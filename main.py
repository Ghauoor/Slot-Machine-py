MAX_LINES = 3


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


def main():
    balance = deposite()
    lines = get_number_of_lines()

    print(balance, lines)


main()
