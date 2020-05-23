#Programa principal de recomendaciones
print("-----------------------------------------")
print("Bienvenido al sistema de recomendaciones")

print("1. Recomendar por rango de costos")
print("2. Recomendar por ubicacion")
print("3. Recomendar por especialidad")
print("4. Recomendar por servicio a domicilio")
print("5. Recomendar por valoración")
print("6. Salir")
print("-----------------------------------------")
try:
    opcion = int(input())
except:
    print("Error ingresaste mal una opcion")
    
if(opcion==1):
    print("Ingrese su precio a gastar: ")
    precio=float(input())
elif(opcion==2):
    print("En que zona se encuentra")
    zona = input()
    
elif(opcion==3):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Ingrese su especialidad: ")
    print("1. Comida rápida")
    print("2. Ensaladas")
    print("3. Carnes")
    print("4. Pizzas")
    print("5. Postres")
    print("6. Comida china")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    especialidad=input()
    
elif(opcion==4):
    print("En que zona te encuentras: ")
    zonaUsuario= input()
elif(opcion==5):
    print("Valoracion")
else:
    print("FIN PROGRAMA")