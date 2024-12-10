#creditCardNumber = "378282246310005"
creditCardNumber = "5555 5555 5555 4444"

def luhnAlgorithm(creditCardNumber):

    creditCardNumber = creditCardNumber.replace(' ', '')
    print(creditCardNumber)
    sum = 0
    lengthOfList = len(creditCardNumber)


    for i, digit in enumerate(reversed(creditCardNumber)):
        if (i + 1) % 2 == 0:
            double = int(digit) * 2
            if double > 9:
                double = double - 9
            sum += double
        else:
            sum += int(digit)

    return sum % 10 == 0

print(f"Credit Card Number: {creditCardNumber}")
print(f"Valid: {luhnAlgorithm(creditCardNumber)}")