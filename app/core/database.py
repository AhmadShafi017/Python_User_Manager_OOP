import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME")
        )

    def execute(self,query,params=None):
        cursor = self.connection.cursor()
        cursor.execute(query,params)
        self.connection.commit()
        return cursor
    
    def executemany(self,query,values):
        cursor = self.connection.cursor()
        cursor.executemany(query,values)
        self.connection.commit()
    
    def close(self):
        self.connection.close()