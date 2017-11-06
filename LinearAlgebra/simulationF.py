#-*- coding: utf-8
from pprint import pprint


def create_list(t, power, value):
    # power equal to the bigest exponent number
    r = []
    for i in range(power + 1):
        r.append(pow(t, i))
    r.append(value)
    return r


def create_matrix(data):

    matrix = []
    for i in data:
        l = create_list(i[0], 5, i[1])
        matrix.append(l)

    return matrix

def count_matrix(matrix):
    dims = len(matrix)

    for i in range(dims):
        matrix[i] = standardize(i, matrix[i])
        for j in range(i + 1, dims):
            matrix[j] = subtraction(i, matrix[j], matrix[i])
    return matrix

def standardize(index, target):
    if target[index] != 0.0:
        target = [i/target[index] for i in target]
    return target
    

def subtraction(index, subed, sub):
    if subed[index] != 0.0:
        sub = [subed[index] * i for i in sub]
        subed = [subed[i] - sub[i] for i in range(len(subed))]
    return subed

def purified(matrix):
    dims = len(matrix)
    for i in range(dims - 1, 0, -1):
        l = matrix[i]
        if l[i] != 1.0:
            continue
        for j in range(0, i):
            matrix[j] = subtraction(i, matrix[j], l)

    return matrix

def simplified_to_standard(matrix):
    # target is to deal the n✖n matrix
    dim = len(matrix)
    for index in range(dim):
        change = 1
        exchange = index + change
        # find one the first 
        while matrix[index][index] == 0.0 and index < dim - 1:
            matrix[index], matrix[exchange] = matrix[exchange], matrix[index]
            change += 1
        if matrix[index][index] == 0.0:
            continue

        to_unit = matrix[index][index]    
        matrix[index] = [e/to_unit for e in matrix[index]]

        next_index = index + 1
        for ano in range(next_index, dim):
            factor = matrix[ano][index]
            subtracted = [e*factor for e in matrix[index]]
            matrix[ano] = subtract_values(matrix[ano], subtracted)
    return matrix

def subtract_values(subtraction_list, subtracted):
    for index in range(len(subtraction_list)):
        subtraction_list[index] = subtraction_list[index] - subtracted[index]
    return subtraction_list


if __name__ == "__main__":
    # # [{speed, resistance}...]
    # data = [(0, 0), (2, 2.9), (4, 14.8), (6, 39.6), (8, 74.3), (10, 119)]
    # # data = [(1, 6), (2, 15), (3, 28)]
    # matrix = count_matrix(create_matrix(data))
    # # matrix = purified(matrix)
    # pprint(matrix)

    matrix = [
        [1, 2, -1, 1, 0, 0],
        [-3, -5, 0, 0, 1, 0],
        [4, 6, -1, 0, 0, 1],
    ]

    r = simplified_to_standard(matrix)
    pprint(r)

