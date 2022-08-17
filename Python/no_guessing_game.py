# 1. Create a number guessing game.
import random

# a function to get users guess
def get_guess():
    guess=int(input('Enter your guess: '))
    return guess

def guide(diff):
  print(diff)
  rt=""
  if abs(diff) == 9 or abs(diff) == 8:
    rt+='very cold'
  elif abs(diff) == 7 or abs(diff) == 6:
    r+='cold'
  elif abs(diff) == 5 or abs(diff) == 4:
    rt+='neutral'
  elif abs(diff) == 3:
    rt+='warm'
  elif abs(diff) == 2:
    rt+='hot'
  elif abs(diff) == 1:
    rt+='very hot'
  
  if diff > 0:
    rt+=' from left'
  else:
    rt+=' from right'
  return rt

def game(num,trial):
  print("I've already guessed...")
  while(trial<6):

    guess=get_guess()
    if guess==num:
      print('You guessed it. Congratulations!')
      break
    else:
      diff=guess-num
      print("you are %s .Try again" % guide(diff))

    trial+=1
  if trial==6:
    print("You failed. The number was %d" % num)

# a menu to with start game and exit options
def menu():
    print('1. Play Game')
    print('2. Exit')
    print('\n')
    choice=input('Enter your choice: ')
    return choice

while(1):
  c= menu()
  if c== '2':
    break
  elif c=='1':
    num=random.randint(1,10)
    game(num,1)
  else:
    print('Invalid choice')
    continue


