print(6 + 4 / 2 - (1 * 2))

#char = input("Enter your name:\n")
#count_char = len(char)
#print(type(count_char))
#print("Your name has " + str(count_char) + " characters")

# ******************************************* #

## Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
#a = input("Enter a numer: ")
#b = a[0]
#c = a[1]
#print(int(b)+ int(c))

#print(3 * 3 + 3 / 3 - 3 )

# ******************************************* #

## The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#weight = 80
#height = 1.75
#Ans: 26

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

res = int(weight)/(float(height)*float(height))
print(int(res))

# ******************************************* #
# 56
# You have 12410 days, 1768 weeks, and 408 months left.

## Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
age = input("What is your current age?")

total_year = 90
total_month = 12
total_weeks = 52
total_days = 365
year = int(total_year)-int(age)
days = int(total_days)*int(year)
month = int(total_month)*int(year)
week = int(total_weeks)*int(year)

print(f"You have {days} days, {week} weeks, and {month} months left.")