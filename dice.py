##My effort to code a die object
import random as rnd
from datetime import datetime as dt
#don't need this now; from older code; may use
#Do I want Die objects to know WHEN they make a roll?

##Now I'll try to create a die object that I can use
class Die():
    def __init__(self, sides):
        self.sides = sides
        # print (rnd.randint(1, int(self.sides)))

    def roll(self):
        result = (rnd.randint(1, int(self.sides)))
        return result
