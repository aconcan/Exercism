
class SpaceAge():
    def __init__(self, seconds):
        
        self.seconds = seconds
        self.earth_seconds = 31557600

        self.planets = {
            'earth': 1.0,
            'mercury': 0.2408467, 
            'venus': 0.61519726,
            'mars': 1.8808158,
            'jupiter': 11.862615,
            'saturn': 29.447498,
            'uranus': 84.016846,
            'neptune': 164.79132,
        }

        for planet in self.planets:
            setattr(self, 'on_'+planet, self._planet_years(self.planets[planet]))

    def _planet_years(self, ratio):
        return lambda ratio = ratio : round(self.seconds/(self.earth_seconds*ratio), 2)

# _planet_years calculation method runs on creation of the class instance and is only callable then
test = SpaceAge(1000000000).on_earth() 
print(test)

# Storing a class instance and then attempting to call on_'planet' is not possible—object not callable
# For example:
test1 = SpaceAge(1000000000)
print(test.on_earth())