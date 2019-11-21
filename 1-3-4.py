import random
import time

#PART 1
def food_id(food):
  if food in fruits:
    if food in citrus:
      return 'Citrus, Fruit'
    else:
      return 'Fruit'
  else:
    if food in starchy:
      return 'Starchy, NOT FRUIT'
    else:
      return 'Fruit'
fruits = ['apple', 'banana', 'orange']
citrus = ['orange']
starchy = ['banana', 'potato']
def food_id_test():
  works = True
  if food_id('orange') != 'Citrus, Fruit':
      works = False
      print('orange bug in food id()')
  if food_id('banana') != 'Starchy, Fruit':
      works = False
      print('banana bug in food_id()') 
  if works:
      print('food_id passed all tests')
      return works

# Part 2
 
def guess_once():
  secret = random.randint(1, 4)
  print 'I have a number between 1 and 4.' 
  guess = int(raw_input('Guess: ')) # Why can't we use input() Mr Dably?
  if guess != secret:
      print 'Wrong, my number is ', secret, '.',
  else:
      print 'Right, my number is', guess, '!'  

def guess_once_m(): #MODIFIED
  secret = random.randint(1, 4)
  print 'I have a number between 1 and 4.' 
  guess = int(raw_input('Guess: ')) # Why can't we use input() Mr Dably?
  if guess != secret:
      if guess > secret:
        print 'Too high... My number was', secret
      else:
        print 'Too low... My number was', secret
  else:
      print 'Right, my number is', guess, '!'

# TASK: Create a quiz decimal(low, high)
def quiz(low, high):
  print 'What can be between', low, 'and', high
  answer = float(raw_input('Type the number:'))
  if answer > low:
    if answer < high:
      print "Correct", low, '<', answer, '<', high
    else:
      print "No,", answer, 'is greater than', high
  else:
    print "No,", answer, 'is lesser than', low
