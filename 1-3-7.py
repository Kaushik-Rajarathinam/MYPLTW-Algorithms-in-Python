# Creator's Note:
# 
# 1-3-7.py is different than the rest of the files. I have created it more like a mini module.
# Contains 4 functions that are tasks in 1.3.7
# BONUS function --> bonus credit --> lottery()
# All resources are free here, except hangman() due to this function can be easily classifed as plagirised if copied.

#---------------------------------------------------------------------------------------------------------------------------------------

import random
import time

class Error(Exception):
  pass

class BadWordError(Error):
  pass

class DablyError(Error):
  pass

# IGNORE ABOVE ASCII ART BELOW
hang = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
verCode = ['DanieldDably', 'EOF','SOP','GFD','NIGA','DOG','MON','NIG','SOA','IGL','CHA','KRA','JOE','NOA','KYL','RAM'] # Verification Codes
players = ['DanieldDably', 'Chakra', 'Kaushik', 'Joe', 'Noah', 'Ethan', 'James', 'Pablo', 'Eshaan', 'Tomas', 'Thomas', 'Temur', '666'] # Players
words = ['chakra','joe','noah','dably','python','eshaan','zeroparticipation','monkey','horrible','danielddably', 'chicken','minecraft','krunker','god','sellpoints','dablymad','spritecranberry','ghost','ransom','biology','computerscience','man','sam','ashfuahisaojhahjfhafjsdhnjkncvskudhgtoeuashfoehawifhsihawofihiwhafoihajghkjashbghagaowf']
# words used for hangman
badWord = ['nigger','faggot','fuck','bitch','Nigger','Fuck','Bitch','Faggot'] # This is my client, and I don't like bad words.
# Bad Word filter is not accurate.. and it will not be fixed soon.

scram = False
total = 0

print "You have loaded CorporalSins's Shell V.1.3.7"
print ""
print "To make this more interesting, tell us your name: "
while scram != True:
  try:
    time.sleep(0.1)
    name = raw_input("NAME: ")
    if name == badWord[0]:
      raise BadWordError
    elif name == badWord[1]: # BADWORD FILTER
      raise BadWordError
    elif name == badWord[2]:
      raise BadWordError
    elif name == badWord[3]:
      raise BadWordError
    elif name == badWord[4]:
      raise BadWordError
    elif name == badWord[5]:
      raise BadWordError
    elif name == badWord[6]:
      raise BadWordError
    elif name == badWord[7]:
      raise BadWordError
    elif name == 'Dably': # DABLY FILTER
      raise DablyError
    else:
      scram = True
  except BadWordError:
    print "BadWordError --> True Dably Army men don't use curse words."
    print ""
  except DablyError:
    print "DablyError --> Mr.Dably has rejected your name."
    print ""
  

time.sleep(0.1)
print ""
print "Okay "+name+". The console is ready, type cmds() to see all commands."

def cmds():
  print "Commands:"
  print "roll(number) --> Rolls 'number' 6-sided dices and gives total. Occasional lag to solve big numbers."
  print "hangman() --> Play Hangman."
  print "Lottery() --> Lottery Pick's random numbers. Can you win the prize?"
  print "goguess() --> Play Guess the number game!"
  print ""
  print "Functions:"
  print "gameResults() --> Function Part of Lottery()"
  print "dice() --> Function Part of roll()"

def goguess():
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

def dice():
  global total
  dic1 = random.randint(1,6)
  total = total + dic1
def roll(number):
  global total, badWord
  try:
    if number == badWord[0]:
      raise BadWordError
    high = number
    number = range(number)
    for i in number:
      dice()
    print "Dice:",high
    print "You rolled:", total
    total = 0
  except OverflowError:
    print "OverFlowError --> Your number make calculators explode."
  except BadWordError:
    print 'BAD WORDS?'


guess = ""
word = ""
guesses = ""
def hangman():
  global word, guesses, guess
  print "Hello, " + name, "Everything here are from computer science class."
  print "and the stuff that happen are sure to be funny. ALL LETTERS IN LOWERCASE."
  print "Lets start!"
  print ""
  time.sleep(1)
  print "Loading..."
  print ""
  time.sleep(0.5)
  word = random.choice(words)
  guesses = ''
  turns = 6
  print hang[0]
  while turns > 0:
    try:
      failed = 0             
      for i in word:      
          if i in guesses:     
              print i,    

          else:    
              print "-",     
              failed = failed+1     
      if failed == 0:        
          print ""
          print "Correct Phrase!!"        
          break              
      print
      guess = raw_input("guess a character:") 
      guesses += guess                    
      if guess not in word:
        
        turns -= 1
        if turns == 6:
          print hang[0]
        if turns == 5:
          print hang[1]
        if turns == 4:
          print hang[2]
        if turns == 3:
          print hang[3]
        if turns == 2:
          print hang[4]
        if turns == 1:
          print hang[5]

        print "Nope!"    
        print "You have", + turns, 'more guesses' 
        if turns == 0:
          print hang[6]
          print "The phrase was", word
      else:
        if turns == 6:
          print hang[0]
        if turns == 5:
          print hang[1]
        if turns == 4:
          print hang[2]
        if turns == 3:
          print hang[3]
        if turns == 2:
          print hang[4]
        if turns == 1:
          print hang[5]
    except KeyboardInterrupt:
      print "KeyboardInterrupt --> Sorry, we denied this interruption."
    except EOFError:
      print "EOFError --> Sorry, we denied this interruption."

cashprize = str(random.randint(100000,500000))
prize = "$"+cashprize
def lottery():
  global cashprize, prize
  cashprize = str(random.randint(100000,500000))
  prize = "$"+cashprize
  verify = False
  password = random.choice(verCode)
  while verify != True:
    try:
      print "reCAPTCHA: Type in this code EXACTLY '"+password+"'"
      check = raw_input("CODE: ")
      if check == password:
        verify = True
      else:
        print "RejectedPrompt --> You typed '"+check+"'."
        print "RequestedPrompt: '"+password+"'"
        print ""
    except KeyboardInterrupt:
      print "KeyboardInterrupt --> Sorry, we denied this interruption."
      print ""
    except EOFError:
      print "EOFError --> Sorry, we denied this interruption."
  booked = False
  
  print "CSPDably Lottery Pooled Prize: "+prize
  while booked != True:
    try:
      no = input("|| Enter your ticket number[1-50]: ")
      if no > 50:
        print "RejectedPrompt --> Number is not right."
      elif no <1:
        print "RejectedPrompt --> Number is not right."
      else:
        booked = True
    except NameError:
      print 'NameError --> Please enter a digit'
    except SyntaxError:
      print 'SyntaxError --> Invalid Prompt'
    except EOFError:
      print 'EOFError --> Sorry, we denied this interruption.'
    except KeyboardInterrupt:
      print "KeyboardInterrupt --> Sorry, we denied this interruption."
  over = False
  while over != True:
    num1 = random.randint(1,50)
    num2 = random.randint(1, 50)
    if num2 == num1:
      num2 = num2-1
    num3 = random.randint(1,50)
    if num3 == num2:
      num3 = num3 -1
    num4 = random.randint(1,50)
    if num4 == num3:
      num4 = num4-1
    num5 = random.randint(1,50)
    if num5 == num4:
      num5 = num5-1
    print ""
    print "Contestants are joining..."
    time.sleep(random.randint(1,2))
    print ""
    print "Starting Round..."
    time.sleep(1)
    print "Your Number: [",no,"] (Don't KeyboardInterrupt)"
    time.sleep(1)
    print "Rolling numbers!!!"
    time.sleep(1)
    print ""
    print "First Number -->",num1
    if num1 == no:
      time.sleep(1)
      print "You have won the lottery!"
      print "DING DING DING! "+name+" has won "+prize
      over = True
    else:
      time.sleep(1.5)
      print "Second Number -->",num2
      if num2 == no:
        time.sleep(1)
        print "You have won the lottery!"
        print "DING DING DING! "+name+" has won "+prize
        over = True
      else:
        time.sleep(1.5)
        print "Third Number -->",num3
        if num3 == no:
          time.sleep(1)
          print "You have won the lottery!"
          print "DING DING DING! "+name+" has won "+prize
          over = True
        else:
          time.sleep(1.5)
          print "Fourth Number -->",num4
          if num4 == no:
            time.sleep(1)
            print "You have won the lottery!"
            print "DING DING DING! "+name+" has won "+prize
            over = True
          else:
            time.sleep(1.5)
            print "And Final Number -->", num5
            if num5 == no:
              time.sleep(1)
              print "You have won the lottery!"
              print "DING DING DING! "+name+" has won "+prize
              over = True
            else:
              over = True
              gameResults()

def gameResults():
  time.sleep(1)
  print "Unfortunate! You haven't had a chance!"
  time.sleep(1)
  plawin = random.randint(1,5)
  if plawin == 1:
    print "In the round, a winner has been announced."
    winner = random.choice(players)
    time.sleep(1.5)
    print winner+" has won the prize of "+prize+"!!!"
  else:
    print "Other contestants haven't won either."
    print "Buy a ticket and enter lottery --> lottery()"
    
def start():
  print ""

# FINAL DEFINITIONS

Lottery = lottery
ROLL = roll
Roll = roll
Hangman = hangman
HANGMAN = hangman
