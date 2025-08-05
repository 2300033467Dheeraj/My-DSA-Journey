matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]
        ]
n = len(matrix)
m = len(matrix[0]) if n > 0 else 0
rowlist=[]
collist=[]
for i in range(n):
  for j in range(m):
      if matrix[i][j]==0:
          rowlist.append(i)
          collist.append(j)
  for i in rowlist:
    for j in range(m):
          matrix[i][j]=0
    for j in collist:
      for i in range(n):
          matrix[i][j]=0
print(matrix)
