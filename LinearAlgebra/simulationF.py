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
    return matrix


if __name__ == "__main__":
    # data = [
    #     # {speed, resistance}
    #     (0, 0), 
    #     (2, 2.9), 
    #     (4, 14.8), 
    #     (6, 39.6), 
    #     (8, 74.3), 
    #     (10, 119)
    # ]
    data = [(1, 6), (2, 15), (3, 28)]
    matrix = create_matrix(data)
    matrix = count_matrix(matrix)
    matrix = purified(matrix)
    pprint(matrix)

