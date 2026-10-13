# Use a list of unsorted integers (you can use a fixed example list like [64, 25, 12, 22, 11] or a list of random numbers).
num_list = [64, 25, 12, 22, 11]
# Implement the bubble sort algorithm using nested loops:
# Loop through the list elements, and for each element, loop through the list again comparing adjacent pairs.
for i in range(len(num_list)):
    for j in range(0, len(num_list) - i - 1):
# Swap elements if they are in the wrong order.
        if num_list[j] > num_list[j + 1]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
# Continue until the list is sorted.
# Print the list at each pass of the outer loop to show the progress of the sorting.
        print(f"Pass {i + 1}: {num_list}")
# Print the sorted list.
print(f"Sorted list: {num_list}")