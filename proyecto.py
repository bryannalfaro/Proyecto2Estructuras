from neo4j import GraphDatabase

#Programa principal de recomendaciones

#Conexión con la base de datos
graphdb = GraphDatabase.driver(uri="neo4j://localhost:7687", auth= ("neo4j", "1234"), encrypted=False)
session = graphdb.session()

#Funciones para filtrar recomendaciones por su valoracion y por su peso
def sendQuery(query):
    temp = query
    query += " WITH lugar.valoracion as rating, lugar.name as l, arista.relacion as peso WHERE peso = 1 RETURN l, rating ORDER BY rating DESC"
    nodes = session.run(query)
    for node in nodes:
        stars = ''
        for r in range (0, int(node[1])):
            stars += '✰'
        print(node[0] + " " + stars)
    temp += " WITH lugar.valoracion as rating, lugar.name as l, arista.relacion as peso WHERE peso <> 1 RETURN l, rating, peso ORDER BY peso DESC LIMIT 4"
    nodesRec = session.run(temp)
    print("Pero tambien le recomendamos estos restaurantes:")
    for node in nodesRec:
        stars = ''
        for r in range (0, int(node[1])):
            stars += '✰'
        print(node[0] + " " + stars)
    enter = input("Presione la tecla Enter para continuar: ")
        
def sendQuerySimple(query):
    query += " WITH lugar.valoracion as rating, lugar.name as l RETURN l, rating ORDER BY rating DESC"
    nodes = session.run(query)
    for node in nodes:
        stars = ''
        for r in range (0, int(node[1])):
            stars += '✰'
        print(node[0] + " " + stars)
    enter = input("Presione la tecla Enter para continuar: ")

#Menu principal
opcion=0
print("--------------------------------------------")
print("| Bienvenido al sistema de recomendaciones |")
print("--------------------------------------------")

#Ciclo de opciones
while(opcion != 6):
    print("\n--------------------------------------------")
    print("| 1. Recomendar por rango de costos        |")
    print("| 2. Recomendar por servicio a domicilio   |")
    print("| 3. Recomendar por especialidad           |")
    print("| 4. Recomendar por ubicacion              |")
    print("| 5. Agregar o eliminar restaurantes       |")
    print("| 6. Salir                                 |")
    print("--------------------------------------------")
    #Programación defensiva
    try:
        print("\nIngresa la opción de la recomendación que deseas:")
        opcion = int(input("---> ")) 
    except:
        print("Error ingresaste mal una opcion")
        
    #Opción de rango de costos
    if(opcion==1):
        print("\nUsted a seleccionado: Recomendar por rango de costo")
        print("Ingrese el rango de dinero que desea gastar: ")
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("| 1. Q10 - Q150         |")
        print("| 2. Q150 - Q300        |")
        print("| 3. Q300 - Q500        |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        precio = int(input("---> "))
        
        if(precio==1):
            q1 = "MATCH(precio {name: '10-150'}) <-[arista]- (lugar)"
            print("Los que estan en tu rango de precio son: \n")
            sendQuery(q1)
            
        if(precio==2):
            q1 = "MATCH(precio {name: '150-300'}) <-[arista]- (lugar)"
            print("Los que estan en tu rango de precio son: \n")
            sendQuery(q1)
            
        if(precio==3):
            q1 = "MATCH(precio {name: '300-500'}) <-[arista]- (lugar)"
            print("Los que estan en tu rango de precio son: \n")
            sendQuery(q1)
        
    #Filtrar por servicio a domicilio
    elif(opcion==2):
        print("Listado de restaurantes con servicio a domicilio: \n")
        q1 = "MATCH(servicio {name: 'Si'}) <-[arista]- (lugar)"
        sendQuerySimple(q1)
        
    #Recomendar por especialidad
    elif(opcion==3):
        print("Ingrese la especialidad que desea: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("| 1. Comida rápida       |")
        print("| 2. Ensaladas           |")
        print("| 3. Carnes              |")
        print("| 4. Pizzas              |")
        print("| 5. Postres             |")
        print("| 6. Comida china        |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        especialidad = input("---> ")
        if(especialidad=="1"):
            q1 = "MATCH(especialidad {name: 'Comida Rapida'}) <-[arista]- (lugar)"
            print("Te recomendamos comer en: \n")
            sendQuery(q1)
            
        if(especialidad=="2"):
            q1 = "MATCH(especialidad {name: 'Ensalada'}) <-[arista]- (lugar)"
            print("Te recomendamos comer en: \n")
            sendQuery(q1)
            
        if(especialidad=="3"):
            q1 = "MATCH(especialidad {name: 'Carnes'}) <-[arista]- (lugar)"
            print("Te recomendamos comer en: \n")
            sendQuery(q1)
            
        if(especialidad=="4"):
            q1 = "MATCH(especialidad {name: 'Pizzas'}) <-[arista]- (lugar)"
            print("Te recomendamos comer en: ")
            sendQuery(q1)
            
        if(especialidad=="5"):
            q1 = "MATCH(especialidad {name: 'Postres'}) <-[arista]- (lugar)"
            print("Te recomendamos comer en: ")
            sendQuery(q1)
                
        if(especialidad=="6"):
            q1 = "MATCH(especialidad {name: 'Comida China'}) <-[arista]- (lugar)"
            print("Te recomendamos comer en: ")
            sendQuery(q1)
        
    #Filtrar restaurantes por zonas
    elif(opcion==4):
        print("En que zona te encuentras: ")
        zonaUsuario= input()
        q1 = "MATCH(zona {name: 'Zona " +zonaUsuario+"'}) <-[arista]- (lugar)"
        sendQuerySimple(q1)
    elif(opcion==5):
        print("1. Agregar un restaurante")
        print("2. Eliminar un restaurante")
        opcion3 = int(input("---> "))
        if(opcion3==1):
            nombre = input("Ingresa el nombre del restaurante: ")
            especialidad = input("Ingrese la especialidad: ")
            rating = int(input("Ingrese el rating: "))
            zona = int(input("Ingrese la zona en la que esta ubicado: "))
            print("Restaurante agregado")
        elif(opcion3==2):
            eliminarrestaurante = input("Ingrese el nombre del restaurante que desea eliminar: ")
            "MATCH(a:lugar{name:'"+eliminarrestaurante+"'})"
            "DETACH DELETE a"
            print("Restaurante eliminado")
        else:
            print("Opción no válida")
    
    
    elif(opcion==6):
        print("Gracias por utilizar el programa.")
        break
    else:
        print("Opcion no válida")