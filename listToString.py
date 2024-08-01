# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
	# Assertion to check that the length and width are positive
	assert length > 0 and width > 0, "Length and width must be positive"
	# Calculation of the area
	area = length * width
	# Return statement
	return area


# Calling the function with positive inputs
area1 = calculate_rectangle_area(5, 6)
print("Area of rectangle with length 5 and width 6 is", area1)

# Calling the function with negative inputs
area2 = calculate_rectangle_area(-5, 6)
print("Area of rectangle with length -5 and width 6 is", area2)
