def calculate_sum_and_difference(num1, num2):
    sum_result = num1 + num2
    difference_result = num1 - num2
    return sum_result, difference_result

# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate sum and difference
sum_result, difference_result = calculate_sum_and_difference(num1, num2)

# Print the results
print("Sum:", sum_result)
print("Difference:", difference_result)