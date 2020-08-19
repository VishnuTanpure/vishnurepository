from sympy import *
from sympy import var
from sympy import sympify

a, b = symbols('a b')

r = nsimplify(input("enter power of (a+-b) :"))
   
if((r-abs(int(r)))!=0):
    n = int(input("as power is not a Natural number please enter the number of terms?"))
    n=n-1
else:
    n = r
bc=[1,r]
r1=r
for i in range(1,n):
    r2 = r1 * (r-i)/factorial(i+1)
    bc.append(r2)
    r1=r1*(r-i)
 
print("Binomial Coefficients are:")
print(bc)

bep=0
bem=0
for i in range(n+1):
    bep=bep+bc[i]*a**(r-i)*b**i
    bem=bem+bc[i]*a**(r-i)*(-b)**i 

print("----------------OUTPUT----------------")
print("Binomial Expansion of (a + b)**",r,"is")    
print("(a + b)**",r,"=",bep)
    
print()
    
print("Binomial Expansion of (a - b)**",r,"is")    
print("(a - b)**",r,"=",bem)