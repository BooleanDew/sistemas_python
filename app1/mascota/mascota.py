from conexion.conexion import Conexion
from tabulate import tabulate
import colorama;
from colorama import Fore as c_fore;#Para color de texto
from colorama import Style as c_style;#Para estilo del texto, pero solo lo usaremos para reiniciar el estilo de la consola.

#Importante: tienes que iniciarlo antes de usar.
colorama.init();
class Mascota:
    conexion = Conexion().getConexion()
    cursor = conexion.cursor()
    def __init__(self,codigo=0,nombre="",tipo=0,edad=0,genero=0):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__tipo = tipo
        self.__edad = edad
        self.__genero = genero
    
    def agregarMascota(self):
        try:
            sql = "INSERT INTO mascota(nombre_mascota,tipo_mascota,edad_mascota,genero_mascota) VALUES(%s,%s,%s,%s,%s)"
            self.cursor.execute(sql,(self.__codigo,self.__nombre,self.__tipo,self.__edad,self.__genero,))
            self.conexion.commit()
            return "Mascota registrada con exito."                   
        except Exception as e:
            return f"error: {e}"
        finally:
            self.conexion.close() 
    def  listarMascotas(self):
        try:
            tipo_mascota = ""
            headers  = [c_fore.CYAN+"CODIGO","NOMBRE","TIPO","EDAD","GENERO"+c_style.RESET_ALL]
            lista_datos = []
            sql = "SELECT * FROM mascota"
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            for dato in datos:#Tipo(1:Animal,2:Ave,3:Acuatico
                if dato[3] == 1:
                    tipo_mascota = "Animal"
                if dato[3] == 2:
                    tipo_mascota = "Ave"
                if dato[3] == 3:
                     tipo_mascota = "Acuatico"
                if dato[5] == 1:
                    genero_mascota = "Hembra"
                if dato[5] == 2:
                    genero_mascota = "Macho"
                lista_datos.append([c_fore.GREEN+str(dato[1]),dato[2],tipo_mascota,dato[4],genero_mascota+c_style.RESET_ALL])
            return tabulate(lista_datos, headers, tablefmt="grid")
        except Exception as e:
            return f"error: {e}"
        finally:
            self.conexion.close()
            
    def eliminarMascota(self,codigo):
        try:
            sql = "DELETE FROM mascota WHERE cod_mascota = %s"
            self.cursor.execute(sql,(codigo,))
            self.conexion.commit()
            return "Registro eliminado con exito."
        except Exception as e:
            return f"No fue posible eliminar la mascota.{e}"
        finally:
            self.conexion.close()
    def actualizarMascota(self,nombre,edad,codigo):
        try:
            sql = "UPDATE mascota SET nombre_mascota=%s, edad_mascota=%s WHERE cod_mascota = %s"
            self.cursor.execute(sql,(nombre,edad,codigo))
            self.conexion.commit()
            return "Registro actualizado con exito."
        except Exception as e:
            return f"No fue posible actulizar la mascota.{e}"
        finally:
            self.conexion.close()
    def  imprimirMascotas(self):
        try:
            lista_datos = []
            sql = "SELECT * FROM mascota"
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            for dato in datos:#Tipo(1:Animal,2:Ave,3:Acuatico
                if dato[3] == 1:
                    tipo_mascota = "Animal"
                if dato[3] == 2:
                    tipo_mascota = "Ave"
                if dato[3] == 3:
                     tipo_mascota = "Acuatico"
                if dato[5] == 1:
                    genero_mascota = "Hembra"
                if dato[5] == 2:
                    genero_mascota = "Macho"
                lista_datos.append([str(dato[1]),dato[2],tipo_mascota,dato[4],genero_mascota])
            return lista_datos
        except Exception as e:
            return f"error: {e}"
        finally:
            self.conexion.close()
            
    