import random
import time 
# Imported Modules

def add_tip(total, tip_percent): # asks for two variables. 'total' and the 'tip' percent.
  tip = tip_percent*total # multiplies the tip_percent to total to find out how the tip is worth.
  return total+tip #adds the tip to the total and returns the amount.

# Task 1: Create a function that solves for Hypotenuse
def hyp(legA, legB): # asks for two variables. 'leg1' and the 'leg2' percent.
  tot = (legA**2) + (legB**2) # Squares both legs and adds them together to find 'tot'
  tot2 = tot**0.5 # square root of tot to find tot2. Then returns tot2 as the hypotenuse
  print "Out[]: The square root of this right triangle with legs", legA, "and", legB, "is", tot2

# Task 2: Create function to solve mean of three numbers.
def find_mean(a, b, c): #ENTER THREE NUMBERS
  tot = a + b + c # adds all numbers togther to get tot.
  mean = tot/3. # divides tot by 3. to get mean.
  print "Out[]: The mean of these three numbers is", mean # returns mean.

# Task 3: Create function to find perimeter of a rectangle.
def perimeter(base, height):
  perm = (2*base) + (2*height) # multiplies hieght by 2, repeat for base and then add them all together as perm
  print "Out[]: The perimeter of this rectangle is", perm # returns perm.
  
  # Kaushik
