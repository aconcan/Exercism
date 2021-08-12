def is_armstrong_number(number):
    if type(number) is not int:
        raise Exception('Method accepts arguments of type int only')
    
    exponent = len(str(number))
    return sum([int(num)**exponent for num in list(str(number))]) == number

