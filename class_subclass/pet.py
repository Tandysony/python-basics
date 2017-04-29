
# base class
class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

polly = Pet("Polly", "Parrot")
print(polly) 

pet_name = polly.getName()
print(pet_name)


# sub-calss
class Dog(Pet):
    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats

rommy = Dog("Rommy", True)
print(rommy.getSpecies())
print(rommy.chasesCats())
print "Does %s , the %s, chase cats? %s" % (rommy.getName(), rommy.getSpecies(), rommy.chasesCats())


## SUMMARY
# 1. Do not forget constructor "__init__"
# 2. The "__str__" is a special built-in method can be overrridden. 
# 3. When calling a method, do not foget "()" at the end