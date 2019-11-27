import random
import time

def age_limit(age): # asks for age in arguement.
  AGE_Req = 13 # required age is 13.
  if age < AGE_Req: # Check if age is below the required age amount of 13.
    print age, "is below the required age" # print that the age is below required age.
  else:
    print age, "is old enough." # print that age is old enough.
  print " Minimum AGE IS", AGE_Req #print final statement 
  

# TASK 1. Create report grade function to tell you if you are good or bad.

def rep_grade(percent):
  Good = 95 # good percent = 95
  if percent >= Good: #checks if percent is greater or equal to the rate of Good
    print "A grade of", percent, "% indicates mastery in Kaushik's World"
    print "Keep up the good work and try to go further." #then prints you have done good.
  else:
    print "A grade of", percent, "% indicates that you failed this class." # else, you will have bad percent.
    print "To achieve mastery, you need a percent of 95 or higher." # prints that you are bad. 
    print "Seek help or practice."

#Part 3

def vowel(word): # asks for the word. 
  vow = 'aeiouAEIOU' # what are in vowels.
  if word in vow: #check if word has any of the following letters.
    return True
  else:
    return False

#TASK 2. Create letter in word function

def l_i_w(letter, word): # asks for letter and the word.
  if letter in word: #check if the letter is in the word.
    return True
  else:
    return False
  
#TASK 3. Create a sequence color function?

secret = ['red','red','yellow','yellow','black'] # list of colors.
def hint(color, LIST):
  if color in LIST:
    print("The color", color, "is in the secret sequence of colors.") # same as the functions above.
  else:
    print("This either is not in sequence of colors or is not a color at all :(")
