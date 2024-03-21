import os
import glob
import csv
from model.transformTextModel import TransformTextModel

class FileModel():
    def __init__(self):
        self.listFiles = []

    def createFilterFile(self, fileName=None, fileType=None):
        fileName_lower = TransformTextModel.valueLowerCase(value=fileName)
        fileType_lower = TransformTextModel.valueLowerCase(value=fileType)

        if fileName and fileType:
            strFile = f'{fileName_lower}.{fileType_lower}'
        elif fileName and not fileType:
            strFile = f'{fileName_lower}*.*'
        elif not fileName and fileType:
            strFile = f'*.{fileType_lower}'
        elif not fileName and not fileType:
            strFile = f'*.*'
        
        return strFile
    
    def getNameFile(self, directory, fileName=None, fileType=None):
        strFile = self.createFilterFile(fileName, fileType)

        directoryFiles = os.path.join(directory, strFile)
        listNameFile = glob.glob(directoryFiles)

        self.listFiles = [os.path.basename(file) for file in listNameFile]
    
    def dropLine(self, datas, listToDelete):
        for i in datas:
            if listToDelete in datas:
                idx = datas.index(listToDelete)
                datas.pop(idx)
        return datas
    
    def readArchive(self, directory, fileName=None, fileType=None):
        datas = []
        lines = []
        
        self.getNameFile(directory, fileName, fileType)
        
        for archiveName in self.listFiles:
            filePath = os.path.join(directory, archiveName)

            with open(filePath, 'r') as archive:
                archiveReader = csv.reader(archive)
                datas.extend(list(archiveReader))
        
        header = datas[0]
        types = datas[1]
        dataFile = self.dropLine(datas=datas, listToDelete=header)
        dataFile = self.dropLine(datas=datas, listToDelete=types)

        lines.append(header)
        lines.append(types)
        lines.append(dataFile)

        return lines