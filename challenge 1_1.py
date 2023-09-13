#Find the Factorial of a given number

#defining the function for factorial
def factorial(number):
  if number==1 or number==0:
    return 1
  else:
    return number*factorial(number-1)

#Taking the input from the user
number=int(input("Enter the integer number:"))

if number<0:
  print("Factorial of negative number is not defined")
else:
  value=factorial(number)
  
#print the factorial of given number
  print("Factorial of {} is {}".format(number,value))
  