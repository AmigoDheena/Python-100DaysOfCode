import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
rps = [rock,paper,scissors]
user_ans = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_ans = random.randint(0,2)
print((rps[int(user_ans)]))
print(rps[computer_ans])

if user_ans == 0 and computer_ans == 1:
  print("You Win")
elif user_ans == 1 and computer_ans == 0:
  print("You Win")
elif user_ans == 2 and computer_ans == 1:
  print("You Win")
elif user_ans == computer_ans:
  print("It's Draw")    
else:
  print("Please Enter valid number")