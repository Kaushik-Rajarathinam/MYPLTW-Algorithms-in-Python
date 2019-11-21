import random, time

# Task 1: Create Function how_eligible(essay)


def how_eligible(essay):
  points = 0
  if '.' in essay:
    points=points+1
    if ',' in essay:
      points=points+1
      if '"' in essay:
        points=points+1
        if '!' in essay:
          points=points+1
        else:
          points=points
      else:
        if '!' in essay:
          points=points+1
    else:
      if '"' in essay:
        points=points+1
        if "!" in essay:
          points=points+1
  else:
    if "," in essay:
      points=points+1
      if '"' in essay:
        points=points+1
        if '!' in essay:
          points=points+1
        else:
          points=points
      else:
        if '!' in essay:
          points=points+1
    else:
      if '"' in essay:
        points=points+1
        if "!" in essay:
          points=points+1
        else:
          points=points
      else:
        if '!' in essay:
          points=points+1
  return points

e = how_eligible

# WORK - CREATE A song?
sotng = ('Twinkle Twinkle Little Star, How I wonder what you are. Up above the world so high, Like a diamond in the sky. Twinkle Twinkle Little Star, How I wonder what you are.')
#ABOVE IS SONG
def song():
  print 'str = ', sotng
  print "Line 1:", sotng[0:29]
  print "Line 2:", sotng[29:56]
  print "Line 3:", sotng[56:84]
  print "Line 4:", sotng[84:111]
  print "Line 5:", sotng[111:140]
  print "Line 6:", sotng[140:166]
  print "The lenght of this poem is", len(sotng), "characters long"
# WORK - COLORS OF THE RAINBOW.
def color():
  print "Enter the first color"
  color0 = raw_input(">>> ")
  color0 = str(len(color0))
  print "Enter the second color"
  color1 = raw_input(">>> ")
  color1 = str(len(color1))
  print "Enter the third color"
  color2 = raw_input(">>> ")
  color2 = str(len(color2))
  print "The first color is "+color0+" characters long."
  print "The second color is "+color1+" characters long."
  print "The third color is "+color2+" characters long."
