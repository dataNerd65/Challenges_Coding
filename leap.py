def is_leap(year):
    #Initializing year as False
    leap = False

    #Logic
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    #Remember to return the bool as a result of the function
    return leap#Return statements should be outside loops be keen next time.
#Review your code everytime you finish
year = int(input("Year: "))
print(is_leap(year))