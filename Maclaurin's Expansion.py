from sympy import *
from sympy import sympify
from prettytable import PrettyTable

print("Maclaurin's Expansion of f(x) in ascending powers of x")
x = symbols('x')
f = input("Enter f(x) = ")
a = int(0)
f = sympify(f)
n = int(input("Enter no. of terms:"))

print("___________________________________________________________________________________________________")
print("")
print("Solution:")
print("")
print("Maclaurin's Expansion of f(x) is")
print("f(x) = f(0) + {f'(0)}*x + {f''(0)/2!}*x**2 + {f'''(0)/3!}*x**3 + ... ")

der = f
der_coef = [f.subs([(x,a)])]
der_terms = [f]
for i in range(n):
    der = diff(der,x)
    der_terms.append(der)
    der_coef.append(der.subs([(x,a)]))

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

y = 0
for i in range(n+1):
    y = y + ((x - nsimplify(a))**i)*(1/factorial(i))*der_coef[i]
    #y = nsimplify(y)
print("")
print("∴ Maclaurin's series expansion of",f,"is")
print("f(x) =",y)