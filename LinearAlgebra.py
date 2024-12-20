# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:56:19 2020

@author: Hp
"""

from prettytable import PrettyTable
from tabulate import tabulate
from fractions import Fraction
import numpy as np
import sympy as sp
from sympy import *
import matplotlib.pyplot as plt
from numpy import *
from numpy.polynomial import Polynomial as P

x=sp.symbols('x')

def MatMul(A,B):
    
    m_A=len(A)
    n_A=len(A[0])
    m_B=len(B)
    n_B=len(B[0])
    m=m_A
    n=n_B
    AB=[[complex(0) for j in range(n_B)] for i in range(m_A)]
    AB=reshape(AB,(m,n))

    if(n_A==m_B):
        for i in range(m_A):
            for j in range(n_B):
                k=0
                t=0
                for k in range(m_B):
                    t=t+A[i][k]*B[k][j]
                AB[i][j]=t
            
    return(AB)

def PolyDiv(u,v):
    def Divide(u,v):
        r=[]
        q=u[0]/v[0]
        q=sp.Rational(q)
        for j in range(len(v)-1):
            r.append(u[j+1]-((u[0]/v[0])*v[j+1]))
        for j in range(len(v)-1,len(u)-1):
            r.append(u[j+1])
        
        return(q,r)    
     
    quo=[]
    while(len(u)>=len(v)):   
        q,u=Divide(u,v)
        quo.append(q)
    
    return(quo,u)

def pivot(M,m,n,k,l):

    pr=k
    if(M[pr][l]==0):
        while(pr<m and M[pr][l]==0):
            pr=pr+1
        if(pr<m):
            for j in range(n):
                t=M[k][j]
                M[k][j]=M[pr][j]
                M[pr][j]=t
  
    return(M)

def echelonform(M,m,n,k=0,l=0):
    pc=[]
    while(l<n and k<m):
        check=1
        h=m-k
        while(check==1 and l<n):
            t=[0 for i in range(h)]
            tc=[]
            for i in range(h):
                tc.append(M[i+k][l])
            if(t==tc and l<n):
                l=l+1
                check=1
            else:
                check=0
        if(k<m and l<n):
            if(M[k][l]==0):
                M=pivot(M,m,n,k,l)
        for i in range(k,m):
            if(i!=k and l<n):
                if(M[i][l]!=0):
                    s=M[i][l]
                    r=M[k][l]
                    for j in range(l,n):
                        M[i][j]=sp.expand((r*M[i][j])-(s*M[k][j]))
        l=l+1
        k=k+1 
    return(M)


def echelon(M,m,n,k=0,l=0):

    pc=[]
    sign=0 #calculates how many times rows are interchanged
    factor=1
    while(l<n and k<m):
        check=1
        h=m-k
        while(check==1 and l<n):
            t=[0 for i in range(h)]
            tc=[]
            for i in range(h):
                tc.append(M[i+k][l])
            
            if(t==tc and l<n):
                l=l+1
                check=1
            else:
                check=0
        
        if(k<m and l<n):
            
            if(M[k][l]==0):
                sign=sign+1
                M=pivot(M,m,n,k,l)
            
            pc.append(l)    
              
        for i in range(k,m):
            if(i!=k and l<n):
                if(M[i][l]!=0):
                    s=M[i][l]
                    r=M[k][l]
                    factor=factor*r
                    for j in range(l,n):
                        M[i][j]=sp.expand((r*M[i][j])-(s*M[k][j]))
                        #M[i][j]=sp.expand(M[i][j]-(s/r)*M[k][j])
                                     
        l=l+1
        k=k+1 
    #print("echelon")           
    #print(M)
    return(M,pc,sign,factor)

def echelon1(M,m,n,k,l):

    pc=[]
    sign=0 #calculates how many times rows are interchanged
    factor=1
    while(l<n and k<m):
        check=1
        h=m-k
        while(check==1 and l<n):
            t=[0 for i in range(h)]
            tc=[]
            for i in range(h):
                tc.append(M[i+k][l])
            
            if(t==tc and l<n):
                l=l+1
                check=1
            else:
                check=0
        
        if(k<m and l<n):
            
            if(M[k][l]==0):
                sign=sign+1
                M=pivot(M,m,n,k,l)
            
            pc.append(l)    
              
        for i in range(k,m):
            if(i!=k and l<n):
                if(M[i][l]!=0):
                    s=M[i][l]
                    r=M[k][l]
                    factor=factor*r
                    for j in range(l,n):
                        #M[i][j]=sp.expand((r*M[i][j])-(s*M[k][j]))
                        M[i][j]=sp.expand(M[i][j]-(s/r)*M[k][j])
                                     
        l=l+1
        k=k+1 
    #print("echelon")           
    #print(M)
    return(M,pc,sign,factor)

def rank(M,m,n): # to find ranks of given matrices
    r=0 # r = number of non zero rows
    null_row=[0.0 for j in range (n)]
    for i in range (m):  # r counts number of non zero rows
        row=[]
        for j in range (n):
            row.append(M[i][j])

        if(row!=null_row):
            r=r+1
                
    return(r)

def EigValEigVec(M,m):
    
    n=m
    
    A=[[sp.Rational(0) for j in range(n)] for i in range(m)]
    B=[[sp.Rational(0) for j in range(n)] for i in range(m)]
   
    A=reshape(A,(m,n))
    B=reshape(B,(m,n))
       
    for i in range(m):
        for j in range(n):
            A[i][j]=M[i][j]
            B[i][j]=M[i][j]
            
    for i in range(n):
        M[i][i]=M[i][i]-x
    
    mat,pc,sign,factor=echelon(M,m,n,0,0)
    determinant=1
    for i in range(m):  # Product of diagonal entries
        determinant=sp.expand(determinant*mat[i][i])
        
    sign=(-1)**sign     # no. of times rows are interchanged
    determinant=determinant*sign
    determinant=Poly(determinant,x) 
    det_coeff=determinant.all_coeffs()
    factor=Poly(factor,x)
    fact_coeff=factor.all_coeffs()
    q,r=PolyDiv(det_coeff,fact_coeff)
    
    char=0
    for i in range(len(q)):
        char=char+q[i]*x**(len(q)-1-i)    
    
    #sp.pprint(char)
    CharPoly=np.poly1d(q)
    char_root=CharPoly.r
    
    for i in range(len(char_root)):
        try:
            char_root[i]=sp.Rational(char_root[i]).limit_denominator()
        except:
            char_root[i]=char_root[i]
      
        try:
            char_root[i]=complex(char_root[i])
            RE=0
            IE=0
            RE=real(char_root[i])
            IE=imag(char_root[i])
            
            if(abs(RE-int(RE))<0.001 or abs(RE-int(RE))>0.99):
                RE=round(RE)
            else:
                RE=RE
        
            if(abs(IE-int(IE))<0.001 or abs(IE-int(IE))>0.99):
                IE=round(IE)
            else:
                IE=IE
          
            char_root[i]=complex(RE,IE)
            
        except:
            z=0
    EigVal=[]
    for i in (char_root):
        if(i not in (EigVal)):
            EigVal.append(i)
    n=n+1          
    M=[[sp.Rational(0) for i in range(n)] for j in range(m)]
    M=reshape(M,(m,n))
    EV_No=0
    EV=[]
    V=[[sp.Rational(0) for i in range(m)]for j in range(m)]
    V=reshape(V,(m,m))
    EVEV={}
    n_EigVec=0  #count no. of Eigen Vectors
    for each in (EigVal):   # Finding Eigen Vectors
        for i in range(m):
            for j in range(n):
                if(i==j):
                    try:
                        M[i][j]=sp.Rational(A[i][j]-each)
                    except:
                        M[i][j]=(A[i][j]-each)
                elif(j==n-1):
                    M[i][j]=0
                else:
                    M[i][j]=A[i][j]
        
        M,pc,sign,factor=echelon1(M,m,n,0,0)
        
        for i in range(m):
            for j in range(n):
                M[i][j]=round((M[i][j]),6)
       
        M,pc,sign,factor=echelon1(M,m,n,0,0)
        rM=rank(M,m,n)
        
        Alfabets=['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16','X17','X18','X19','X20']
        unknowns=[]
       
        X=[Fraction(1) for i in range(n-1)]
        for i in range(n-1):  # to get required number of unknowns from Alfabets
            unknowns.append(Alfabets[i])
      
        r=rM
        k=n-1
        npc=[i for i in range(k) if i not in pc]        # ncp-non pivot columns
        n_EigVec=n_EigVec+len(npc)
        tEV=[]
        for b in range(len(npc)): #b-to find basis of solution space
            X=[sp.Rational(1) for i in range(n-1)]
            #X=[Fraction(1) for i in range(n-1)]     # initiate all variables with value 1
            for i in range(len(npc)):
                if(i==b):
                    #X[npc[i]]=float(1)
                    X[npc[i]]=sp.Rational(1)
                else:
                    X[npc[i]]=0
                          
            z=len(pc)
            a=0
            for i in range(k):  # calculate values of non-free variables using Back substitution metod
                check=1
                j=0
                flag=0
                for g in range(len(npc)):   
                    if(k-1-i==npc[g]):
                        flag=flag+1
                        
                if(flag==0):
                    while(check==1 and j<k):
                        if(M[r-1-a][k-1-j]!=0):
                            check=0
                            v=M[r-1-a][k]
                            
                            for l in range(k):
                                v=v-M[r-1-a][l]*X[l]
                        
                        else:
                            check=1
                            j=j+1
                    try:
                        X[k-1-i]=sp.Rational((v+M[r-1-a][k-1-i])/M[r-1-a][k-1-i]).limit_denominator()
                    except:
                        X[k-1-i]=expand(((v+M[r-1-a][k-1-i])/M[r-1-a][k-1-i]))  
                        X[k-1-i]=complex(X[k-1-i])
                    a=a+1
            
            EV.append(X)
            tEV.append(X)
            X=reshape(X,(m,1))
            AX=MatMul(A,X)
           
            try:
                λX=[[sp.Rational(0) for j in range(1)] for i in range(m)]
            except:
                λX=[[complex(0) for j in range(1)] for i in range(m)]
            λX=reshape(λX,(m,1))
            
            for i in range(m):
                λX[i][0]=complex(each*X[i][0])
            
            for i in range(m):
                EV[EV_No][i]=X[i][0]
       
            EV_No=EV_No+1  
        EVEV[each]=tEV                 
     
    return(EVEV)