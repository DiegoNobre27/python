from connection.connection import Connection

class TableModel():
    def __init__(self, databaseType, stringConnection):
        self.databaseType = databaseType

        self.conn = Connection()
        self.connection = self.conn.connect(databaseType=databaseType, stringConnection=stringConnection)
        self.cursor = self.connection.cursor()
    
    def checkTable(self, tableName, databaseType):
        if databaseType == 'postgresql':
            query = f"select exists (select 1 from pg_tables where tablename = '{tableName}')"
        elif databaseType == 'sqlserver':
            ...
        
        self.cursor.execute(query)

        existTable = self.cursor.fetchone()[0]
        
        return existTable

    def createTable(self, tableName, dataList, existTable):
        if not existTable:
            query = f'create table {tableName}('

            for column, type in dataList:
                query += f'{column} {type},'
            
            query = query.rstrip(', ') + ');'
            
            self.cursor.execute(query)
            self.connection.commit()
    
    def setRegisterTable(self, tableName, columnsName, dataList):
        query = f'insert into {tableName} ('
        query += f', '.join(columnsName)
        query += ') values '
        
        for v in dataList:
            query += '(' + ', '.join(f"'{x}'" if isinstance(x, str)\
                                     else str(x) for x in v) + "), "
        
        query = query.rstrip(', ') + ';'
        
        self.cursor.execute(query)
        self.connection.commit()

    def getRegisterTable(self, tableName, databaseType, limit=None): 
        query = f'select * from {tableName}'
        
        if limit:
            if databaseType == 'postgresql':
                bound = f'limit {limit}'
                query = f'select * from {tableName} {bound}'
            elif databaseType == 'sqlserver':
                bound = f'top {limit}'
                query = f'select {bound} * from {tableName}'

        self.cursor.execute(query)
        values = self.cursor.fetchall()
        
        return values

    def updateRegisterTable(self, tableName, dataForUpdate, conditions): 
        if not dataForUpdate or not conditions:
            raise ValueError('Dados para atualizar e condições são necessários')
        
        updatePart = ', '.join([f"{column} = '{value}'" for column, value in dataForUpdate.items()])
        wherePart = ' and '.join([f"{column} = '{value}'" for column, value in conditions.items()])

        query = f'update {tableName} set {updatePart} where {wherePart}'

        print(query)

    def deleteRegisterTable(self): ...

    def disconnect(self):
        self.conn.disconnect(cursor=self.cursor, connection=self.connection)
        print('Conexão fechada')