#python program to implement transpose of a matrix.A
m = int(input('number of rows, m = '))
n = int(input('number of columns, n = '))
matrix = [[0 for j in range(n)] for i in range(m)]

for i in range(m):
  for j in range(n):
    print('entry in row: ', i+1, ' column: ', j+1)
    matrix[i][j] = int(input())

print("Matrix entered is:")
for i in range (m):
    for j in range (n):
        print(matrix[i][j], end=' ')
    print("")


print("Transpose of the Matrix is:")
for i in range(n):
    for j in range(m):
        print(matrix[j][i], end=' ')
    print("")
