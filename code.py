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
import random
image = [rock,paper,scissors]
user = int(input("What do you chose? 0 for rock, 1 for paper, 2 for scissors\n"))
print(image[user])
comp = random.randint(0,2)
print(image[comp])


if user == 1 and comp == 2 :
    print("You Lose")
elif user ==0 and comp==1 :
    print("You Lose")
elif user == 2 and comp== 0 :
    print("You Lose")
elif user == comp:
    print("Draw")
elif user == 2 and comp == 2 :
    print("You  Won")
elif user ==1 and comp==0 :
    print("You  Won")
elif user == 0 and comp== 2 :
    print("You  Won")
else:
    print("Invalid")

