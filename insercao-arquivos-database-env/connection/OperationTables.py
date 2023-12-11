from connection.Conexao import DataBaseConnector

class OperationTables():
    def __init__(self, dataBaseType, host, user, password, database):
        self.dataBaseType = dataBaseType
        self.database = database
        self.existTable = None
        
        self.conn = DataBaseConnector(dataBaseType, host, user, password, database)
        self.connection = self.conn.connect()
        self.cursor = self.conn.createCursor()

    def checkTable(self, nameTable):
        self.dataBaseType = self.dataBaseType.lower()
        
        if self.dataBaseType == 'postgresql':
            query = f"select exists (select 1 from pg_tables where tablename = '{nameTable}')"
            
        elif self.dataBaseType == 'mysql':
            ...
        elif self.dataBaseType == 'sqlserver':
            ...
        
        self.cursor.execute(query)

        self.existTable = self.cursor.fetchone()[0]
        
        return self.existTable
    
    def createTable(self, nameTable, columnsName, columnsTypes, existTable):
        try:
            if not existTable:
                dataColumns = list(zip(columnsName, columnsTypes))
                query = f'create table {nameTable}('

                for column, type in dataColumns:
                    query += f'{column} {type}, '
                
                query = query.rstrip(', ') + ');'

                self.cursor.execute(query)
                self.connection.commit()

                self.existTable = True

                print('Tabela criada com sucesso')
        except Exception as e:
            print('Não foi possível executar essa ação ou a tabela já existe na base de dados.')
            print(f'Error: {e}')
    
    def insertDataTables(self, table, dataTable, columnNames, existTable):
        try:
            if not existTable:
                query = f'insert into {table} ('

                query += f', '.join(columnNames)
                query += ') values '

                for v in dataTable:
                    query += '(' + ', '.join(f"'{x}'" if isinstance(x, str) else str(x) for x in v) + "), "
                
                query = query.rstrip(', ') + ';'
            
                self.cursor.execute(query)
                self.connection.commit()

                print('Registros inseridos na tabela')
        except Exception as e:
            print('Não foi possível inserir os dados na tabela')
            print(f'Error: {e}')

    def updateDataTables(self):
        ...

    def deleteDataTables(self):
        ...