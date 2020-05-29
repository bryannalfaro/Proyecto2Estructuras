from neo4j import GraphDatabase

#Programa principal de recomendaciones


graphdb = GraphDatabase.driver(uri="neo4j://localhost:7687", auth= ("neo4j", "1234"), encrypted=False)

session = graphdb.session()


#WITH lugar.valoracion as rating, lugar.name as l
#RETURN l, rating
#ORDER BY rating DESC

def sendQuery(query):
    query += " WITH lugar.valoracion as rating, lugar.name as l RETURN l, rating ORDER BY rating DESC"
    nodes = session.run(query)
    for node in nodes:
        stars = ''
        for r in range (0, int(node[1])):
            stars += '✰'
        print(node[0] + " " + stars)

opcion=0

print("-----------------------------------------")
print("Bienvenido al sistema de recomendaciones")
while(opcion != 6):
    print("1. Recomendar por rango de costos")
    print("2. Recomendar por servicio a domicilio")
    print("3. Recomendar por especialidad")
    print("4. Recomendar por ubicacion")

    print("6. Salir")
    print("-----------------------------------------")
    try:
        opcion = int(input()) 
    except:
        print("Error ingresaste mal una opcion")
        
    if(opcion==1):
        print("Ingrese su precio a gastar: ")
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. 10-150")
        print("2. 150-300")
        print("3. 300-500")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        precio = int(input())
        
        if(precio==1):
            q1 = "MATCH(precio {name: '10-150'}) <-- (lugar)"
            print("Los que estan en tu rango de precio son: ")
            sendQuery(q1)
            
        if(precio==2):
            q1 = "MATCH(precio {name: '150-300'}) <-- (lugar)"
            print("Los que estan en tu rango de precio son: ")
            sendQuery(q1)
            
        if(precio==3):
            q1 = "MATCH(precio {name: '300-500'}) <-- (lugar)"
            print("Los que estan en tu rango de precio son: ")
            sendQuery(q1)
        
    elif(opcion==2):
        print("Estos tienen servicio")
        q1 = "MATCH(servicio {name: 'Si'}) <-- (lugar)"
        print("Los que tienen servicio son: ")
        sendQuery(q1)
        
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
        if(especialidad=="1"):
            q1 = "MATCH(especialidad {name: 'Comida Rapida'}) <-- (lugar)"
            print("Te recomendamos comer en: ")
            sendQuery(q1)
            
        if(especialidad=="2"):
            q1 = "MATCH(especialidad {name: 'Ensalada'}) <-- (lugar)"
            print("Te recomendamos comer en: ")
            sendQuery(q1)
            
        if(especialidad=="3"):
            q1 = "MATCH(especialidad {name: 'Carnes'}) <-- (lugar)"
            print("Te recomendamos comer en: ")
            sendQuery(q1)
            
        if(especialidad=="4"):
            q1 = "MATCH(especialidad {name: 'Pizzas'}) <-- (lugar)"
            print("Te recomendamos comer en: ")
            sendQuery(q1)
            
        if(especialidad=="5"):
            q1 = "MATCH(especialidad {name: 'Postres'}) <-- (lugar)"
            print("Te recomendamos comer en: ")
            sendQuery(q1)
                
        if(especialidad=="6"):
            q1 = "MATCH(especialidad {name: 'Comida China'}) <-- (lugar)"
            nodes = session.run(q1)
            print("Te recomendamos comer en: ")
            sendQuery(q1)
        
    elif(opcion==4):
        print("En que zona te encuentras: ")
        zonaUsuario= input()
        q1 = "MATCH(zona {name: 'Zona " +zonaUsuario+"'}) <-- (lugar)"
        sendQuery(q1)
            
    else:
        print("FIN PROGRAMA")
        
        



