#Problema 01
a = int(input())
b = int(input())
c = ((a != b ) or (a >= b))and (a%b == 1)
d = c*1
print(d)
#Problema 02
a = int(input())
b = int(input())
c = not( a== b or a <= b) and ((a%b) != 2)
d = c*1
print(d)
#Problema 03
a = int(input())
b = int(input())
c = a != (b**2) and (b/a) == 1
d = c*1
print(d)
#Problema 04
a = float(input())
b = int(input())
c = (b == int(a)) or a*b >10
d = c*1
print(d)
#Problema 05
a = int(input())
b = int(input())
c = not(((a**2) + (b**2))**0.5 == (2*a - b))
d = c*1
print(d)
#Problema 06
a = float(input())
b = float(input())
def trunc(a,b):
    c = a*(10**b)
    return (int(c)/100)
c = trunc(a,2) == b
d = c*1
print(d)
#Problema 07
a = int(input())
b = int(input())
def bin3(x):
    binario3 = ""
    for i in range(len(str(bin(x)))-1, len(str(bin(x)))-2, -1):
        binario3 = str(bin(x)[i]) + binario3
    return binario3
c = bin3(a) == bin3(b)
d = c*1
print(d)
#Problema 08
a = input()
b = input()
c = (a != b) and len(a) == len(b)
d = c*1
print(d)
#Problema 09
a = float(input())
b = float(input())
c = round(a,2) == round(b,2)
d = c*1
print(d)
#Problema 10
a = input()
b = input()
c = input()
d = (a > b) or (b >c and a>c)
e = d*1
print(e)
#Problema 11
a = int(input())
print(bin(a)[2:])