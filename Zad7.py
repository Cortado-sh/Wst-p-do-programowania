def create_matrix_with_ones_on_edges(size):
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        matrix[0][i] = 1
        matrix[size - 1][i] = 1
        matrix[i][0] = 1
        matrix[i][size - 1] = 1
    return matrix

def toggle_matrix(matrix):
    return [[1 if cell == 0 else 0 for cell in row] for row in matrix]

matrix = create_matrix_with_ones_on_edges(5)
for row in matrix:
    print(row)

toggled_matrix = toggle_matrix(matrix)
for row in toggled_matrix:
    print(row)
