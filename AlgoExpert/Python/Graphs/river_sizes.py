def riverSizes(matrix):

    res = []

    if not matrix or not len(matrix) or not len(matrix[0]):
        return res

    height = len(matrix)
    width = len(matrix[0])

    for x in range(height):
        for y in range(width):
            if matrix[x][y] == 1:
                res.append(dfs(x, y, width, height, matrix, 1))


    return res

def dfs(x, y, width, height, matrix, counter):
    if x < 0 or y < 0 or x >= height or y >= width or matrix[x][y] == 0:
        return 0

    matrix[x][y] = 0

    right = dfs(x + 1, y, width, height, matrix, counter + 1)
    left = dfs(x - 1, y, width, height, matrix, counter + 1)
    up = dfs(x, y + 1, width, height, matrix, counter + 1)
    down = dfs(x, y - 1, width, height, matrix, counter + 1)

    return right + left + up + down + 1
