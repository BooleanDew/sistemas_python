from mascota.mascota import Mascota
from datetime import datetime
import colorama;
from colorama import Fore as c_fore;#Para color de texto
from colorama import Style as c_style;#Para estilo del texto, pero solo lo usaremos para reiniciar el estilo de la consola.

#Importante: tienes que iniciarlo antes de usar.
colorama.init()
import os
if __name__ == "__main__":
    while(True):
        print(f"""
            Bienvenido a VetePet 1.0                 F1echa: [{datetime.now().date()}]
            
                1 - Mascotas
                3 - Salir
            """)
        opcion = int(input(c_fore.BLUE+"Ingrese una opcion del menu: "+c_style.RESET_ALL))
        if opcion == 1:
            
            print(c_fore.RED+"""
            ****** MASCOTAS ******
                1 - Nueva
                2 - Listar
                3 - Buscar
                4 - Eliminar
                5 - Actualizar
                6 - Descargar 
            """+c_style.RESET_ALL)
            opcion_mascota = int(input(c_fore.BLUE+"Ingrese opcion: "+c_style.RESET_ALL))
            if opcion_mascota == 1:
                print("Registrar:\n=============")
                nombre = input("Nombre: ")
                tipo = int(input("Tipo(1:Animal,2:Ave,3:Acuatico): "))
                edad = int(input("Edad: "))
                genero = int(input("Genero(1:Hembra, 2:Macho): "))
                mascota = Mascota(nombre,tipo,edad,genero)
                respuesta_mascota = mascota.agregarMascota()
                print(respuesta_mascota)
            elif opcion_mascota == 2:
                lista_mascota = Mascota().listarMascotas()
                print(lista_mascota)
            elif opcion_mascota == 3:
                print("Buscar Mascota\n")
                cod_mascota = int(input("Ingrese el codigo de la mascota: "))
                lista_mascota = Mascota().listarMascotas()
                
                for mascota in lista_mascota:
                    if(mascota["codigo"] == cod_mascota):
                        print("================")
                        print("Nombre: ",mascota["nombre"],"\nTipo: ",mascota["tipo"],"\nEdad: ",mascota["edad"],"\nGenero: ",mascota["genero"])
                        print("================\n")
            elif opcion_mascota == 4:
                print("Eliminar Mascota\n")
                cod_mascota = int(input("Ingrese el codigo de la mascota: "))
                respuesta = Mascota().eliminarMascota(cod_mascota)
                print(respuesta)
            elif opcion_mascota == 5:
                print("Actulizar Mascota\n")
                lista_mascota = Mascota().listarMascotas()
                print(lista_mascota)
                cod_mascota = int(input("Codigo de la mascota: "))
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                
                respuesta = Mascota().actualizarMascota(nombre,edad,cod_mascota)
                print(respuesta)
            elif opcion_mascota == 6:
                lista_mascota = Mascota().imprimirMascotas()
                with open("reporte.html","w") as listado:
                    li = ""
                    for dato in lista_mascota:
                       li += "<li>"+dato[2]+"</li>"
                    
                    listado.write("<html><head></head><body><ul>"+li+"</ul></body></html>")
                os.system("start reporte.html")
        elif opcion==3:
            break              