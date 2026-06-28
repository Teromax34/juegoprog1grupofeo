def peliculas():
    cont = 0
    cont_error = 0
    print("Pregunta 1")
    opcion = input("Un hombre azul llega a un planeta llamado Pandora: \n1-Avatar\n2-Titanic\n3-Avengers\n")
    if opcion == "1":
        print("Correcto")
        cont +=1
    else:
        print("Incorrecto")
        cont_error += 1
    print("Pregunta 2")
    opcion = input("Un barco choca contra un iceberg: \n1-Frozen \n2-Avatar \n3-Titanic\n")
    if opcion == "3":
        print("Correcto")
        cont +=1
    else:
        print("Incorrecto")
        cont_error += 1
    print("Pregunta 3")
    opcion = input("Un grupo de superhéroes se une para derrotar a Thanos: \n1- Batman \n2-Avengers Endgame \n3-Toy Story\n")
    if opcion == "2":
        print("Correcto")
        cont +=1
    else:
        print("Incorrecto")
        cont_error += 1
    print("Pregunta 4")
    opcion = input("Un pez payaso busca a su hijo perdido en el océano: \n1-Buscando a Nemo \n2-Cars \n3-Ratatouille\n")
    if opcion == "1":
        print("Correcto")
        cont +=1
    else:
        print("Incorrecto")
        cont_error += 1
    print("Pregunta 5")
    opcion = input("Un chef es en realidad una rata que cocina en París: \n1-Ratatouille \n2-Coco \n3-Intensamente\n")
    if opcion == "1":
        print("Correcto")
        cont +=1
    else:
        print("Incorrecto")
        cont_error += 1
        
    porc = (cont * 100) / (cont + cont_error)
    print(f"Los aciertos que tuviste fueron: {cont}")
    print(f"Los errores fueron: {cont_error}")
    print(f"El porcentaje de acierto es de: {porc}%")
    
peliculas()