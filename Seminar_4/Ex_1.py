# Напишите функцию для транспонирования матрицы 

def mat_transpose(matrix):
    a = len(matrix)
    b = len(matrix[0])
    result = [[0 for j in range(a)] for i in range(b)]
    for i in range(a):
        for j in range(b):
            result[j][i] = matrix[i][j]
    return result
matrix = [[9,8,7],[6,5,4]]
print(mat_transpose(matrix))
