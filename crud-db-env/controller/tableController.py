from model.transformTextModel import TransformTextModel

class TableController():
    def __init__(self, modelObject):
        self.modelObject = modelObject

    def checkTable(self, tableName, databaseType):
        newTableName = TransformTextModel.convertTextOrListLowerCase(textOrList=tableName)
        newDatabaseType = TransformTextModel.convertTextOrListLowerCase(textOrList=databaseType)

        try:
            existTable = self.modelObject.checkTable(tableName=newTableName, databaseType=newDatabaseType)

            if existTable:
                print('A tabela já existe')
                return existTable
            else:
                print('A tabela não existe na base')
        except Exception as e:
            print(e)

    def createTable(self, tableName, columnsName, columnsTypes, existTable):
        newTableName = TransformTextModel.convertTextOrListLowerCase(textOrList=tableName)

        newColumnsName = TransformTextModel.replaceWords(expression=columnsName, symbol=' ', text='_')
        newColumnsName = TransformTextModel.replaceWords(expression=newColumnsName, symbol='%', text='percent')
        newColumnsName = TransformTextModel.convertTextOrListLowerCase(textOrList=newColumnsName)

        newcolumnsTypes = TransformTextModel.convertTextOrListLowerCase(textOrList=columnsTypes)
        
        dataList = list(zip(newColumnsName, newcolumnsTypes))

        if not existTable:
            try:
                self.modelObject.createTable(tableName=newTableName, dataList=dataList, existTable=existTable)
                print('Tabela criada com sucesso')
            except Exception as e:
                print(e)

    def setRegisterTable(self, tableName, columnsName, dataList):
        newTableName = TransformTextModel.convertTextOrListLowerCase(textOrList=tableName)
        
        newColumnsName = TransformTextModel.replaceWords(expression=columnsName, symbol=' ', text='_')
        newColumnsName = TransformTextModel.replaceWords(expression=newColumnsName, symbol='%', text='percent')
        newColumnsName = TransformTextModel.convertTextOrListLowerCase(textOrList=newColumnsName)
        
        newDataList = TransformTextModel.emptyText(dataList)
        newDataList = TransformTextModel.replaceWordInList(wordList=newDataList, symbol="$", text='')
        newDataList = TransformTextModel.replaceWordInList(wordList=newDataList, symbol="'", text='')

        try:
            self.modelObject.setRegisterTable(tableName=newTableName, columnsName=newColumnsName, dataList=newDataList)
            print('Dados inseridos com sucesso')
        except Exception as e:
            print(e)
    
    def getRegisterTable(self, tableName, databaseType, limit=None): 
        newTableName = TransformTextModel.convertTextOrListLowerCase(textOrList=tableName)
        newDatabaseType = TransformTextModel.convertTextOrListLowerCase(textOrList=databaseType)
        newLimit = limit

        try:
            datas = self.modelObject.getRegisterTable(tableName=newTableName, databaseType=newDatabaseType, limit=newLimit)

            newData = [list(tupla) for tupla in datas]

            return newData
        except Exception as e:
            print(e)
        
    def updateRegisterTable(self, tableName, dataForUpdate, conditions):
        newTableName = TransformTextModel.convertTextOrListLowerCase(textOrList=tableName)

        try:
            #update = 
            self.modelObject.updateRegisterTable(tableName=newTableName, dataForUpdate=dataForUpdate, conditions=conditions)
            #return update
        except Exception as e:
            print(e)

    def deleteRegisterTable(self): ...
        