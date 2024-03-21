from connection.connection import Connection
from model.transformTextModel import TransformTextModel

class TableModel():
    def __init__(self, databaseType, stringConnection):
        self.databaseType = databaseType

        self.conn = Connection()
        self.connection = self.conn.connect(databaseType=databaseType, stringConnection=stringConnection)
        self.cursor = self.connection.cursor()
    
    def checkTable(self, tableName):
        databaseType = TransformTextModel.valueLowerCase(self.databaseType)

        if databaseType == 'postgresql':
            query = f"select exists (select 1 from pg_tables where tablename = '{tableName}')"
        elif databaseType == 'sqlserver':
            ...
        
        self.cursor.execute(query)

        existTable = self.cursor.fetchone()[0]
        
        return existTable

    def createTable(self, tableName, columnsName, columnsTypes, existTable):
        if not existTable:
            dataColumns = list(zip(columnsName, columnsTypes))
            query = f'create table {tableName}('

            for column, type in dataColumns:
                query += f'{column} {type},'
            
            query = query.rstrip(', ') + ');'
            
            self.cursor.execute(query)
            self.connection.commit()
    
    def setRegisterTable(self, tableName, columnsName, dataTable):
        query = f'insert into {tableName} ('
        query += f', '.join(columnsName)
        query += ') values '

        datas = TransformTextModel.emptyText(dataTable)
        
        for v in datas:
            query += '(' + ', '.join(f"'{x}'" if isinstance(x, str) else str(x) for x in v) + "), "
        
        query = query.rstrip(', ') + ';'
        
        self.cursor.execute(query)
        self.connection.commit()

    def getRegisterTable(self): ...

    def updateRegisterTable(self): ...

    def deleteRegisterTable(self): ...

    def disconnect(self):
        self.conn.disconnect(cursor=self.cursor, connection=self.connection)
        print('Conexão fechada')