class Animal(object):
	def __init__(self,name,species,age,favorite_color):
		self.name = name
		self.species = species
		self.age=age
		self.favorite_color=favorite_color

class Cat(Animal):
	def MEOW(self,sound):
		print(sound + "!" + " my name is " + self.name )
class Bird(Animal):
		def intro(self,species):
			print("I'm a " + species)
class Chicken(Bird):
	def BAQ(self,sound):
		print(sound + "!" + " my name is " +self.name)
	def Ability(self,ability):
		print("OH,I "+ability + " Fly")
class Dove(Bird):
	def HOO(self,sound):
		print(sound + "!" + " my name is " + self.name)
	def Ability(self,ability):
		print("HAH,I " + ability + "Fly")

# tommy = Cat(name = "Tommy", species= "Cat",age = "17",favorite_color="black")
# tommy.MEOW("MEOW")""
K= Bird("none","Bird","none","none")
K.intro("Chicken")
Rick = Chicken("Rick","Bird", "16", "blue")
Rick.BAQ("BAQ")
Rick.Ability("Can't")
K.intro("Dove")
Bob = Dove("Bob","Bird","6","yellow")
Bob.HOO("HOO")
Bob.Ability("Can ")




