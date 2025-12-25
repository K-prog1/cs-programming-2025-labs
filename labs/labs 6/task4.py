def add_matrices(m1, m2, n):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result

def read_matrix(n):
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            raise ValueError("Неверное количество элементов в строке")
        matrix.append(row)
    return matrix

try:
    n = int(input().strip())
    
    if n <= 2:
        print("Ошибка: размер матрицы должен быть больше 2")
        exit()

    a = read_matrix(n)
    b = read_matrix(n)

    result = add_matrices(a, b, n)

    for row in result:
        print(' '.join(map(str, row)))

except Exception as e:
    print("Ошибка: некорректный ввод")