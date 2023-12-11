import os
import glob
import csv

class Arquivo():
    # directory = pasta raiz do projeto
    # fileType = extensão do arquivo
    # fileName = nome do arquivo

    def __init__(self, directory, fileType=None, fileName=None):
        self.fileType = fileType
        self.fileName = fileName
        self.directoryFiles = directory
        self.strFile = []
        self.listFiles = []
        self.listLineFile = []

    def getDirectory(self):
        # pega o diretorio raiz e adiciona a pasta onde se encontra os arquivos
        self.directoryFiles = os.path.join(self.directoryFiles, 'file\\')

    def createFilterFile(self):
        # cria a string que o glob buscará na pasta
        if self.fileType:
            fileType_lower = self.fileType.lower()
        else:
            fileType_lower = ""

        if self.fileName:
            fileName_lower = self.fileName.lower()
        else:
            fileName_lower = ""

        if self.fileName and self.fileType:
            self.strFile = f'{fileName_lower}.{fileType_lower}'
        elif self.fileName and not self.fileType:
            self.strFile = f'{fileName_lower}*.*'
        elif not self.fileName and self.fileType:
            self.strFile = f'*.{fileType_lower}'

    def getNameFiles(self):
        # pega o nome dos arquivos de acordo com o filtro
        self.getDirectory()
        self.createFilterFile()

        directoryFiles = os.path.join(self.directoryFiles, self.strFile)
        listNamesFiles = glob.glob(directoryFiles)

        self.listFiles = [os.path.basename(file) for file in listNamesFiles]
    
    def readFiles(self):
        self.getNameFiles()

        #sizeListFiles = len(self.listFiles)
        listLine = []

        for fileName in self.listFiles:
            filePath = os.path.join(self.directoryFiles, fileName)

            # lê os arquivos
            with open(filePath, 'r') as archive:
                archiveReader = csv.reader(archive)

                # adiciona todas as linhas do arquivo à lista
                listLine.extend(list(archiveReader))
        
        # copia o cabeçalho
        header = listLine[0]

        for line in listLine:
            if header in listLine:
                indice = listLine.index(header)
                listLine.pop(indice)
        
        # adiciona o cabeçalho e as linhas dos arquivos       
        self.listLineFile.append(header)
        self.listLineFile.append(listLine)

        return self.listLineFile
    