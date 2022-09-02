def matrixReshape(mat,r,c):
    row = len(mat)
    col = len(mat[0])

    for i in range(row):
        for j in range(col):
            pass

mat = [[1,2],[3,4]]
r = 1
c = 4

print(matrixReshape(mat,r,c))