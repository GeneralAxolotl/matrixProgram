from cmath import *


def linear(a, b):
    solutions = list()
    if a == 0 and b == 0:
        solutions.append(True)

    if a == 0 and b != 0:
        solutions.append(False)

    if a != 0:
        solutions.append(-b / a)
    return solutions


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




def synthetic_division(a,b,c,d):
    
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
    print(quadratic(temp[0],temp[1],temp[2]))
    t=quadratic(temp[0],temp[1],temp[2])
    eigen=[e1]
    eigen.append(t[0])
    eigen.append(t[1])
    eigen.sort()
    print("Eigen Value",eigen)
synthetic_division(1,-18,99,-162)
