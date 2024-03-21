class FileController():
    def __init__(self, modelObject):
        self.modelObject = modelObject
    
    def readFile(self, directory, fileName=None, fileType=None):
        print('Lendo arquivo')
        
        try:
            datas = self.modelObject.readArchive(directory=directory, fileName=fileName, fileType=fileType)
            print('Arquivo lido com sucesso')
            
            return datas
        except Exception as e:
            print(e)
            