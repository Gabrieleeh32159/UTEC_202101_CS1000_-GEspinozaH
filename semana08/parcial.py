import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/pshiguihara/AmazonSageMaker/master/MatrizDatos2.csv"
datos = pd.read_csv(url)
def opcion1():
  print("Bienvenido a la opción [1]")
  list = [int(x) for x in datos["COSTO ALQUILER DIARIO"]]
  lista2 = sorted(list)
  n = int(input("N: "))
  for i in range(len(list)-1, len(list)-n-1 , -1):
    print(lista2[i])

def opcion2():
  print("Opción 2")
  print("="*20)
  N = int(input("N: "))
  datos2 = datos.groupby(['CODIGO INMUEBLE']).agg({'DIAS ALQUILER':np.mean})
  print(datos2.head(N))

def opcion3():
  print("Bienvenido a la opción [3] Mostrar los registros donde la ciudad sea Arequipa, la categoría sea departamentos y el estado de transacción devuelto")
  print("="*20)
  N = int(input("Ingrese N: "))
  booleanos = (datos['CIUDAD']== "AREQUIPA") & (datos['CATEGORIA']=="DEPARTAMENTO") & (datos['ESTADO TRANSACCION']=="DEVUELTO")
  la_data = datos[booleanos]
  print(la_data.head(N))

def opcion4():
  datos2 = datos[datos["TIPO"] == "ALQUILER"].groupby(['CATEGORIA','ESTADO TRANSACCION']).size()
  print(datos2)

def opcion5():
  print("Bienvenido a la opción [5] Mostrar los primeros N registros")
  print("="*40)
  print(datos.groupby(['CIUDAD','CATEGORIA']).agg({'COSTO ALQUILER DIARIO':np.mean,'TOTAL ALQUILER':np.size}))


def opcion6():
  print("Opción 6")
  print("="*20)
  bool = (datos["TIPO"] == "ALQUILER") & (datos["ESTADO TRANSACCION"] == "DEVUELTO")
  datos2 = datos[bool]
  city = input("Ciudad: ")
  datos3 = datos2[datos2["CIUDAD"] == city]
  prom = np.mean(datos3["COSTO ALQUILER DIARIO"])
  mayor = max(datos3["COSTO ALQUILER DIARIO"])
  menor = min(datos3["COSTO ALQUILER DIARIO"])
  suma = sum(datos3["COSTO ALQUILER DIARIO"])
  prom_alq_total = np.mean(datos3["TOTAL ALQUILER"])
  print(f"Elcosto de alquiler diario promedio de la ciudad es {prom}")
  print(f"El registro con el mayor costo de alquier diario de {city} es {mayor}")
  print(f"El registro con el menor costo de alquier diario de {city} es {menor}")
  print(f"La suma de los costos de alquiler diario de las transacciones de {city} es {suma}")
  print(f"El promedio del total alquiler de {city} es {prom_alq_total}")

def menu():
  opc = 0
  while (opc!=7):
    print("Bienvenido a nuestro Programa")
    print("="*40)
    print("[1] Seleccionar las N transacciones con mayor costo de alquiler diario")
    print("[2] Seleccionar N inmuebles y reportar los promedios de dias de alquiler de cada uno")
    print("[3] Mostrar los registros donde la ciudad sea Arequipa, la categoría sea departamentos y el estado de transacción devuelto")
    print("[4] Resumir el número de registros por categoría y estado de transacción, considerando solo el tipo alquiler")
    print("[5]  Hacer un resumen por Ciudad y categoría, para mostrar el promedio de días de alquiler y el importe total recaudado")
    print("[6]  Buscador Universal")
    
    opc = int(input("Opción: "))
    if opc==1:
      opcion1()
    elif opc==2:    
      opcion2()
    elif opc==3:
      opcion3()
    elif opc==5:    
      opcion5()
    elif opc==6:    
      opcion6()
    print(""*10)     