print("*******Festival musical Nuevas tecnologias*******")
print("Por favor escoger una de las opciones: ")
print("0. Salir")
print("1. Registrar bandas")
print("2. Ver lista de bandas")
print("3. editar hora de presentacion")
print("4. Retirar banda")

bandas=[]
opcion=6

while opcion!=0:
    banda={}
    opcion=int(input("Digite una de las opciones: "))
    if opcion == 1:
        banda["nombreBanda"]=input("Ingresar el nombre de la banda: ")
        banda["id"]=int(input("Digite el id de la banda: "))
        banda["genero"]=(input("Digitar el genero de la banda: "))
        banda["horaInicio"]=float(input("Hora en que se presenta la banda: "))
        banda["horaFin"]=float(input("Hora en que finaliza la presentacion: "))
        banda["pago"]=float(input("Ingresar el pago de la agrupacion: "))
        banda["estado"]=input("¿Ya se presento en el festival? Si o No: ")
        if banda["estado"]=="Si" or banda["estado"]== "si":
            banda["estado"]=True
        elif banda["estado"]=="No" or banda["estado"]== "no":
            banda["estado"]=False
        else:
            print("Error debe de ingredar un valor Si o No")
        bandas.append(banda)

    elif opcion == 2:
        for banda in bandas:
            print(banda)
    elif opcion == 3:
        idbuscar=int(input("Digitar el id de la banda a la que se le cambiara la hora: "))
        for banda in bandas:
            if banda["id"] == idbuscar:
                Diccionario = banda
                print(Diccionario)
                nuevaHoraInicio = float(input("Digitar la nueva hora de inicio: "))
                Diccionario["horaInicio"]=nuevaHoraInicio
                nuevaHoraFinal = float(input("Digitar la nueva hora del final de la presentación: "))
                Diccionario["horaFin"]=nuevaHoraFinal
                print(Diccionario)
    elif opcion == 4:
        idbuscar=int(input("Digitar el id de la banda que desea eliminar: "))
        for banda in bandas:
            if banda["id"]==idbuscar:
                bandaAEliminar = banda
                bandas.remove(bandaAEliminar)
                print(bandas)
            else:
                print("Error no digito el id de la banda")
    else:
        break
        
print("Fin del formulario")
                        