# Py Test Problems

# Task 1
def is_palindrome(string): #Defining Function
  palindrome = string[::-1] # This will reverse the order of letters in string ---> Palindrome
  if palindrome == string: #check if the following string matches original string.
    return True 
  else: # Else false.
    return False
# Task 2
def num(n_list, limit): #Get list of numbers, and the limit.
  for i in n_list: # for i in each number of list.
    if i > limit: # if i is greater than limit.
      print i, # print i. the comma is to make the output appear like this --> 1 2 4 

# Task 3

def aven(n_list): #get list of numbers
  numList = [] # Empty list of even numbers that are to be appended.
  tot = 0.0 # tot = 0
  var = 0 # var = 0
  for i in n_list: # for each in the list.
    if i%2 == 0: # if %2 == 0, then it is even.
      numList.append(i) # add the numbers to the list.
  for a in numList: # for a in each number is list.
    tot = tot + a # tot = tot + a
    var = var + 1 # var will be the total amount of even numbers.
  tot = tot/var # divide tot by var to get new tot.
  return tot # return final answer.
  
