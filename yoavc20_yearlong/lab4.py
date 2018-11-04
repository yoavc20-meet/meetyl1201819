#problem1
'''
class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yummy!!" + self.name + " is eating a " + food)
	def description(self):
		print(self.name + " is " + str(self.age) + " years old and loves the color "+ self.favorite_color)
#problem2	
	def make_sound(self):
		print(self.sound * 3)
Brownie = Animal(" woof! ", " Brownie ", 14, "red")
Brownie.eat("chocolate cookie")	
Brownie.description()
Brownie.make_sound()
'''
#problem3
'''
class person(object):
	def __init__(self,name,age,city, gender, fav_food, fav_sport):
		self.gender = gender
		self.name = name
		self.age = age
		self.fav_food = fav_food
		self.city = city
		self.fav_sport = fav_sport
	def eat(self):
		print(self.name + " is eating " + self.fav_food)
	def play_sport(self):
		print(self.name + " is playing " + self.fav_sport)

u = person("Uri", 15, "Jerusalem", "male", "pizza", "Volleyball")

u.eat()

u.play_sport()
'''
#extra
class song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
		self.song_name = song_name
	def lyrics(self):
		print(self.lyrics)

a = song("found myself in a late night drives,",                                              
	"Without a destination",
	"All I had were thoughts about the past",
	"And a list of my favorite songs to keep me company",
	"But I still struggle and lose myself everyday",
	"I always find myself lost in every line of all these songs",
	"But I felt better when I saw that this is life",
	"And in life were gonna cry",
	"In life were gonna lose sleep",
	"Were gonna feel helpless",
	"But thats how its got to be ",
	"When you lose yourself youll find what youre looking for",
	"I am growing past who I used to be" )
a.lyrics()