# #DogClasses
# class BestDog:
# #class variables
#     animal_kind = 'Canine'
#
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#         self.bark()
#
#     def bark(self):
#         print('Bork Bork')
#
# husky = BestDog("Husky","Husky")
# lacy = BestDog("Lacy","Jack Russell")
#
# husky.animal_kind = "Big Dog"
# BestDog.animal_kind = "Dolphin"
#
# print ("_____")
# print(f"Husky is a {husky.animal_kind}")
# print(f"Lacy is a {lacy.animal_kind}")
# print(f"Husky's breed is {husky.breed}")
# print(f"Lacy's breed is {lacy.breed}")

#MethodExamples
# class MethodExamples:
#
#     def __init__(self):
#         self._this_can_be_accessed = "I can be accessed easily"
#
#     def get_this_can_be(self):
#         return self._this_can_be_accessed
#     def set_this_can_be(self, value_to_be_set):
#         self._this_can_be_accessed = value_to_be_set
#
# x = MethodExamples
#
# print(x)

#INHERITANCE
class Animal:

    def __init__(self):
        self.alive = True
    def breathe(self):
        print("One breath in, one out")

class LandMammal(Animal):

    def __init__(self, legs):
        super().__init__()
        self.legs = legs
    def run(self):
        return "I can run!"

Mammoth = LandMammal()
Horse = Animal()

Horse.alive = False
print(Horse.alive)

print(Mammoth.run())


