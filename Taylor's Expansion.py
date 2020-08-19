from sympy import *
from sympy import sympify
from prettytable import PrettyTable

print("Taylor's Expansion of f(x) in ascending powers of (x-a)")
x = symbols('x')
mode = int(input("enter 1 for radian or 0 for degree: "))
f = input("Enter f(x) = ")
a = nsimplify(input("expansion about = "))
if(mode == 0):
    a = a*pi/180
f = sympify(f)
n = int(input("Enter no. of terms:"))

print("___________________________________________________________________________________________________")
print("")
print("Solution:")
print("")
# Taylor's expansion is y = f(x) + x f'(x) + (x^2/2)f''(x) +...
print("Taylor's Expansion of f(x) about x = a is")
print("f(x) = f(a) + {f'(a)}*(x-a) + {f''(a)/2!}*(x-a)**2 + {f'''(a)/3!}*(x-a)**3 + ... ")

der = f
der_coef = [f.subs([(x,a)])]
der_terms = [f]
for i in range(n):
    der = diff(der,x)
    der_terms.append(der)
    der_coef.append(der.subs([(x,a)]))
#print(der_terms)
#print(der_coef)

column_temp = ["f(x)","1st derivative of f(x)","2nd derivative of f(x)","3rd derivative of f(x)"]
column_0 = []
for i in range(len(der_coef)):
    if(i<=3):
        column_0.append(column_temp[i])
    else:
        column_0.append(str(i)+"th derivative of f(x)")
    
table = PrettyTable()
table.add_column("order",column_0)
table.add_column("derivative",der_terms)
table.add_column("evaluated at x = "+str(a),der_coef)
print(table)

print("Taylor's Expansion of f(x) about x =",nsimplify(a),"is")
print("f(x) = f(",a,") + {f'(",a,")}*(x-",a,") + {f''(",a,")/2!}*(x-",a,")**2 + {f'''(",a,")/3!}*(x-",a,")**3 + ... ",sep="")

y = 0
for i in range(n+1):
    y = y + ((x - nsimplify(a))**i)*(1/factorial(i))*der_coef[i]
    #y = nsimplify(y)
#print("Taylor's series expansion of",f,"about x =",a,"is")
#print("f(x) =",y)

print()
#print("Taylor's series expansion of f(x) about x =",a,"is")
print("∴ Taylor's series expansion of",f,"about x =",a,"is")
print("f(x) = ",end="")
print(nsimplify(der_coef[0]),sep="",end=" ")
if(nsimplify(der_coef[1])!=0):
    if(nsimplify(der_coef[1]) > 0):
        print("+ {",nsimplify(der_coef[1]/factorial(1)),"}*(",str(x - a),")",sep="",end=" ")
    else:
        print("- {",nsimplify(abs(der_coef[1])/factorial(1)),"}*(",str(x - a),")",sep="",end=" ")
for j in range(2,len(der_coef)):
    if(nsimplify(der_coef[j])!=0):
        if(der_coef[j] > 0):
            print("+ {",nsimplify(der_coef[j]/factorial(j)),"}*(", str(x - a),")**",j, sep="",end=" ")
        else:
            print("- {",nsimplify(abs(der_coef[j])/factorial(j)),"}*(", str(x - a),")**",j, sep="",end=" ")