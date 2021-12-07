# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
rand_num = random.randint(0,len(names)-1)
# print(type(rand_num))
#print(f"{names[rand_num]} is going to buy the meal today!")
print(f"{random.choice(names)} is going to buy the meal today!")

