import math


class ShapeException(Exception):
    pass


def shape(matrix):
    if isinstance(matrix[0], list):
        return (len(matrix), len(matrix[1]))
    elif isinstance(matrix[0], int):
        return (len(matrix), )


def vector_add(v1, v2):
    if shape(v1) != shape(v2):
        raise ShapeException
    return [x + y for x, y in zip(v1, v2)]


def vector_sub(v1, v2):
    if shape(v1) != shape(v2):
        raise ShapeException
    return [x - y for x, y in zip(v1, v2)]


def vector_sum(*args):
    vec_len = len(args[1])
    for vector in args:
        if len(vector) != vec_len:
            raise ShapeException
    return [sum(i) for i in zip(*args)]


def dot(v1, v2):
    if shape(v1) != shape(v2):
        raise ShapeException
    return sum([v1[i] * v2[i] for i in range(len(v1))])


def vector_multiply(vector, scalar):
    return [idx * scalar for idx in vector]


def vector_mean(*args):
    return [sum(vectors)/len(vectors) for vectors in zip(*args)]


def magnitude(vector):
    return math.sqrt(sum([vector[i]**2 for i in range(len(vector))]))


def matrix_row(matrix, row):
    return matrix[row]


def matrix_col(matrix, col):
    return [i[col] for i in matrix]


def matrix_scalar_multiply(matrix, scalar):
    pass


def matrix_vector_multiply(m1, v1):
    if len(v1) != len(m1[0]):
        raise ShapeException


def matrix_matrix_multiply(m1, m2):
    if len(m1[0]) != len(m2):
        raise ShapeException
