import sys
import os
menu = {1:{"opciones" :"agregar contacto"       ,"funcion":"agregar_contactos"},
        2:{"opciones" :"ver lista de contactos" ,"funcion":"ver_lista_contactos"},
        3:{"opciones" :"buscar contacto"        ,"funcion":"buscar_contactos"},
        4:{"opciones" :"editar contactos"       ,"funcion":"editar_contactos"},
        5:{"opciones" :"salir de la agenda"     ,"funcion":"salir"},
        }

class persona:
    def __init__(self,nombre,apellido,direccion,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+self.direccion+" "+self.telefono

class agenda:
    def __init__(self):
        self.agendas = list()

    def menu(self,OPCIONES):
        while True:
            print("Ingrese una de las siguientes opciones:")
            for key, value in OPCIONES.items():
                print("%s - %s" % (key, value["opciones"]))
            opcion = input("Ingrese una opcion:\n")
            if not (opcion.isdigit() and int(opcion) in OPCIONES.keys()):
                    print("Entrada incorrecta, ingrese un valor valido.")
                    opcion = self.menu(OPCIONES)
            return int(opcion)

    def agregar_contactos(self):
        print("ingrese el nombre")
        nombree = input()
        print("ingrese el apellido")
        apellidoo = input()
        print("ingrese la direccion")
        direccionn = input()
        print("ingrese el N° de telefono")
        celular = input()
        contacto = persona(nombre=nombree,apellido=apellidoo,direccion=direccionn,telefono=celular)
        self.agendas.append(contacto)
        return self.agendas

    def ver_lista_contactos(self):
        for y in self.agendas:
            print(y)
        print("ingrese enter para salir al menu")
        input()

    def buscar_contactos(self):
        nom = input("ingrese el contacto para buscar ")
        busqueda = dict() # en este diccionario se guardan toda las coincidencias con el id del contacto
        id = 0
        for y in self.agendas:
            id += 1
            #y.nombre="ariel"
            if (nom in y.nombre or nom in y.apellido) or (nom in y.direccion or nom in y.telefono):
                #la busqueda se hace atraves del nombre,apellido,direccion y n°telefono
                busqueda[id]=[y.nombre,y.apellido,y.direccion,y.telefono] #aca guarda un dict con el id del contacto y el nombre
        if len(busqueda) > 1:
            print("se a encontrado", len(busqueda),"coincidencias")
            cont = 1
            otrodict = dict()
            for ide2,nomb in busqueda.items():
                print(cont,nomb) #el ide2 es el id de la posicion en la que se encuentra el contacto
                otrodict[cont] = ide2
                cont += 1
            while True:
                print(cont,"para ingresar otra busqueda")
                cont += 1
                print(cont,"para salir al menu")
                print("para ver un contacto ingrese una opcion valida")
                opcion = input()
                if opcion.isdigit():
                    opcion = int(opcion)
                    if opcion >= 1 and opcion <= cont-2:
                        edit = otrodict[opcion] # en la variable "edit" tengo guardado el id del contacto que voy a editar
                        ide3 = 0
                        for a in self.agendas:
                            ide3 +=1
                            if edit == ide3:
                                print(a,"gggggggg")
                                return ide3# aca retornamos la lista de la class persona
                    elif opcion == cont-1:
                        print("buscar otro contacto")
                        cont = 1
                        self.buscar_contactos()
                    elif opcion == cont:
                        break
        elif len(busqueda) == 1:
            for clave in busqueda.keys():#aca esta el ide del contacto encontrado
                ide4 = 0
                for algo in self.agendas:
                    ide4 +=1
                    if clave == ide4:
                        print(algo)
                        return ide4
        elif len(busqueda) == 0:
            print("no se encontro resultados")
            print("1 para segir buscando")
            print("2 para salir al menu")
            opcion2 = input()
            if opcion2.isdigit():
                opcion2 =int(opcion2)
                if opcion2 == 1:
                    self.buscar_contactos()
                elif opcion2 == 2:
                    return None

    def editar_contactos(self):
        busqueda = self.buscar_contactos()
        if busqueda is None:
            return None #aca crear un metodo "menu" para que cuando aprete salir menu venga al menu y no que finalise el programa
        ide5 = 0
        for w in self.agendas:
            ide5 +=1
            if busqueda == ide5:
                while True :
                    print(" el contacto a editar es""\n",w)
                    print("1 para editar el nombre")
                    print("2 para editar el apellido")
                    print("3 para editar la direccion")
                    print("4 para editar el N° de telefono")
                    print("5 para salir al menu")
                    opcion = input()
                    if opcion.isdigit():
                        opcion = int(opcion)
                        if opcion == 1:
                            nombr = input("ingrese el nuevo nombre""\n")
                            w.nombre= nombr    #poner puntos de control para que el usuario decida que atrubutos modificar
                            print(w,"22222222")
                        elif opcion == 2:
                            apell = input("ingrese el nuevo apellido""\n")
                            w.apellido= apell
                        elif opcion == 3:
                            direcc = input("ingrese la nueva direccion""\n")
                            w.direccion= direcc
                        elif opcion == 4:
                            telef = input("ingrese el nuevo N° telefonico""\n")
                            w.telefono= telef
                        elif opcion == 5:
                            print("saliendo al menu")
                            break # aca crear un metodo menu

    def salir(self):
        print("Finalizando programa")
        sys.exit()

b = agenda()
while True:
    os.system('cls' if os.name=='nt' else 'clear')
    print("==================================")
    print("=              agenda            =")
    print("==================================")
    opcion = 0
    opcion = b.menu(menu)
    getattr( b,menu[opcion]["funcion"])()
