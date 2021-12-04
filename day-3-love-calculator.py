# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lowercase = name1 + name2.lower()
letter_t = lowercase.count("t")
letter_r = lowercase.count("r")
letter_u = lowercase.count("u")
letter_e = lowercase.count("e")

letter_l = lowercase.count("l")
letter_o = lowercase.count("o")
letter_v = lowercase.count("v")
letter_e = lowercase.count("e")

true_count = letter_t + letter_r + letter_u + letter_e
love_count = letter_l + letter_o + letter_v + letter_e

love_score = int(str(true_count) + str(love_count))

# Pierre Curie
# Marie Curie

# love_score = "10"
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score <= 50 and love_score >= 40:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")