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
user_choice=int(input("What do you choose?Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice==0:
    print(rock)
elif user_choice==1:
    print(paper)
else:
    print(scissors)
print("Computer chose:")
computer_choice=random.randint(0,2)
print(computer_choice)
if computer_choice==0:
    print(rock)
elif computer_choice==1:
    print(paper)
else:
    print(scissors)
if computer_choice==user_choice:
    print("It's a draw")
elif user_choice==0 and computer_choice==1:
    print("You lose")
elif user_choice==0 and computer_choice==2:
    print("You win!")
elif user_choice==1 and computer_choice==0:
    print("You win!")
elif user_choice==1 and computer_choice==2:
    print("You lose")
elif user_choice==2 and computer_choice==0:
    print("You lose")
elif user_choice==2 and computer_choice==1:
    print("You win!")
