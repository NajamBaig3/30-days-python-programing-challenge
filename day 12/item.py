# Define a function to use as the key for sorting
def sort_by_second_item(t):
    return t[1]

# Example list of tuples
list_of_tuples = [(1, 5), (2, 3), (3, 8), (4, 1), (5, 6)]

# Sort the list of tuples by the second item in each tuple
sorted_list = sorted(list_of_tuples, key=sort_by_second_item)

# Print the sorted list
print("Sorted list of tuples by the second item:")
for item in sorted_list:
    print(item)
