from sympy import *
from sympy import sympify
from prettytable import PrettyTable

print("Evaluation using Taylor's Expansion!!!")
check=1
while(check==1):
    try:
        f_eval = str(input("Evaluate = "))
        check=0
    except:
        print("Invalid input.")
        check=1
        
x = symbols('x')
check=1
while(check==1):
    try:
        mode = (input("enter 1 for radian or 0 for degree: "))
        check=0
        if(int(mode) != 0 and int(mode) != 1):
            print("Please Enter 1 or 0")
            check=1
    except:
        print("Invalid input.")
        check=1


check=1
while(check==1):
    try:
        f = input("Enter f(x) = ")
        f = sympify(f)
        check=0
    except Exception as e:
        print("Invalid Input",e)
        check=1
 
check_1=1
check_2=1
while(check_1==1 or check_2==1):
    try:
        a = nsimplify(input("Enter a = "))
        h = nsimplify(input("Enter h = "))
        check_1=0
        if(type(float(a))):
            check_2=0
        if(type(float(h))):
            check_2=0
    except Exception as e:
        print("Invalid Input",e)
        check_1=1        

if(int(mode) == 0):
    a = a*pi/180
    h = h*pi/180

check=1
while(check==1):
    try:    
        n = int(input("Enter no. of terms:"))
        check=0
        if(n<0):
            print("Please enter Positive Integer.")
            check=1
    except:
        print("Please enter Positive Integer.")
        check=1

print("___________________________________________________________________________________________________")
print("")
print("Solution:")
print("")
# Taylor's expansion is y = f(x) + x f'(x) + (x^2/2)f''(x) +...
print("Taylor's Expansion of f(x+h) in ascending powers of h is")
print("f(x+h) = f(x) + {f'(x)}*h + {f''(x)/2!}*h**2 + {f'''(x)/3!}*h**3 + ... -----(1)")
print("put x = a")
print("f(a+h) = f(a) + {f'(a)}*h + {f''(a)/2!}*h**2 + {f'''(a)/3!}*h**3 + ... -----(2)")

der = f
der_coef = [f.subs([(x,a)])]
der_terms = [f]
for i in range(n):
    der = diff(der,x)
    der_terms.append(der)
    der_coef.append(der.subs([(x,a)]))

y = 0
for i in range(n+1):
    y = y + ((h)**i)*(1/factorial(i))*der_coef[i]

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
table.add_column("evaluated at x = (a = "+str(a)+")",der_coef)
print(table)

print("Putting a =",a,"& h =",h,"in eq.(2), we get")
print("f(",a,"+",h,") = f(",a,") + {f'(",a,")}*(",h,") + {f''(",a,")/2!}*(",h,")**2 + {f'''(",a,")/3!}*(",a,")**3 + ... ",sep="")

print()
#print("∴ Taylor's series expansion of f(a+h) about (",a,") in ascending powers of (",h,") is")
print("∴",f_eval,"= ",end="")
print(nsimplify(der_coef[0]),sep="",end=" ")
if(nsimplify(der_coef[1])!=0):
    if(nsimplify(der_coef[1]) > 0):
        print("+ {",nsimplify(der_coef[1]/factorial(1)),"}*(",str(h),")",sep="",end=" ")
    else:
        print("- {",nsimplify(abs(der_coef[1])/factorial(1)),"}*(",str(h),")",sep="",end=" ")
for j in range(2,len(der_coef)):
    if(nsimplify(der_coef[j])!=0):
        if(der_coef[j] > 0):
            print("+ {",nsimplify(der_coef[j]/factorial(j)),"}*(", str(h),")**",j, sep="",end=" ")
        else:
            print("- {",nsimplify(abs(der_coef[j])/factorial(j)),"}*(", str(h),")**",j, sep="",end=" ")
            
print()
print("∴",f_eval,"=",float(y))