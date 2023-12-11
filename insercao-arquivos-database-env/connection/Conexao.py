import pyodbc
import mysql.connector
import psycopg

class DataBaseConnector():
    def __init__(self, dataBaseType, host, user, password, database):
        self.dataBaseType = dataBaseType
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        if self.dataBaseType == 'sqlserver':
            con_str = f'DRIVER=SQL Server;SERVER={self.host};DATABASE={self.database};UID{self.user};PWD={self.password};'
            
            try:
                self.connection = pyodbc.connect(con_str)

                print(f'Conexão criada com sucesso, ao {self.dataBaseType}')
            except Exception as e:
                print('Erro ao tentar se conectar')
                print(f'Error: {e}')
        elif self.dataBaseType == 'mysql':
            try:
                self.connection = mysql.connector.connect(user=self.user, password=self.password, host=self.host+"", database=self.database)
                
                print(f'Conexão criada com sucesso, ao {self.dataBaseType}')
            except Exception as e:
                print('Erro ao tentar se conectar')
                print(f'Error: {e}')
        elif self.dataBaseType == 'postgresql':
            try:
                str_connection = f"postgresql://{self.user}:{self.password}@{self.host}:5433/{self.database}"
                self.connection = psycopg.connect(str_connection)

                print(f'Conexão criada com sucesso, ao {self.dataBaseType}')
            except Exception as e:
                print('Erro ao tentar se conectar')
                print(f'Error: {e}')

        return self.connection

    def createCursor(self):
        if self.connection:
            self.cursor = self.connection.cursor()

            print('Cursor criado com sucesso')
            
            return self.cursor

    def desconect(self):
        self.cursor.close()
        self.connection.close()
        print('Conexão encerrada com sucesso')