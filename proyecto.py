from neo4j import GraphDatabase

#Programa principal de recomendaciones


graphdb = GraphDatabase.driver(uri="neo4j://localhost:7687", auth= ("neo4j", "1234"), encrypted=False)

session = graphdb.session()

opcion=0
print("-----------------------------------------")
print("Bienvenido al sistema de recomendaciones")
while(opcion != 6):
    print("1. Recomendar por rango de costos")
    print("2. Recomendar por servicio a domicilio")
    print("3. Recomendar por especialidad")
    print("4. Recomendar por ubicacion")
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
        print("Estos tienen servicio")
        
        q1 = "MATCH(servicio {name: 'Si'}) <-- (lugar) RETURN lugar.name"
        nodes = session.run(q1)
        print("Los que tienen servicio son: ")
        for node in nodes:
            print(node[0])
        
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
            q1 = "MATCH(especialidad {name: 'Comida Rapida'}) <-- (lugar) RETURN lugar.name"
            nodes = session.run(q1)
            print("Te recomendamos comer en: ")
            for node in nodes:
                print(node[0])
        if(especialidad=="2"):
            q1 = "MATCH(especialidad {name: 'Ensalada'}) <-- (lugar) RETURN lugar.name"
            nodes = session.run(q1)
            print("Te recomendamos comer en: ")
            for node in nodes:
                print(node[0])
        if(especialidad=="3"):
            q1 = "MATCH(especialidad {name: 'Carnes'}) <-- (lugar) RETURN lugar.name"
            nodes = session.run(q1)
            print("Te recomendamos comer en: ")
            for node in nodes:
                print(node[0])
        if(especialidad=="4"):
            q1 = "MATCH(especialidad {name: 'Pizzas'}) <-- (lugar) RETURN lugar.name"
            nodes = session.run(q1)
            print("Te recomendamos comer en: ")
            for node in nodes:
                print(node[0])
        if(especialidad=="5"):
            q1 = "MATCH(especialidad {name: 'Postres'}) <-- (lugar) RETURN lugar.name"
            nodes = session.run(q1)
            print("Te recomendamos comer en: ")
            for node in nodes:
                print(node[0])
                
        if(especialidad=="6"):
            q1 = "MATCH(especialidad {name: 'Comida China'}) <-- (lugar) RETURN lugar.name"
            nodes = session.run(q1)
            print("Te recomendamos comer en: ")
            for node in nodes:
                print(node[0])
        
    elif(opcion==4):
        print("En que zona te encuentras: ")
        zonaUsuario= input()
        q1 = "MATCH(zona {name: 'Zona " +zonaUsuario+"'}) <-- (lugar) RETURN lugar.name"
        nodes = session.run(q1)
        for node in nodes:
            print(node[0])
            
    elif(opcion==5):
        print("Valoracion")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Ingrese la valoracion que desea: ")
        print("1")
        print("2")
        print("3")
        print("4")
        print("5")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        valoracion = input()
       
        q1 = "MATCH(valoracion {name: '"+valoracion+"'}) <-- (lugar) RETURN lugar.name"
        nodes = session.run(q1)
        for node in nodes:
            print(node[0])
    else:
        print("FIN PROGRAMA")
