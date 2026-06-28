def peliculas():
    cont = 0
    cont_error = 0
    preguntas = [
        {"pregunta": "Un hombre azul llega a un planeta llamado Pandora:",
         "opciones": ["Avatar", "Titanic", "Avengers"],
         "correcta": 1},
        {"pregunta": "Un barco choca contra un iceberg:",
         "opciones": ["Frozen", "Avatar", "Titanic"],
         "correcta": 3},
        {"pregunta": "Un grupo de superhéroes se une para derrotar a Thanos:",
         "opciones": ["Batman", "Avengers Endgame", "Toy Story"],
         "correcta": 2},
        {"pregunta": "Un pez payaso busca a su hijo perdido en el océano:",
         "opciones": ["Buscando a Nemo", "Cars", "Ratatouille"],
         "correcta": 1},
        {"pregunta": "Un chef es en realidad una rata que cocina en París:",
         "opciones": ["Ratatouille", "Coco", "Intensamente"],
         "correcta": 1},
    ]
    for i in range(len(preguntas)):
        print(preguntas[i]["pregunta"])
        for j in range(len(preguntas[i]["opciones"])):
            print(f"{j+1} , {preguntas[i]["opciones"][j]}")
            
        respuestas = int(input("Ingresar la Respuesta: "))
        if respuestas == preguntas[i]["correcta"]:
            cont +=1
        else:
            cont_error +=1

    porc = (cont * 100) / (cont + cont_error)
    print(f"Los aciertos que tuviste fueron: {cont}")
    print(f"Los errores fueron: {cont_error}")
    print(f"El porcentaje de acierto es de: {porc}%")
peliculas()