def opcion1():
  print("Bienvenido a la opción [1] Mostrar los primeros N registros")
  print("="*40)
  N = int(input("Ingrese N: "))
  print(datos.head(N))

def opcion2():  
  print("Bienvenido a la opción [2] Mostrar registros con las columnas time, day y sex")
  print("="*40)
  print(datos[['time','day','sex']])


def menu():
  opc=1
  while (opc!=3):
    print("Bienvenido a nuestro Programa")
    print("="*40)
    print("[1] Mostrar los primeros N registros")
    print("[2] Mostrar registros con las columnas time, day y sex")
    print("[3] Salir")
    opc = int(input("Opción: "))
    if opc==1:
      opcion1()
    elif opc==2:    
      opcion2()
    print(""*10)

import pandas as pd
url = "https://raw.github.com/pandas-dev/pandas/master/pandas/tests/io/data/csv/tips.csv"
datos = pd.read_csv(url)
menu()
print(datos.head())
bool1 = (datos['day']=='Fri')
bool2 = (datos['day']=='Sat')
bool3 = (datos['day']=='Sun')
bool4 = bool1 | bool2 | bool3
feriados = []
for i in range(len(bool4)):
  if bool4[i] == True:
    feriados.append('Feriado')
  else:  
    feriados.append('Día de semana')
print(feriados)
datos.assign(feriado=feriados)