# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from LinearAlgebra import *
order=[int(i) for i in input("Enter Order of a Matrix in m*n format:").split("*")]
m=order[0]
n=order[1]
M=[[sp.Rational(0) for j in range(n)]for i in range(m)]
M=reshape(M,(m,n))
for i in range(m):
    for j in range(n):
        print("Enter",i,"th row",j,"th column entry:",end="")
        M[i][j]=sp.Rational(input())
print(M)
M=echelonform(M,m,n)
print(M)
EVEV=EigValEigVec(M,m)
print(EVEV)
