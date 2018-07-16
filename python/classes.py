class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
			self.sound = sound
			self.name = name
			self.age = age
			self.favorite_color = favorite_color
	def eat(self,food):
			print("Yummy!" + self.name + " is eating " + food)
	def description(self):
			print(self.name + " is " + self.age + " years old and loves the color " + self.favorite_color)
	def make_sound(self,X):
		for i in range(X):
			print (self.sound)
class Person(object):
	def __init__(self,name,age,city,gender):
			self.name = name
			self.age = age
			self.city = city
			self.gender = gender
	def eat(self,favorite_breakfast):
			print(self.name + " is eating " + favorite_breakfast)
	def play(self,favorite_sport):
			print(self.name + " is playing " + favorite_sport)
class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		song_lyrics = ["roses are red","violets are blue","I wrote this poem for you"]
		for i in range(3):
			print song_lyrics[i]
s = Song("iuhj")
s.sing_me_a_song()



# d = Animal("HAW","DOG","3","purple")
# d.eat("bones")
# d.description()
# d.make_sound(4)
# h = Person("Hamza","14","Nablus","Male")
# h.eat("pancake")
# h.play("basketball")
