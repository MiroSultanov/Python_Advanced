# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its elements. 
# There will be no case with two or more 3x3 squares with equal maximal sum.

rows, columns = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

best_sum = float("-inf")
start_row = 0
start_col = 0

for row in range(rows - 2):
    for col in range(columns - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] \
                      + matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] \
                      + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

        if current_sum > best_sum:
            best_sum = current_sum
            start_row = row
            start_col = col

print(f"Sum = {best_sum}")
print(f"{matrix[start_row][start_col]} {matrix[start_row][start_col + 1]} {matrix[start_row][start_col + 2]}")
print(f"{matrix[start_row + 1][start_col]} {matrix[start_row + 1][start_col + 1]} {matrix[start_row + 1][start_col + 2]}")
print(f"{matrix[start_row + 2][start_col]} {matrix[start_row + 2][start_col + 1]} {matrix[start_row + 2][start_col + 2]}")

