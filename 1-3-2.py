import random
import time 
# Imported Modules

def add_tip(total, tip_percent):
  tip = tip_percent*total
  return total+tip

# Task 1: Create a function that solves for Hypotenuse
def hyp(legA, legB):
  tot = (legA**2) + (legB**2)
  tot2 = tot**0.5
  print "Out[]: The square root of this right triangle with legs", legA, "and", legB, "is", tot2

# Task 2: Create function to solve mean of three numbers.
def find_mean(a, b, c): #ENTER THREE NUMBERS
  tot = a + b + c
  mean = tot/3.
  print "Out[]: The mean of these three numbers is", mean

# Task 3: Create function to find perimeter of a rectangle.
def perimeter(base, height):
  perm = (2*base) + (2*height)
  print "Out[]: The perimeter of this rectangle is", perm
  
  # Kaushik
