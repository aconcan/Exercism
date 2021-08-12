import random
from string import ascii_uppercase, digits

class Robot:

    # Making name private; internal use only
    def __init__(self):
        self._name = self.__generate_name()

    # Declaring name generation privately 
    def __generate_name(self):
        return random.choice(ascii_uppercase) + random.choice(ascii_uppercase) + random.choice(digits) + random.choice(digits) + random.choice(digits)

    # Getter for private name variable
    @property
    def name(self):
        return self._name

    # Preferable to dict solution—requires less memory
    def reset(self):
        previous_name = self._name
        self._name = self.__generate_name()
        
        if previous_name == self._name:
            self.reset()
