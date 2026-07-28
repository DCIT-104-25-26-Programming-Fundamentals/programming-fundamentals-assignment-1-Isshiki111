# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)

    return matrix


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for i in range(cols):
        new_row = []

        for j in range(rows):
            new_row.append(matrix[j][i])

        result.append(new_row)

    return result


def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])

        result.append(row)

    return result


def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])

    result = []

    for i in range(rows1):
        row = []

        for j in range(cols2):
            total = 0

            for k in range(cols1):
                total = total + matrix1[i][k] * matrix2[k][j]

            row.append(total)

        result.append(row)

    return result


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()


def main():

    # Part A - Transpose
    print("PART A - TRANSPOSE MATRIX")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    print("\nTransposed Matrix:")
    transpose = transpose_matrix(matrix)
    print_matrix(transpose)

    # Part B - Addition
    print("\nPART B - ADD TWO MATRICES")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter Matrix A")
    matrix1 = read_matrix(rows, cols)

    print("Enter Matrix B")
    matrix2 = read_matrix(rows, cols)

    print("\nResult:")
    result = add_matrices(matrix1, matrix2)
    print_matrix(result)

    # Part C - Multiplication
    print("\nPART C - MULTIPLY TWO MATRICES")

    rows1 = int(input("Rows of Matrix A: "))
    cols1 = int(input("Columns of Matrix A: "))

    print("Enter Matrix A")
    matrix1 = read_matrix(rows1, cols1)

    rows2 = int(input("Rows of Matrix B: "))
    cols2 = int(input("Columns of Matrix B: "))

    if cols1 != rows2:
        print("Error: Matrices cannot be multiplied.")
        return

    print("Enter Matrix B")
    matrix2 = read_matrix(rows2, cols2)

    print("\nProduct Matrix:")
    result = multiply_matrices(matrix1, matrix2)
    print_matrix(result)


main()