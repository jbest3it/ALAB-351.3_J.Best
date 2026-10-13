# Demonstrates the use of logical operators:
# ask the user for two boolean inputs (True/False or 1/0) and show the results of and, or, and not on those inputs.
bool1 = input("Enter first boolean value (True/False): ")
bool2 = input("Enter second boolean value (True/False): ")
print(f"Logical AND of {bool1} and {bool2} = {bool(bool1) and bool(bool2)}")
print(f"Logical OR of {bool1} and {bool2} = {bool(bool1) or bool(bool2)}")
print(f"Logical NOT of {bool1} = {not bool(bool1)}")
# Demonstrates bitwise operators (&, |, ^, ~, <<, >>) on two small integers (for example, 5 and 3). 
# Print the results in binary form using bin() to show what is happening at the bit level.
int1 = int(input("Enter first integer value (0-5): "))
int2 = int(input("Enter second integer value (0-5): "))
print(f"Bitwise AND of {int1} and {int2} = {int1 & int2} (binary: {bin(int1 & int2)})")
print(f"Bitwise OR of {int1} and {int2} = {int1 | int2} (binary: {bin(int1 | int2)})")
print(f"Bitwise XOR of {int1} and {int2} = {int1 ^ int2} (binary: {bin(int1 ^ int2)})")
print(f"Bitwise NOT of {int1} = {~int1} (binary: {bin(~int1)})")
print(f"Left shift of {int1} by 1 = {int1 << 1} (binary: {bin(int1 << 1)})")
print(f"Right shift of {int1} by 1 = {int1 >> 1} (binary: {bin(int1 >> 1)})")