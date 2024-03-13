bandas = [] #No sabemos el numero de bandas y por eso se pone vacia
banda = {} #Objeto(Diccionario)

#Construyendo la interfaz
print("***ALTAVOZ ES TU VOZ***")
print("***********************")

opcion = 100
while(opcion != 5):
    
    print("1. Registrar Banda")
    print("2. Buscar Informacion de una Banda")
    print("3. Listar agenda del evento")
    print("4. Modificar una Banda")
    print("5. SALIR")
    
    opcion = int(input("Dijita una opcion: "))

    if opcion == 1:
        banda = {} #Objeto(Diccionario) *Se coloca dentro del bucle para que cada vez que termine el ciclo limpie y agregue datos nuevos
        #Creando los datos del diccionario
        banda ["id"] = int(input("Dijita el id: "))
        banda ["nombre"] = input("Nombre de la banda: ")
        banda ["genero"] = input("Genero: ")
        banda ["clasificacion"] = input("Clasificacion: ")
        banda ["tiempo"] = int(input("Tiempo: "))
        banda ["costo"] = int(input("Costo: $"))
        
        #Agregando un diccionario a una lista
        bandas.append(banda)
        
    elif opcion == 2:
        
        bandaBuscada = input("Dijita el nonmbre de la banda que estas buscando: ")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"] == bandaBuscada:
                #Como lo encontre muestro los datos de BandAuxiliar
              print(f"id: {bandAuxiliar["id"]} \n nombre: {bandAuxiliar["nombre"]} ")  
            else:
                print("Parce siga buscando... oooo")
         
    elif opcion == 3:
        print(bandas)
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else: 
        pass