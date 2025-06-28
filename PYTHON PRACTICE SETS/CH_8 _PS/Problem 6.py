def inches_to_cm(inches):
    return inches * 2.54

# Taking user input
inches = float(input("Enter length in inches: "))
print(f"{inches} inches is equal to {inches_to_cm(inches)} cm")