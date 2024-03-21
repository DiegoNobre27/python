class TableController():
    def __init__(self, modelObject):
        self.modelObject = modelObject

    def checkTable(self, tableName):
        table = tableName.lower()
        
        try:
            existTable = self.modelObject.checkTable(tableName=table)

            if existTable:
                print('A tabela já existe')
                return existTable
            else:
                print('A tabela não existe na base')
        except Exception as e:
            print(e)

    def createTable(self, tableName, columnsName, columnsTypes, existTable):
        table = tableName.lower()
        if not existTable:
            try:
                self.modelObject.createTable(tableName=table, columnsName=columnsName, columnsTypes=columnsTypes, existTable=existTable)
                print('Tabela criada com sucesso')
            except Exception as e:
                print(e)

    def setRegisterTable(self, tableName, columnsName, dataTable):
        table = tableName.lower()

        try:
            self.modelObject.setRegisterTable(tableName=table, columnsName=columnsName, dataTable=dataTable)
            print('Dados inseridos com sucesso')
        except Exception as e:
            print(e)
    
    def getRegisterTable(self): ...
        
    def updateRegisterTable(self): ...

    def deleteRegisterTable(self): ...
        