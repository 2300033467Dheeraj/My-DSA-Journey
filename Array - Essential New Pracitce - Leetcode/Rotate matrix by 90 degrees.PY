matrix =[
            [1, 2, 3],
            [4, 5, 6], 
            [7, 8, 9]
        ]
n = len(matrix)
m = len(matrix[0])

for i in range(n):
    for j in range(i,n):
        matrix[i][j] , matrix[j][i] = matrix[j][i],matrix[i][j]
print(matrix) 
#for transverse matrix
for i in range(n):
    matrix[i].reverse()
print(matrix)