from model.transformTextModel import TransformTextModel

import pyodbc
import psycopg2

class Connection():
    
    def defaultPortConnection(self, databaseType, port):
        databaseType = TransformTextModel.convertTextOrListLowerCase(textOrList=databaseType)
        
        if not port:
            door = '5432' if databaseType == 'postgresql' else '1433'
            return door
        else:
            return port

    def createStringConnection(self, databaseType, host, user, password, database, port=None):
        databaseType = TransformTextModel.convertTextOrListLowerCase(textOrList=databaseType)
        door = self.defaultPortConnection(databaseType=databaseType, port=port)

        con_str = f'postgresql://{user}:{password}@{host}:{door}/{database}' if databaseType == 'postgresql' \
            else f'DRIVER=SQL Server;SERVER={host},{door};DATABASE={database};ID={user};PWD={password};'
        
        return con_str
    
    def connect(self, databaseType, stringConnection):
        databaseType = TransformTextModel.convertTextOrListLowerCase(textOrList=databaseType)

        if databaseType == 'sqlserver':
            try:
                connection = pyodbc.connect(stringConnection)
                print('Conexão aberta')

                return connection
            except Exception as e:
                print(e)
        elif databaseType == 'postgresql':
            try:
                connection = psycopg2.connect(stringConnection)
                print('Conexão aberta')

                return connection
            except Exception as e:
                print(e)

    def disconnect(self, cursor, connection):
        cursor.close()
        connection.close()
