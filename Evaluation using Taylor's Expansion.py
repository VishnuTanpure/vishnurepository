from sympy import *
from sympy import sympify

x, a, h = symbols('x a h')
mode = int(input("enter 1 for radian or 0 for degree."))
f = input("Enter f(x) =")

a1 = nsimplify(input("Enter value of a: "))
h1 = nsimplify(input("Enter value of h: "))

if(mode == 0):
    a1 = a1*pi/180
    h1 = h1*pi/180
f = sympify(f)
n = int(input("Enter no. of terms:"))

# Taylor's expansion is y = f(x) + x f'(x) + (x^2/2)f''(x) +...
der = f
der_coef = [f.subs([(x,a)])]
for i in range(n):
    der = diff(der,x)
    der_coef.append(der.subs([(x,a)]))

#print(der_coef)
y = 0
for i in range(n+1):
    y = y + ((h)**i)*(1/factorial(i))*der_coef[i]
 
print("Taylor's series expansion of",f,"about x =",a,"is")
print("f(x) =",y)

print(float(y.subs([(a,a1),(h,h1)])))