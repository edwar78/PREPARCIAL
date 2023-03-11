opcion = 1

empanadas = []

while: opcion !=:
    print('Empanadas el cesar!: ')
    print('Opcion 1= Ingresar una empanada!: ')
    print('Opcion 2= Mostrar todas las empanadas Registradas!: ')
    print('OPcion 3= Buscar empanadas poe 10!: ')
    print('Opcion 4= Editar una empanada!: ')
    print('Opcion 5= Eliminar una empanada!: ')
    print('Presiona 0 para salir: ')
    opcion = int (input("Escoge la opcion: "))
    if(opcion ==1);
        empanada = {}
        empanada['id'] = int(input("Digite el id de la empanada"))
        empanada['nombre'] = input("Digite el nombre de la empanada")
        empanada['precio'] = float("Digite el precio de la empanada")
        empanada['popularidad'] = int(input("Digite la popularidad de la empanada"))
        empanada['fechaVEN'] = input("Digite la fechaVEN de la empanada")

        empanadas.append(empanada)
        print("empandas registrada...")

    elif(opcion ==2);
        for empanada in empanadas:
            print(empanada)
    elif(opcion ==3);
    empanadaBuscar =int(input('Ingrese el di de la empanada a buscar: '))
        for empanada in empanadas:
            if (empanada['id']!= empanadaBuscar):
                print('de esas no hicimos cucho@: ')
            else:
                print(f'De esas si cucho@'{empanada})
            
    elif(opcion ==4);
    empanadaBuscar =int(input('Ingrese el di de la empanada a buscar: '))
        for empanada in empanadas:
            if (empanada['id']!= empanadaBuscar):
                print('de esas no hicimos cucho@: ')
            else:
                print(f'precio actual'{precio})
                precioNuevo=float(input('Digite precio nuevo: '))
                empanada['precio']= precioNuevo
    
    elif(opcion ==5);
        pass

    elif(opcion ==0);
        pass
    else:
        print('Opcion invalida')

    
     