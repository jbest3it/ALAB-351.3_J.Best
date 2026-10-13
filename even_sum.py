# set variable to hold the sum of even numbers
sum_even = 0
#  use or loop to iterate through the numbers 1 to 50.
for i in range(1, 51):

# calculate the sum of all even numbers in that range.

    if i % 2 == 0:
        sum_even += i

# print the result.
print(f"The sum of even numbers from 1 to 50 is {sum_even}.")

# modify the script to perform the same task using a while loop instead of a for loop
# i = 1
# sum_even = 0
# while i <= 51:
#    if i % 2 == 0:
#        sum_even += i
#    i += 1
# print(f"The sum of even numbers from 1 to 50 is {sum_even}.")