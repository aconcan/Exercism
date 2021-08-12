class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        # introduced nested for loop
        self.rows = [[int(num) for num in row.split(' ')] for row in self.matrix_string.split('\n')]
    
    # for loop removed
    def row(self, index):
        return list(self.rows[index-1])

    def column(self, index):
        return [row[index-1] for row in self.rows]

test = Matrix('1 2 3 4\n5 6 7 8\n9 8 7 6')
print(test.rows)
print(test.row(2))
print(test.column(2))
