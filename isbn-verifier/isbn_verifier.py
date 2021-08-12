# def is_valid(isbn):
#     # List conversion so X can be replaced
#     isbn = list(isbn.replace('-', ''))
    
#     if len(isbn) != 10:
#         return False

#     if isbn[-1] == 'X':
#         isbn[-1] = '10'
    
#     total = 0
#     for i, digit in enumerate(isbn[::-1]):
#         total += int(digit)*(i+1)

#     if total % 11 == 0:
#         return True

#     return False
        

# isbn = '3-598-21507-X'
# print(is_valid(isbn))

# Top starred solution—makes use of re module
import re

def check_isbn_formula(digits):
    numbers_to_mult = list(map(int, digits))
    return sum([factors[0] * factors[1] for factors in zip(numbers_to_mult, range(10,0,-1))]) % 11 == 0

def verify(isbn):
    stripped_isbn = isbn.replace("-", "")

    if not re.compile("[0-9]{9}([0-9]|X)$").match(stripped_isbn):
        return False
    else:
        digits = list(stripped_isbn)
        if digits[-1] == 'X':
            digits[len(digits)-1] = '10'
        return check_isbn_formula(digits)

 
print(verify('3-598-21507-X'))