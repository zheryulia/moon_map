matrix = []

with open("matrix.txt") as file:
    for line in file:
        matrix.append([int(num) for num in line.strip()])


def calculate(moon_map):
    k = 0
    row = len(moon_map)
    column = len(moon_map[0])
    for i in range(row):
        for j in range(column):
            element = moon_map[i][j]
            element_right = 0
            element_down = 0
            if j < column - 1:
                element_right = moon_map[i][j + 1]
            if i < row - 1:
                element_down = moon_map[i + 1][j]
            if element == 1 and element_right == 0 and element_down == 0:
                k += 1

    return k


count = calculate(matrix)
print(count)