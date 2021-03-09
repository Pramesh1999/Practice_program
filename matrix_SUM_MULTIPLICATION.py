row = int(input())
col = int(input())
mat1 = []
for i in range(row):
    mat = []
    for x in range(col):
        a = int(input())
        mat.append(a)
    mat1.append(mat)
print("print first array element")
print(mat1)

row1 = int(input())
col1 = int(input())
mat2 = []
for i in range(row1):
    mat = []
    for  x in range(col1):
        a = int(input())
        mat.append(a)
    mat2.append(mat)
print("print second array element")
print(mat2)
print("print first1 array in matrix form ")
for i in mat1:
    for j in i:
        print (j, end= "  ")
    print() 
print("second array in matrix from")
for i in mat2:
    for j in i:
        print (j, end= "  ")
    print() 
sum1 = []
for i in range(row1):
    mat = []
    for j in range(col1):
        s = mat1[i][j]+mat2[i][j]
        mat.append(s)
    sum1.append(mat)
print("print matrix sum")
for i in sum1:
    for j in i:
        print (j, end= "  ")
    print() 
if(col != row1):
    print("we can not multily matrix enter matrix is not follow matrix multiplication rule")
mul =[]
for i in range(row1):
    mat = []
    for j in range(col):
        sum1 = 0
        for k in range(col):
            s = mat1[i][k] * mat2[k][j]
            sum1 = sum1+s
        mat.append(sum1)
    mul.append(mat)
print("both matrix multiplication")
for i in mul:
    for j in i:
        print(j, end="  ")
    print()
            
        
