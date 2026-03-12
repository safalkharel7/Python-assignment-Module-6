def conv():
    litres = gallons * 3.78541
    return litres
gallons = float(input("How many gallons would you like to convert to litres?: "))
if gallons >= 0:
    litres = conv()
    print(f"\n{gallons} gallons is equivalent to {litres: 0.4f} litres")
else:
    print("\nPlease enter a positive value")