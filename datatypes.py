# Let's talk about strings

first = "this is a string"

second = "this is " + "another string"

# This multiplies strings (so response will be 'ack ack')

response = "ack " * 2

#Here's an integer: 

myInt = 2 * 10

# This is a list - what Python knows as an array:

list_var = ['test1', 'test2', 'test3', 'test4']

# This removes the last item in a list:

new_list = list_var.pop()

# This returns the list length:

list_length = len(new_list)

# This removes a specific item in the list:

new_list.pop(list_length - 2)

# Dictionaries
new_dict = {
	"one": "a word",
	"two": "another word",
	"three": "a third word"
}

# You can now retrieve a value based on a key from a dictionary: 

single_value = new_dict["two"]

# Dictionaries can hold other dictionaries or lists and lists vice versa

# Tuples > Basicall a data type that is a pair (or a pair of pairs):

tup( 'one', 'two')

complex_tup(
	("going", "going"),
	("back", "back"),
	("to cali", "cali")
)

new_string = complex_tup[2][1]

# new_string in this case should return as 'cali'

