from model.transformTextModel import TransformTextModel

import pyodbc
import psycopg2

class Connection():
    
    def checkPortDefault(self, databaseType, port):
        databaseType = TransformTextModel.valueLowerCase(databaseType)

        if not port and databaseType == 'postgresql':
            door = '5432'
        elif not port and databaseType == 'sqlserver':
            door = '1433'
        
        return door

    def createStringConnection(self, databaseType, host, user, password, database, port=None):
        databaseType = TransformTextModel.valueLowerCase(value=databaseType)
        door = self.checkPortDefault(databaseType=databaseType, port=port)
        
        if databaseType == 'sqlserver':
            con_str = f'DRIVER=SQL Server;SERVER={host},{door};DATABASE={database};ID={user};PWD={password};'
        elif databaseType == 'postgresql':
            con_str = f'postgresql://{user}:{password}@{host}:{door}/{database}'
        
        return con_str
    
    def connect(self, databaseType, stringConnection):
        databaseType = TransformTextModel.valueLowerCase(value=databaseType)
        
        if databaseType == 'sqlserver':
            try:
                connection = pyodbc.connect(stringConnection)
                print('Conexão aberta')
            except Exception as e:
                print(e)
        elif databaseType == 'postgresql':
            try:
                connection = psycopg2.connect(stringConnection)
                print('Conexão aberta')
            except Exception as e:
                print(e)
        
        return connection

    def disconnect(self, cursor, connection):
        cursor.close()
        connection.close()
