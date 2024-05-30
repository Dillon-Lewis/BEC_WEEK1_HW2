# Task 1

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# Task 2

numb = int(input("Enter a number:"))
numb1 = int(input("Enter a 2nd number:"))
numb2 = int(input("Enter a 3rd number:"))

if numb > numb1 and numb > numb2:
    print("The largest number is", numb)
elif numb1 > numb and numb1 > numb2:
    print("The largest number is", numb1)
elif numb2 > numb1 and numb2 > numb:
    print("The largest number is", numb2)
    