# Loops and things

beans_and_spam = ["spam","spam","beans","spam","spam","spam","beans","spam","spam","spam","spam","beans","spam",]
	
x = len(beans_and_spam)
y = 0

# For loop

for item in beans_and_spam:
  if item == "beans":
    y ++

print(y)

my_list[1,2,-3,5]

for i in my_list:
	if i < 0:
		print("There's a negative number in the list")
	elif i == 3:
		print("there's a three in here too")
		
# This returns false:

isinstance(3.1424, int)

# Functions!!!

buncha_string = ["abc", "DEF", "book", "Record", "bacon sandwich"]

# This sorts the list in reverse order, lower case last

print(buncha_string.sort(key=str.lower, reverse=True))
	  	
def parseLists(list):
  num_list = []
  str_list = []
  for i in list:
    if isinstance(i, int):
      num_list.append(i)
    elif isinstance(i, str):
      str_list.append(i)
    else:
      print("Found an item in the list that was neither a string or integer")
  return num_list, str_list      	  	
