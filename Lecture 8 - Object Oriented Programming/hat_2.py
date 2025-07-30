########## HAT 2 ##########
import random 

# Example 1
class Hat:
    
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

# hat = Hat()
Hat.sort("Harry")