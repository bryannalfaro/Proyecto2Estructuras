from neo4j import GraphDatabase

#Programa principal de recomendaciones


graphdb = GraphDatabase.driver(uri="neo4j://localhost:7687", auth= ("neo4j", "1234"), encrypted=False)

session = graphdb.session()

menu_filtros = "Desea utilizar otro filtro?\n1. Si\n2. No"
filtros_disponibles = ["Recomendar por rango de costos", "Recomendar por servicio a domicilio", "Recomendar por especialidad", "Recomendar por ubicación",
                       "Recomendar por valoracion"]
numeracion = 0

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
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. 10-150")
        print("2. 150-300")
        print("3. 300-500")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        precio = int(input())
        print(menu_filtros)
        opcion_filtro = int(input())
        
        if(opcion_filtro == 1):
            filtros_disponibles.remove("Recomendar por rango de costos")
            for item in filtros_disponibles:
                numeracion = numeracion + 1
                print(str(numeracion) + ". " + item)
            opcion_filtrado = int(input())
            
        else:
        
        
            if(precio==1):
                q1 = "MATCH(precio {name: '10-150'}) <-- (lugar) RETURN lugar.name"
                nodes = session.run(q1)
                print("Los que estan en tu rango de precio son: ")
                for node in nodes:
                    print(node[0])
            if(precio==2):
                q1 = "MATCH(precio {name: '150-300'}) <-- (lugar) RETURN lugar.name"
                nodes = session.run(q1)
                print("Los que estan en tu rango de precio son: ")
                for node in nodes:
                    print(node[0])
            if(precio==3):
                q1 = "MATCH(precio {name: '300-500'}) <-- (lugar) RETURN lugar.name"
                nodes = session.run(q1)
                print("Los que estan en tu rango de precio son: ")
                for node in nodes:
                    print(node[0])
            
        
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
        
        

