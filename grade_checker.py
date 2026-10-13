# ask the user to input a numeric grade (0-100) 
grade = int(input("Enter grade (0-100): "))

# perform the check and reports the grade.
if grade >= 90:
    print("Your grade is: A!")
elif grade >= 80:
    print("Your grade is: B!")
elif grade >= 70:
    print("Your grade is C!")
elif grade >= 60:
    print("Your grade is: D.")
else:
    print("Your grade is: F.")

#  if the grade is passing (A-C) congradulate the user, if it is a D or F, encourage them to try again
if grade >= 70:
    print("Congratulations! You passed!")
else:
    print("Keep trying! You can do it!")