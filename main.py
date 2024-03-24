# THIS PYTHON IS FOR PYTHON 2.01
# This was found at https://annedawson.net/pythonprograms.txt
# Comments was added by me, no changes to code was made to this file

total = 0.0
# raw_input is no longer a function in Python 3.x
# It was replaced by input(...)
number1=float(raw_input("Enter the first number: "))
total = total + number1
number2=float(raw_input("Enter the second number: "))
total = total + number2
number3=float(raw_input("Enter the third number: "))
total = total + number3
average = total / 3
# Print syntax was changed to a function
# print(...)
print "The average is " + str(average)