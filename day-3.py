#program that interprets the Body Mass Index (BMI) based on a user's weight and height.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

res = round(weight / height ** 2)
#print(res)

if res < 18.5:
    print(f"Your BMI is {res}, you are underweight.")
elif res < 25:
    print(f"Your BMI is {res}, you have a normal weight.")
elif res < 30:
    print(f"Your BMI is {res}, you are slightly overweight")
elif res < 35:
    print(f"Your BMI is {res}, you are obese")
else:
    print(f"Your BMI is {res}, you are clinically obese")