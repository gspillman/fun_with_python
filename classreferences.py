#importing from same level

from classcollections import MessageUsers

#note - you can import from another directory by adding a __init.py__ to a given directory

obj = MessageUsers()

obj.set_user("Toby", 89.98)
obj.set_user("Carl", 23.99)
obj.set_user("David", 1092.22)

print(obj.set_messages())


