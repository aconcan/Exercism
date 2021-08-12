# refactored with list comprehension

def square_of_sum(num):
    return sum(range(0, num+1))**2

def sum_of_squares(num):
    return sum(i*i for i in range(0, num+1))

def difference_of_squares(num):
    return square_of_sum(num) - sum_of_squares(num)
