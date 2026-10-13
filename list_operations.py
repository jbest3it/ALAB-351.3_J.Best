org_list = []

# create a list of at least 5 integers from user input
print("Enter 5 numbers:")
for i in range(5):
   
    num = int(input(f"Enter number {i+1}: "))
    org_list.append(num)

# print the original list.
print(f"Original list: {org_list}")

# use the built-in sorted() function to print a sorted version of the list without modifying the original list.
print(f"Sorted list: {sorted(org_list)}")

# use the list’s .sort() method to sort the list in place, then prints the list to show it is now sorted.
org_list.sort()
print(f"List after in-place sorting: {org_list}")

# add a new element to the list (append an integer), then prints the updated list.
org_list.append(9)
print(f"List after appending 9: {org_list}")

# remove an element from the list (you can remove by value or index), then prints the list again.
del org_list[3] 
print(f"List after removing item number 4: {org_list}")

# use the reverse() method to reverse the list, then prints the reversed list.
org_list.reverse()
print(f"List after reversing: {org_list}")