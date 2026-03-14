import math #import math for pie to calculate area of pizza.
def pizza_price(price, size):
    radius_in_meter = size / (2 * 100)   #1 cm = 1/100 m & radius = diameter/2
    radius = radius_in_meter
    area = radius**2 * math.pi          #gives area is meter square
    price_square_meter = price / area   #price per square meter = price/area(m**2)
    return price_square_meter           #returns price_square_meter value
price = float(input("Enter a price: "))   #asks for price and stores as float
size = float(input("Enter the diameter of pizza in centimeters: ")) #asks the diameter size
price_square_meter = pizza_price(price, size)   #function called for computation.
print(f"\nThe price per meter square for the given pizza is: {price_square_meter:0.4f}")