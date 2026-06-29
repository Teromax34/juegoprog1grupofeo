def campo():
    puntos = 0

    print("prguntas de producción agropecuaria ")

    print("Situación 1: Manejo del suelo en sistema agrícola.")
    opcion = input("¿Qué práctica se utiliza para conservar humedad y reducir erosión?\n1- Labranza convencional\n2- Siembra directa\n3- Quema de rastrojos\n")

    if opcion == "2":
        print("Correcto")
        puntos += 10
    else:
        print("Incorrecto")

    print("\nSituación 2: Fertilidad del suelo.")
    opcion = input("¿Qué elemento es esencial para el crecimiento vegetativo de los cultivos?\n1- Nitrógeno\n2- Sodio\n3- Silicio\n")

    if opcion == "1":
        print("Correcto")
        puntos += 10
    else:
        print("Incorrecto")

    print("\nSituación 3: Producción ganadera.")
    opcion = input("¿Qué se entiende por carga animal?\n1- Cantidad de alimento en el potrero\n2- Número de animales por hectárea\n3- Peso total del ganado vendido\n")

    if opcion == "2":
        print("Correcto")
        puntos += 10
    else:
        print("Incorrecto")

    print("\nSituación 4: Manejo de pasturas.")
    opcion = input("¿Qué sistema permite mejor recuperación del pasto?\n1- Pastoreo continuo\n2- Pastoreo rotativo\n3- Sobrepastoreo permanente\n")

    if opcion == "2":
        print("Correcto")
        puntos += 10
    else:
        print("Incorrecto")

    print("\nSituación 5: Suelos agrícolas.")
    opcion = input("¿Qué proceso implica pérdida de nutrientes por infiltración profunda?\n1- Lixiviación\n2- Compactación\n3- Erosión hídrica superficial\n")

    if opcion == "1":
        print("Correcto")
        puntos += 10
    else:
        print("Incorrecto")

    print("\nSituación 6: Fertilización.")
    opcion = input("¿Qué fertilizante aporta principalmente nitrógeno?\n1- Urea\n2- Superfosfato triple\n3- Cloruro de potasio\n")

    if opcion == "1":
        print("Correcto")
        puntos += 10
    else:
        print("Incorrecto")

    print("\nSituación 7: Agricultura.")
    opcion = input("¿Qué cultivo es típico de invierno en la región pampeana?\n1- Soja\n2- Trigo\n3- Maíz tardío\n")

    if opcion == "2":
        print("Correcto")
        puntos += 10
    else:
        print("Incorrecto")

    print("\nSituación 8: Sanidad vegetal.")
    opcion = input("¿Qué práctica ayuda a prevenir plagas y enfermedades?\n1- Monocultivo\n2- Rotación de cultivos\n3- Exceso de riego\n")

    if opcion == "2":
        print("Correcto")
        puntos += 10
    else:
        print("Incorrecto")

    print("\nResultado final")
    print(f"Puntos: {puntos}/80")
    return int(puntos)