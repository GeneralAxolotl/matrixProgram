from cmath import *
#Solves Linear Equation
def linear(a, b):
    solutions = list()
    if a == 0 and b == 0:
        solutions.append(True)

    if a == 0 and b != 0:
        solutions.append(False)

    if a != 0:
        solutions.append(-b / a)
    return solutions

#Solves Quadratic Equation
def quadratic(a, b, c):
    solutions = list()
    if a != 0:
        D = b ** 2 - 4 * a * c
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        solutions.append(x1.real)
        solutions.append(x2.real)
    else:
        solutions.append(linear(b, c))
    return solutions


#Getting Matrix A
A=[]
s1,s2,s3,l,a,b,c,d=1,1,1,1,1,1,1,1
sign=-1
quadEquation=[]
for i in range(3):
    matrixItem=[]
    for j in range(3):
        matrixItem.append(int(input("Enter Element:")))
    A.append(matrixItem)
print('\n'.join([''.join(['{:4}'.format(item)for item in row])for row in A]))

#determinant 0f matrix
def deter(matA):
    m1=((matA[1][1]*matA[2][2])-(matA[1][2]*matA[2][1]))
    m2=((matA[1][0]*matA[2][2])-(matA[1][2]*matA[2][0]))
    m3=((matA[1][0]*matA[2][1])-(matA[1][1]*matA[2][0]))
    s3=(matA[0][0]*(m1))-(matA[0][1]*(m2))+(matA[0][2]*(m3))
    return s3

#sum of co-factor elements of main diagonal elements
def sumofMainDia(matA):
    s=((matA[0][0]*matA[1][1])-(matA[0][1]*matA[1][0]))+((matA[0][0]*matA[2][2])-(matA[0][2]*matA[2][0]))+((matA[1][1]*matA[2][2])-(matA[1][2]*matA[2][1]))
    return s

#Characteristic Equation
def charEquation(matA):
    global l,s1,s2,s3,a,b,c,d
    s1=matA[0][0]+matA[1][1]+matA[2][2]
    print("s1",s1)
    s2=sumofMainDia(matA)
    print("s2",s2)
    s3=deter(matA)
    print("S3:",s3)
    b,d=s1*sign,s3*sign
    c=s2
charEquation(A)

#Eigen Value

#To Find Eigen Vector
def synthetic_division(a,b,c,d):
    e=[a,b,c,d]                               #Solves The polynomial equation
    print(e)
    x=-4
    temp=[1,1,1,1]
    while(temp[3]!=0):
        temp=[1,1,1,1]
        temp[0]=e[0]+0
        temp[1]=e[1]+(x*temp[0])
        temp[2]=e[2]+(x*temp[1])
        temp[3]=e[3]+(x*temp[2])
        #print(x,temp)
        e1=x
        x=x+1
        if(x>5):
            break
    print("Reduced Eqn of",e,"is:",temp)
    quadEquation=list(temp)
    return quadEquation

#Solves The polynomial equation
def find_eigenValue(a,b,c,d):
    #Synthetic Division
    e=[a,b,c,d]                              
    print(e)
    x=-4
    temp=[1,1,1,1]
    while(temp[3]!=0):
        temp=[1,1,1,1]
        temp[0]=e[0]+0
        temp[1]=e[1]+(x*temp[0])
        temp[2]=e[2]+(x*temp[1])
        temp[3]=e[3]+(x*temp[2])
        #print(x,temp)
        e1=x
        x=x+1
        if(x>5):
            break
    print("Reduced Eqn of",e,"is:",temp)
    quadEquation=list(temp)

    #Solves the reduced quadratic equation

    print(quadratic(quadEquation[0],quadEquation[1],quadEquation[2]))
    t=quadratic(quadEquation[0],quadEquation[1],quadEquation[2])
    eigen=[e1]
    eigen.append(t[0])
    eigen.append(t[1])
    eigen.sort()
    print("Eigen Value",eigen)
    return eigen




find_eigenValue(a,b,c,d)




#To find eigen vector
#def eigenVector(e1,e2,e3):

v1=[]
v2=[]
v3=[]
#Diagonalisation of matA
def diagonalise():
    matM=[]
    matD=[]
    matN=[]
    matNtrans=[]
    for i in range(3):
        matM.append(v1)
        matM.append(v2)
        matM.append(v3)
    print(matM)
    l=sqrt(matM[0][0]**2+matM[1][0]**2+matM[2][0]**2)
    m=sqrt(matM[0][1]**2+matM[1][1]**2+matM[2][1]**2)
    n=sqrt(matM[0][2]**2+matM[1][2]**2+matM[2][2]**2)
    print(l,m,n)
    for i in range(3):
            matN[0][i]=matM[0][i]/l
    for i in range(3):
            matN[1][i]=matM[1][i]/m
    for i in range(3):
            matN[2][i]=matM[2][i]/n
    print(matN)



def transpose(matA):
    temp=[]
    for i in range(3):
        temp[2][i]=matA[0][i]
    for i in range(3):
        temp[1][i]=matA[1][i]
    for i in range(3):
        temp[0][i]=matA[2][i]
              




















































