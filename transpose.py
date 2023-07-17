def transpose(matrix,rows,cols):
    for i in range(rows):
        for j in range(i+1,cols):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix
matrix=[]
rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
for i in range(rows):
    matrix.append(list(map(int,input("Enter elements:").split())))
print(transpose(matrix,rows,cols))