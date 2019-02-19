#Exercise1

emotions = {
	'Happiness': 3,
	"Fear": 1,
	"Saddness": 2
}   

#------------------------
#Exercise2

class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		self.name = name
		self.emotions = emotions



	def __str__(self):
		return "{} is feeling a high amount of {}.".format(self.name, self.emotions)


#Exercise3
	def feeling_moment(self):
		for feelings, level in emotions.items():
			if level == 1:
				self.emotions = "Fear"


			elif level == 2:
				self.emotions = "Saddness"
				

			elif level == 3:
				self.emotions = 'Happiness'
				 


Human = Person('Josh')
Human.feeling_moment()
print(Human)

