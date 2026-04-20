import mysql.connector
import json
from models.salle import Salle

class DataSalle:

    def get_connection(self):
        with open("Data/config.json") as f:
            config = json.load(f)

        return mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO salle VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (salle.code, salle.libelle, salle.type, salle.capacite))

        conn.commit()
        conn.close()

    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = """UPDATE salle 
                   SET libelle=%s, type=%s, capacite=%s 
                   WHERE code=%s"""
        cursor.execute(query, (salle.libelle, salle.type, salle.capacite, salle.code))

        conn.commit()
        conn.close()


    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM salle WHERE code=%s", (code,))
        conn.commit()
        conn.close()

    def get_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM salle WHERE code=%s", (code,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return Salle(*result)
        return None

