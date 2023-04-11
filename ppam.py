# Reading input
n, h = map(int, input().split())
boards = [list(map(int, input().split())) for i in range(n)]

# Initializing variables
hole_boards = 0
x_coord = n

# Moving laser from left to right
for i in range(n):
    # Check if the board is made of steel
    if boards[i][2] == 3:
        x_coord = i
        break
    # Check if the height of the board is less than the laser height
    if boards[i][1] < h:
        continue
    # Check if the board is made of wood and its height is greater than the laser height
    if boards[i][2] == 1 and boards[i][1] > h:
        hole_boards += 1

# Outputting result
print(x_coord, hole_boards)
