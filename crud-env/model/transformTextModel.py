class TransformTextModel():
    def valueLowerCase(value):
        if not value:
            value = ""
            return value

        return value.lower()
    
    def emptyText(datasLine):
        for i in range(len(datasLine)):
            for j in range(len(datasLine[i])):
                if datasLine[i][j] == '':
                    datasLine[i][j] = 0

        return datasLine