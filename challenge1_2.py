#check the given year is leap or not

#Taking the input form the user
year=int(input("Enter the year:"))

#check whether is leap or not using if-elif-else statement
if year%4==0 and year%100!=0:
  print("The {} year is leap year".format(year))
elif year%400==0:
  print("The {} year is leap year ".format(year))
else:
  print("The {} year is not leap year ".format(year))
  
