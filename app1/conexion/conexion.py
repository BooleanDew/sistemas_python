import mysql.connector

class Conexion:
    
    def getConexion(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="veterinaria"
        )
        
        return db