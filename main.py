monthlyInterestRate = 0.0012
totalInterestPaid = 0
totalValuePaid = 0
totalMonths = 0


def simpleInterestCalculator(initialValue, installmentValue):
    global totalMonths, totalInterestPaid, totalValuePaid
    totalMonths += 1
    interest = initialValue * monthlyInterestRate
    totalInterestPaid += interest
    totalValuePaid += (installmentValue + interest)
    initialValue -= installmentValue
    if initialValue < installmentValue:
        return initialValue
    else:
        return simpleInterestCalculator(initialValue, installmentValue)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialValue = 300000
    installmentValue = 7317
    amountLeft = simpleInterestCalculator(initialValue, installmentValue)
    print("-------------------------------------------------------")
    print("Initial Value: ", initialValue, "\nInstallment Value: ", installmentValue, "\nTotal Months: ", totalMonths,
          "\nTotal Value Paid: ", totalValuePaid, "\nTotal Interest Paid: ", totalInterestPaid, "\nAmount Left: ",
          amountLeft)
    print("-------------------------------------------------------")