import math

# Define the constant for the value of PI
PI = math.pi

# Function to calculate circumference
def calculate_circumference(radius):
    return 2 * PI * radius

# Get user input for the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate circumference
circumference = calculate_circumference(radius)

# Print the result
print("The circumference of the circle is:", circumference)