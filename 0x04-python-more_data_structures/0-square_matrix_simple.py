#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    if not matrix:
      return None

    # using list comprehension to square each element in the matrix
    return [[element**2 for element in row] for row in matrix]
