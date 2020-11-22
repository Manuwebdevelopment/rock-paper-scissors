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
choices = [rock, paper, scissors]
user_choice = int(input('What would you like to choose? Type 0 for Rock 1 for Paper and 2 for Scissor\n'))
print(choices[user_choice])

computer_choice = random.randint(0, 2)
print(f'Computer choice\n{computer_choice}')
print(choices[computer_choice])

if user_choice >= 3:
  print("You type and invalid numer, you loose!")
elif user_choice == 0 and computer_choice == 2:
  print('You win')
elif computer_choice == 0 and user_choice == 2:
  print("You loose!")
elif computer_choice > user_choice:
  print('You loose')
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw!")


