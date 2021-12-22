#                    Declaracion de Librerias a Utilizar
from os import write
import requests 
from datetime import date, datetime

#                     Titulo de la Aplicación a Mostrar 
print("Mercado de Criptiomonedas")
print("\n")
#                              Primera Funcion 
#                    Nombre de Primera funcion a Utilizar 
print("Calculadora de Criptomonedas", )
print("\n")
#                    Programacion de la Primera Funcion
criptomoneda_nombre=input("Ingresa el Simbolo de la Criptomoneda que Tienes: ")
criptomoneda_cantidad=float(input("Cantidad que Tienes de Criptomonedas: "))
criptomoneda_valor=float(input("Precio al que compraste tu criptomoneda en USD: "))
valor_total=criptomoneda_cantidad*criptomoneda_valor
fecha=datetime.now()
print("La cantidad de dinero gastaste en USD: ", valor_total)
print("Fecha y hora en que registraste", fecha.strftime("%A %d/%m/%y %H:%M:%S") )

#                              Segunda Funcion 
#                     Funcion para Guardar la Criptomoneda 
def esmoneda(cripto):
    return cripto in monedas

#                      Funcion par Guardar los datos de la Pagina 
def nombre(cripto): 
    monedas_dict={}
    for coin in data["data"]:
        monedas_dict[coin["symbol"]]=coin["name"]
    return monedas_dict.get(cripto) 

#                        Inicializamos Variables a Utilizar
monedas=()
diccionario={}

#                        Solicitud para llemar los valores de las Criptomonedas
COINMARKET_API_KEY = "c0cbebee-21f4-44cc-8d59-bcb993490e45" 
headers = { 
  'Accepts': 'application/json', 
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY 
}

#                         Pagina Donde se Toman los Precios Nombre y Sigla 
data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",
        headers=headers).json() 

#                              Funciones y Parametros 
for cripto in data["data"]:
    diccionario[cripto["symbol"]]=cripto["quote"]["USD"]["price"] 
monedas = diccionario.keys() 
print("\n")
print("Listas de Criptomonedas que Deseas Consultar")
#                          Solicitamos  las Criptomonedas 
moneda=input("Indique la primera criptomoneda que desea conocer: ")   
moneda1=input("Indique la segunda criptomoneda que desea conocer: ")  
moneda2=input("Indique la tercera criptomoneda que desea conocer: ")  


#                       Evaluación si existen las criptomone
while not esmoneda(moneda) & esmoneda(moneda1) & esmoneda(moneda2): 
        print("Moneda no se Encuentra la Base de Datos .")
        moneda=input("Ingrese la Primera Criptomoneda: ")
        moneda1=input("Ingrese la Segunda Criptomoneda: ")
        moneda2=input("Ingrese la Tercera Criptomoneda: ")
else:
#                           Impresion de Resultados     
    print("Datos de las Criptomonedas que Escogiste")
    print("La primera criptomoneda es: ",nombre(moneda)," con simbolo:",moneda,
        " precio en USD:",diccionario.get(moneda))
    print("La segunda criptomoneda es: ",nombre(moneda1)," con symbol:",moneda1,
        " precio en USD:",diccionario.get(moneda1)),
    print("La tercera criptomoneda es: ",nombre(moneda2)," con symbol:",moneda2,
        "precio en USD:",diccionario.get(moneda2))
    print("Datos obtenidos en binance.com", ", El dia y a la hora",fecha.strftime("%A %d/%m/%y %H:%M:%S"))

#                                       Tercera Funcion
print("\n")
print("Comparacion de Precio cuando compra la Criptomoneda a precio actual")
while not esmoneda(criptomoneda_nombre):
    print("La Criptomoneda que tienes hace parte de las registrada: ")

#                        Muestra de los valores y Comparación de los precios de la criptomoneda 
print("El valor en el momento que la comprates es:",criptomoneda_valor)
print("El valor en que se encuentra en este momento:", diccionario.get(criptomoneda_nombre))
print("Fecha y hora en que se consulto:",fecha.strftime("%A %d/%m/%y %H:%M:%S") )

#                                      Cuarta Funcion 

#                              Balance de criptomoneda 
print("\n")
print("Balance de la Criptomoneda")
print("Nombre de Criptomoneda")
print(nombre(criptomoneda_nombre))
print("Simbolo de Criptomoneda")
print(criptomoneda_nombre)
print("Numero de Critomonedas Compradas")
print(criptomoneda_cantidad)
print("Precio al que se Compraron Inicialmente")
print(criptomoneda_valor)
print("El valor en que se encuentra en este momento:")
print(diccionario.get(criptomoneda_nombre))
print("Dinero Invertido en el momento de la Compra de la Criptomoneda USD:")
print(valor_total)
valor_final=float(diccionario.get(criptomoneda_nombre))*criptomoneda_cantidad
print("Dinero Recibido por el numero de Criptomoneda al valor de Hoy:")
print(valor_final)
ganancia=float(valor_final)-valor_total
print("Ganancia Obtenida: ")
print(ganancia)

#                                    Quinta Funcion 

#                     Se guarda las trasacciones hechas por el usuario y se genera un achivo.txt
memorias_datos=open("Copia de Transacciones.txt", "w")
memorias_datos.write("Transacciones realizadas por el Usuario\n")
memorias_datos.write("\n")
memorias_datos.write("Datos dado por el Usuario\n")
memorias_datos.write("Nombre de Criptomoneda \n")
memorias_datos.write(criptomoneda_nombre + "\n")
memorias_datos.write("Cantidad de Criptomonedas \n")
memorias_datos.write(str(criptomoneda_cantidad) + "\n")
memorias_datos.write("Precio de Compra de la Criptomoneda\n")
memorias_datos.write(str(criptomoneda_valor) + "\n")
memorias_datos.write("Dinero Invertido por las Criptomonedas\n")
memorias_datos.write(str(valor_total) + "\n")
memorias_datos.write("Fecha y Hora en que se realizo el registro\n")
memorias_datos.write(str(fecha) + "\n")
memorias_datos.write("\n")
memorias_datos.write("Datos solicitados a la Pagina\n")
memorias_datos.write("Simbolos de las Criptomonedas a Solicitar \n")
memorias_datos.write(str(moneda) + "\n")
memorias_datos.write(str(moneda1) + "\n")
memorias_datos.write(str(moneda2) + "\n")
memorias_datos.write("Precio Actual de las Criptomonedas\n")
memorias_datos.write(str(diccionario.get(moneda)) + "\n")
memorias_datos.write(str(diccionario.get(moneda1)) + "\n")
memorias_datos.write(str(diccionario.get(moneda2)) + "\n")
memorias_datos.write("\n")
memorias_datos.write("Comparacion de Valor que se Tiene a Valor dado por la Pagina \n")
memorias_datos.write(str(criptomoneda_valor) + "\n")
memorias_datos.write(str(diccionario.get(criptomoneda_nombre)) + "\n")
memorias_datos.close()

#                        Guardar datos de las criptomonedas que se consultaron
memoria_criptomoneda=open("Listas de Criptomonedas.txt","w")
memoria_criptomoneda.write("Criptomonedas Guardadas\n")
memoria_criptomoneda.write("\n")
memoria_criptomoneda.write("Primera Criptomonedas\n")
memoria_criptomoneda.write(str(moneda) + "\n")
memoria_criptomoneda.write(str(diccionario.get(moneda)) + "\n")
memoria_criptomoneda.write("\n")
memoria_criptomoneda.write("Segunda Criptomonedas\n")
memoria_criptomoneda.write(str(moneda1) + "\n")
memoria_criptomoneda.write(str(diccionario.get(moneda1)) + "\n")
memoria_criptomoneda.write("\n")
memoria_criptomoneda.write("Tercera Criptomonedas\n")
memoria_criptomoneda.write(str(moneda2) + "\n")
memoria_criptomoneda.write(str(diccionario.get(moneda2)) + "\n")
memoria_criptomoneda.close()