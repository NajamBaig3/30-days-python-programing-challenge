def min_max(numbers):
    if not numbers:
        return None

    smallest = largest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return smallest, largest

# Example usage:
user_list = [int(x) for x in input("Enter numbers separated by space: ").split()]
result = min_max(user_list)
print("Smallest number:", result[0])
print("Largest number:", result[1])
