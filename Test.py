def divideNos(num1, num2):
    # Assert keyword to make sure the second number is greater than zero
    assert num2 > 0, "The divisor must be greater than zero, Zero division error"

    # calculation REMEMBER TO give descriptive variable names 
    quotient =  num1 / num2

    return print(f"Quotient is: {quotient}")

# Calling the function twice for testing
divideNos(12, 3)
divideNos(12, 0)