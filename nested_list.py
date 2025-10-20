matrix = [
    [1, 2, 3],   # row 0
    [4, 5, 6],   # row 1
    [7, 8, 9]    # row 2
]

print(matrix[0])      # [1, 2, 3]  (first row)
print(matrix[1][2])   # 6          (row 1, col 2)

flat = [val for row in matrix for val in row]
print(flat)  # [1,2,3,4,5,6,7,8,9]

transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)  # [[1,4,7],[2,5,8],[3,6,9]]

matrix[0][1] = 99
print(matrix)
# [[1, 99, 3], [4, 5, 6], [7, 8, 9]]

# - Nested lists = lists inside lists (great for 2D data).
# - Access with double indexing (matrix[row][col]).
# - Use nested loops or nested comprehensions for transformations.
# - For heavy numerical work, NumPy arrays are more efficient—but nested lists are the conceptual foundation.
