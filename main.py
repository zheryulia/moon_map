matrix = []

with open("matrix.txt") as file:
    for line in file:
        matrix.append([int(num) for num in line.strip()])


def calculate(moon_map: list) -> list:
    """Функция, подсчитывающая количество кратеров"""
    k = 0  # cчетчик кратеров
    row = len(moon_map)
    column = len(moon_map[0])
    for i in range(row):
        for j in range(column):
            element = moon_map[i][j]
            element_right = 0  # считаем, что справа нет других элементов, пока не доказано обратное
            element_down = 0  # считаем, что снизу нет других элементов, пока не доказано обратное
            if j < column - 1: # -1, чтобы не выйти за пределы массива, потому что сравниваем со следующим
                element_right = moon_map[i][j + 1]
            if i < row - 1:
                element_down = moon_map[i + 1][j]
            if element == 1 and element_right == 0 and element_down == 0:
                k += 1

    return k


count = calculate(matrix)
print(count)
