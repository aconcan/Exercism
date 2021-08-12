def saddle_points(matrix):
    # check all rows same length
    if len(set(map(len, matrix))) > 1:
        raise ValueError('.+')

    # get transpose
    matrixT = list(zip(*matrix))
    points = []

    # check row max and column mins for all numbers in matrix
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if num == max(row) and num == min(matrixT[j]):
                point_dict = {
                    'row': i+1,
                    'column': j+1
                }
                points.append(point_dict)

    return points
