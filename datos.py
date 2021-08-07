def datos():
    print("esto sera la base de datos")
    mis_datos = open("datos.txt","a")
    nombre = input("ingrese su nombre ")
    mis_datos.write(nombre)
    mis_datos = open("datos.txt","r")
    print(mis_datos.readlines())
    print("bienvenido")
datos()
