import random
import time

def age_limit(age):
  AGE_Req = 13
  if age < AGE_Req:
    print age, "is below the required age"
  else:
    print age, "is old enough."
  print " Minimum AGE IS", AGE_Req
  

# TASK 1. Create report grade function to tell you if you are good or bad.

def rep_grade(percent):
  Good = 95
  if percent >= Good:
    print "A grade of", percent, "% indicates mastery in Kaushik's World"
    print "Keep up the good work and try to go further."
  else:
    print "A grade of", percent, "% indicates that you failed this class."
    print "To achieve mastery, you need a percent of 95 or higher."
    print "Seek help or practice."

#Part 3

def vowel(letter):
  vow = 'aeiouAEIOU'
  if letter in vow:
    return True
  else:
    return False

#TASK 2. Create letter in word function

def l_i_w(letter, word):
  if letter in word:
    return True
  else:
    return False
  
#TASK 3. Create a sequence color function?

secret = ['red','red','yellow','yellow','black']
def hint(color, LIST):
  if color in LIST:
    print("The color", color, "is in the secret sequence of colors.")
  else:
    print("This either is not in sequence of colors or is not a color at all :(")
