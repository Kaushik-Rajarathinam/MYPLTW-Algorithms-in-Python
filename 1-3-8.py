# 1.3.8
import random
import time

def beyond():
  count = 1
  while count != -1: # a random while loop condition that won't stop.
    print "To Infinity and beyond! Miles: ", count #Goes on forever.
    count += 1

def bbeyond():
  count = 0
  while count != -1:
    count +=1
    if count%5 ==0: # check if any number divided by 5's reminder is 0.
      time.sleep(0.5) 
      print "To Infinity and beyond! Miles: ", count

def numero():
  number = 0
  corrupted = False #CORRUPTED = False
  while corrupted == False: # Condition of corrupted.
    number = random.randint(1, 100)
    if number != 20:
      print "Number: ",number # print the number
    else:
      print "Number:  20 has killed the program." # print this when number = 20
      corrupted = True
  print random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1) # Random stuff.
  
    
def goguess(): # Guess your number with while loop. 
  number = random.randint(1,20)
  guesses = 0
  found = False
  print "Guess a number for 1 to 20 and see if it matches my number."
  while found == False:
    try:
      answer = input(">>> ")
      if answer == number:
        guesses=guesses+1
        print "You guessed my number in", guesses, "guesses"
        found = True
      elif answer >= number:
        print "Too High"
        guesses=guesses+1
      else:
        print "Too Low"
        guesses=guesses+1
    except NameError:
      print "That's not a number."
    except SyntaxError:
      print "You need to type something!"





