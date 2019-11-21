import random, time


username = ""
players = ['Thomas', 'John','ERROR', 'Jay', 'Kaushik', 'DanieldDably', 'Jone', 'Clara', 'Jane', 'Chakra', 'DeLawd', 'Charles','Eshaan']
# JUST SOME VARIABLES ON TOP THAT ARE USED IN THE FUNCTION

def game():
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  bdic1 = random.randint(1,6)
  bdic2 = random.randint(1,6)
  goal = random.randint (2, 12)
  player = random.choice(players)
  global username
  #print "Enter your name:"
  #username = raw_input(">>> ")
  #time.sleep(1)
  #print "Starting Game:"
  #time.sleep(1)
  #print ""
  #print ""
  #print ""
  print "Your are playing against", player
  #time.sleep(1)
  #print "Reach the Goal!"
  #time.sleep(1)
  print ""
  print "GOAL: ", goal
  print ""
  raw_input("Enter to roll two dice:")
  print ""
  print "Rolling Two Dice... "
  print ""
  time.sleep(1)
  print "First dice rolls a: ", dice1
  time.sleep(1)
  print "Second dice rolls a: ", dice2
  die = dice1+dice2
  time.sleep(1)
  print ""
  print "You have a total of: ", die
  time.sleep(1)
  print ""
  print player, "is rolling dice."
  print ""
  time.sleep(1)
  print "First dice rolls a: ", bdic1
  time.sleep(1)
  print "Second dice rolls a: ", bdic2
  print ""
  bdie = bdic1+bdic2
  time.sleep(1)
  print player+"'s total is:", bdie
  if die == goal:
    print "Your goal matches total. You win."
  elif bdie == goal:
    print player+"'s total matches goal. "+player+" wins."
  else:
    if bdie > die:
      print player+" has a higher number than you. "+player+" wins."
    elif bdie < die:
      print "You have a higher number than "+player+". You win."
    else:
      print "Results are tied."

# Kaushik
