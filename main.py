def deposite():
    while True:
        amount = input("What Would You Like To Deposite? $")
        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break
            else:
                print("Amount Must be Greater Then Zero")
        else:
            print("Enter a Number.")

    return amount
