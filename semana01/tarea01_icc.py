#Problema 1
print("Problema 1")
n1 = 13
n_octal1 = 0
cifra1 = 0
while n1 >= 1:
    resto1 = n1 % 8
    n_octal1 = n_octal1 + resto1*(10**cifra1)
    cifra1 = cifra1 + 1
    n1 = n1//8
print("El numero 13 en el sistema octal es ", n_octal1)
print("")

#Problema 2
print("Problema 2")
n2 = 18
n_octal2 = 0
cifra2 = 0
while n2 >= 1:
    resto2 = n2 % 8
    n_octal2 = n_octal2 + resto2*(10**cifra2)
    cifra2 = cifra2 + 1
    n2 = n2//8
print("El numero 18 en el sistema octal es ", n_octal2)
print("")

#Problema 3
print("Problema 3")
n3 = 48
numero_hex3 = []
while n3 >= 1:
    resto3 = n3%16
    numero_hex3.insert(0, resto3)
    n3 = n3//16
for i in range(0,len(numero_hex3),1):
    if numero_hex3[i] == 10:
        numero_hex3.pop(i)
        numero_hex3.insert(i,"A")
    elif numero_hex3[i] == 11:
        numero_hex3.pop(i)
        numero_hex3.insert(i,"B")
    elif numero_hex3[i] == 12:
        numero_hex3.pop(i)
        numero_hex3.insert(i,"C")
    elif numero_hex3[i] == 13:
        numero_hex3.pop(i)
        numero_hex3.insert(i,"D")
    elif numero_hex3[i] == 14:
        numero_hex3.pop(i)
        numero_hex3.insert(i,"E")
    elif numero_hex3[i] == 15:
        numero_hex3.pop(i)
        numero_hex3.insert(i,"F")
numero_hex_final3 = ""
for i in range(0,len(numero_hex3),1):
    numero_hex_final3 = numero_hex_final3 + str(numero_hex3[i])
print("El número 48 en hexadecimal es ", numero_hex_final3)
print("")

#Problema 4
print("Problema 4")
n4 = 99
numero_hex4 = []
while n4 >= 1:
    resto4 = n4%16
    numero_hex4.insert(0, resto4)
    n4 = n4//16
for i in range(0,len(numero_hex4),1):
    if numero_hex4[i] == 10:
        numero_hex4.pop(i)
        numero_hex4.insert(i,"A")
    elif numero_hex4[i] == 11:
        numero_hex4.pop(i)
        numero_hex4.insert(i,"B")
    elif numero_hex4[i] == 12:
        numero_hex4.pop(i)
        numero_hex4.insert(i,"C")
    elif numero_hex4[i] == 13:
        numero_hex4.pop(i)
        numero_hex4.insert(i,"D")
    elif numero_hex4[i] == 14:
        numero_hex4.pop(i)
        numero_hex4.insert(i,"E")
    elif numero_hex4[i] == 15:
        numero_hex4.pop(i)
        numero_hex4.insert(i,"F")
numero_hex_final4 = ""
for i in range(0,len(numero_hex4),1):
    numero_hex_final4 = numero_hex_final4 + str(numero_hex4[i])
print("El número 99 en hexadecimal es ", numero_hex_final4)
print("")

#Problema 5
print("Problema 5")
n5 = 67
numero_hex5 = []
while n5 >= 1:
    resto5 = n5%16
    numero_hex5.insert(0, resto5)
    n5 = n5//16
for i in range(0,len(numero_hex5),1):
    if numero_hex5[i] == 10:
        numero_hex5.pop(i)
        numero_hex5.insert(i,"A")
    elif numero_hex5[i] == 11:
        numero_hex5.pop(i)
        numero_hex5.insert(i,"B")
    elif numero_hex5[i] == 12:
        numero_hex5.pop(i)
        numero_hex5.insert(i,"C")
    elif numero_hex5[i] == 13:
        numero_hex5.pop(i)
        numero_hex5.insert(i,"D")
    elif numero_hex5[i] == 14:
        numero_hex5.pop(i)
        numero_hex5.insert(i,"E")
    elif numero_hex5[i] == 15:
        numero_hex5.pop(i)
        numero_hex5.insert(i,"F")
numero_hex_final5 = ""
for i in range(0,len(numero_hex5),1):
    numero_hex_final5 = numero_hex_final5 + str(numero_hex5[i])
print("El número 67 en hexadecimal es ", numero_hex_final5)
print("")

#Problema 6
print("Problema 6")
n6 = 104
numero_en_binario6 = 0
cifra6 = 0
while (n6 >= 1) :
    resto6 = n6%2
    numero_en_binario6 = numero_en_binario6 + (resto6*(10**(cifra6)))
    cifra6 = cifra6 + 1
    n6 = n6//2

print("El número 104 en binario es: ", numero_en_binario6)
print("")

#Problema 7
print("Problema 7")
n7 = 254
numero_en_binario7 = 0
cifra7 = 0
while (n7 >= 1) :
    resto7 = n7%2
    numero_en_binario7 = numero_en_binario7 + (resto7*(10**(cifra7)))
    cifra7 = cifra7 + 1
    n7 = n7//2

print("El número 254 en binario es: ", numero_en_binario7)
print("")

#Problema 8
print("Problema 8")
n8 = 305
numero_hex8 = []
while n8 >= 1:
    resto8 = n8%16
    numero_hex8.insert(0, resto8)
    n8 = n8//16
for i in range(0,len(numero_hex8),1):
    if numero_hex8[i] == 10:
        numero_hex8.pop(i)
        numero_hex8.insert(i,"A")
    elif numero_hex8[i] == 11:
        numero_hex8.pop(i)
        numero_hex8.insert(i,"B")
    elif numero_hex8[i] == 12:
        numero_hex8.pop(i)
        numero_hex8.insert(i,"C")
    elif numero_hex8[i] == 13:
        numero_hex8.pop(i)
        numero_hex8.insert(i,"D")
    elif numero_hex8[i] == 14:
        numero_hex8.pop(i)
        numero_hex8.insert(i,"E")
    elif numero_hex8[i] == 15:
        numero_hex8.pop(i)
        numero_hex8.insert(i,"F")
numero_hex_final8 = ""
for i in range(0,len(numero_hex8),1):
    numero_hex_final8 = numero_hex_final8 + str(numero_hex8[i])
print("El número 305 en hexadecimal es ", numero_hex_final8)
print("")

#Problema 9
print("Problema 9")
n9 = 587
n_octal9 = 0
cifra9 = 0
while n9 >= 1:
    resto9 = n9 % 8
    n_octal9 = n_octal9 + resto9*(10**cifra9)
    cifra9 = cifra9 + 1
    n9 = n9//8
print("El numero 587 en el sistema octal es ", n_octal9)
print("")

#Problema 10
print("Problema 10")
n10 = 254
numero_en_binario10 = 0
cifra10 = 0
while (n10 >= 1) :
    resto10 = n10%2
    numero_en_binario10=numero_en_binario10+(resto10*(10**(cifra10)))
    cifra10 = cifra10 + 1
    n10 = n10//2

print("El número 254 en binario es: ", numero_en_binario10)
print("")

#Problema 11
print("Problema 11")
n11 = 1023
numero_en_binario11 = 0
cifra11 = 0
while (n11 >= 1) :
    resto11 = n11%2
    numero_en_binario11=numero_en_binario11+(resto11*(10**(cifra11)))
    cifra11 = cifra11 + 1
    n11 = n11//2

print("El número 1023 en binario es: ", numero_en_binario11)
print("")

#Problema 12
print("Problema 12")
n12 = 1054
numero_hex12 = []
while n12 >= 1:
    resto12 = n12%16
    numero_hex12.insert(0, resto12)
    n12 = n12//16
for i in range(0,len(numero_hex12),1):
    if numero_hex12[i] == 10:
        numero_hex12.pop(i)
        numero_hex12.insert(i,"A")
    elif numero_hex12[i] == 11:
        numero_hex12.pop(i)
        numero_hex12.insert(i,"B")
    elif numero_hex12[i] == 12:
        numero_hex12.pop(i)
        numero_hex12.insert(i,"C")
    elif numero_hex12[i] == 13:
        numero_hex12.pop(i)
        numero_hex12.insert(i,"D")
    elif numero_hex12[i] == 14:
        numero_hex12.pop(i)
        numero_hex12.insert(i,"E")
    elif numero_hex12[i] == 15:
        numero_hex12.pop(i)
        numero_hex12.insert(i,"F")
numero_hex_final12 = ""
for i in range(0,len(numero_hex12),1):
    numero_hex_final12 = numero_hex_final12 + str(numero_hex12[i])
print("El número 1054 en hexadecimal es ", numero_hex_final12)
print("")

#Problema 13
print("Problema 13")
n13 = 3054
n_octal13 = 0
cifra13 = 0
while n13 >= 1:
    resto13 = n13 % 8
    n_octal13 = n_octal13 + resto13*(10**cifra13)
    cifra13 = cifra13 + 1
    n13 = n13//8
print("El numero 3054 en el sistema octal es ", n_octal13)
print("")

#Problema 14
print("Problema 14")
n14 = 5785
numero_en_binario14 = 0
cifra14 = 0
while (n14 >= 1) :
    resto14 = n14%2
    numero_en_binario14=numero_en_binario14+(resto14*(10**(cifra14)))
    cifra14 = cifra14 + 1
    n14 = n14//2

print("El número 5785 en binario es: ", numero_en_binario14)
print("")

#Problema 15
print("Problema 15")
n15 = 15850
numero_hex15 = []
while n15 >= 1:
    resto15 = n15%16
    numero_hex15.insert(0, resto15)
    n15 = n15//16
for i in range(0,len(numero_hex15),1):
    if numero_hex15[i] == 10:
        numero_hex15.pop(i)
        numero_hex15.insert(i,"A")
    elif numero_hex15[i] == 11:
        numero_hex15.pop(i)
        numero_hex15.insert(i,"B")
    elif numero_hex15[i] == 12:
        numero_hex15.pop(i)
        numero_hex15.insert(i,"C")
    elif numero_hex15[i] == 13:
        numero_hex15.pop(i)
        numero_hex15.insert(i,"D")
    elif numero_hex15[i] == 14:
        numero_hex15.pop(i)
        numero_hex15.insert(i,"E")
    elif numero_hex15[i] == 15:
        numero_hex15.pop(i)
        numero_hex15.insert(i,"F")
numero_hex_final15 = ""
for i in range(0,len(numero_hex15),1):
    numero_hex_final15 = numero_hex_final15 + str(numero_hex15[i])
print("El número 15850 en hexadecimal es ", numero_hex_final15)
print("")
