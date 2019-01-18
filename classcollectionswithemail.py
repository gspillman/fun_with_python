import datetime

#Here's an example of a class: 

def Player:
	lives = 3
	score = 0
	order = 1
	rank = 100
	@property
	def get_score(self):
		return self.score
	@property
	def dies(self):
		self.lives -= 1
		return self.lives
	#test2 is a keyword argument (AKA, its optional)	
	def update_player(self, test1, test2=None):
	    self.score += 1000
	    print test1
	    if test2 != None:
	    	lives += 1
	    	return self.score

player1 = Player()
player2 = Player()

player1.dies
player2.get_score

#Here's a complex class with getters and setters:

class MessageUsers():
	user_details = []
	messages = []
	base_message = """Hello {name}!  Your total is {total}"""

	def set_user(self, name, amount):
		#formats the first character in name to upper case and the remaining characters to lower
		name = name[0].upper() + name[1:].lower()
		amount = "%.2f" %(amount)
		detail = {
			"name": name,
			"amount": amount,
		}
		#create today as a variable containing the date and formatting it
		today = datetime.date.today()
		date_text = '{today.month}/{today.day}/{today.year}'.format(today = today)
		#appending date text to the detail dictionary
		detail['date'] = date_text
		#appends the current details to the user details list
		self.user_details.append(detail)
	def set_messages(self):
		if len(self.user_details) > 0:
			for detail in self.get_details():
				name = detail["name"]
				amount = detail["amount"]
				date = detail["date"]
				message = self.base_message
				new_message = message.format(
					name=name,
					date=date,
					total=amount
				)
				self.messages.append(new_msg)
			return self.messages
		return []		
	def get_details():
		return self.user_details

obj = MessageUsers()

obj.set_user("Joe", 123.22)
obj.set_user("Jane", 998.23)
obj.set_user("Billy", 12.88)
obj.get_details()
obj.set_messages()

