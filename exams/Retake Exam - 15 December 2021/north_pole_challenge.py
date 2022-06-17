def validate_cell(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1

def set_cell(rows, columns, my_pos_row, my_pos_col):
    if my_pos_row < 0:
        return rows - 1, my_pos_col
    elif my_pos_col < 0:
        return my_pos_row, columns - 1
    elif my_pos_row > rows - 1:
        return 0, my_pos_col
    elif my_pos_col > columns - 1:
        return my_pos_row, 0
    else:
        return my_pos_row, my_pos_col

def check_for_gift(matrix, my_pos_row, my_pos_col, gifts):
    if matrix[my_pos_row][my_pos_col] == "D":
        gifts['decorations'] += 1
    elif matrix[my_pos_row][my_pos_col] == "G":
        gifts['gifts'] += 1
    elif matrix[my_pos_row][my_pos_col] == "C":
        gifts['cookies'] += 1
    return gifts

rows, columns = [int(x) for x in input().split(", ")]
matrix = []
# current_position = next((x, y) for x in range(rows) for y in range(columns) if rows[x] and columns[y] == 'Y')
my_pos_row = 0
my_pos_col = 0
total_subjects = 0
walk_end = False

gifts = {'decorations': 0,
         'gifts': 0,
         'cookies': 0
         }
for row in range(rows):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(columns):
        if row_elements[col] == "Y":
            my_pos_row = row
            my_pos_col = col
        if row_elements[col] != '.' and row_elements[col] != 'Y':
            total_subjects += 1

matrix[my_pos_row][my_pos_col] = 'x'

while True:
    input_command = input()
    if input_command == "End":
        matrix[my_pos_row][my_pos_col] = "Y"
        break

    direction = input_command.split("-")[0]
    steps = int(input_command.split('-')[1])

    for step in range(steps):
        my_pos_row, my_pos_col = validate_cell(direction, my_pos_row, my_pos_col)

        if set_cell:
            my_pos_row, my_pos_col = set_cell(rows, columns, my_pos_row, my_pos_col)
            check_for_gift(matrix, my_pos_row, my_pos_col, gifts)
            matrix[my_pos_row][my_pos_col] = 'x'
            if sum(gifts.values()) == total_subjects:
                matrix[my_pos_row][my_pos_col] = 'Y'
                walk_end = True
                break

    if walk_end:
        break

if sum(gifts.values()) == total_subjects:
    print("Merry Christmas!")
print(f"You've collected:")
print(f"- {gifts.get('decorations')} Christmas decorations")
print(f"- {gifts.get('gifts')} Gifts")
print(f"- {gifts.get('cookies')} Cookies")

for row in matrix:
    print(*row, sep=" ")
