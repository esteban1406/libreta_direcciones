from libreta import LibretaDirecciones

def menu():
    print("1. agregar contacto")
    print("2. Listar contactos")
    print("3. Eliminar contacto por correo electronico")
    print("4. Salir")

    
    opcion = input("seleccione una opcion")
    return opcion

def main():
    libreta = LibretaDirecciones("contactos.txt")

    while True:
        opcion = menu()
        if opcion == "1" :
            nombre = input("nombre")
            telefono = input("telefono")
            correo = input("correo")
            libreta.agregar_contacto(nombre,telefono,correo)
            print("contacto agregado")
        
        elif opcion == "2":
            print("**************LISTA DE CONTACTOS*************")
            libreta.listar_contactos()
        
        elif opcion == "3":
            print("**************eliminar por correo*************")
            correo_eliminar = input("ingrese el correo de contacto a eliminar")
            if any(contacto.correo == correo_eliminar for contacto in libreta.contactos):
                libreta.contactos = [contacto for contacto in libreta.contactos if contacto.correo != correo_eliminar]
                libreta.guardar_contactos()
                print("contacto eliminado")
            else:
                print(" no se encotro el correo")


        elif opcion == "4":
            break
        else:
            print("opcion invalida")


if __name__ =="__main__":
    main()

