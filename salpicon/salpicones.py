print("**Salpicon**")
print("************")
print(".0 Salir")
print("1. Registrar frutas")
print("2. Costo total del salpicon")
print("3. Mostrar frutas por precio de mayor a menor")
print("4. Mostrar cual es la fruta más cara y la más barata")
print("************")

opcion=90
salpicon=[]

while opcion !=0 :
    opcion=int(input("Digitar una opcion: "))
    if opcion == 1 :
        cantidad=int(input("Ingrese la cantidad de frutas: "))
        for fruta in range(cantidad):
            frutas={}
            frutas["nombre"]=input("Ingresar el nombre de la fruta: ")
            frutas["id"]=int(input("Ingrese el id de la fruta: "))
            frutas["precio"]=int(input("Digitar el precio de la fruta: "))
            frutas["cantidad"]=int(input("Ingresar la cantidad de frutas deseadas: "))
            salpicon.append(frutas)
        print(salpicon)   

    elif opcion == 2 :
        precioSalpicon=0
        for fruta in salpicon:
            precioFruta=(fruta["cantidad"]*fruta["precio"])
            precioSalpicon += precioFruta
        print(f'El precio del salpicon es: {precioSalpicon}')
    
    elif opcion == 3 :
        ordenar=sorted(salpicon,key=lambda x: x["precio"], reverse=True)
        print(ordenar)
        for fruta in ordenar:
            print(f'Nombre: {fruta["nombre"]} su precio es: {fruta["precio"]}')
    
    elif opcion == 4:
        maximo = max(salpicon, key=lambda x: x["precio"])
        minimo = min(salpicon, key=lambda X: X["precio"])
        print(f'la fruta mas cara es: {maximo["nombre"]} y la mas barata es: {minimo["nombre"]}')
        
print("fin del programa.")



