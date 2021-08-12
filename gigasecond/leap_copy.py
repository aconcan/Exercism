def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        
        return True
    
    return False

''' 
Better solutions:

https://exercism.io/tracks/python/exercises/leap/solutions/e39730d074687ad04690a352

https://exercism.io/tracks/python/exercises/leap/solutions/6b1e76b48df76d418d94bd3b

'''