class TransformTextModel():
    def convertTextOrListLowerCase(textOrList):
        if isinstance(textOrList, str):
            return textOrList.lower()
        elif isinstance(textOrList, list):
            return [item.lower() for item in textOrList]
        else:
            return None
    
    def emptyText(datasLine):
        for i in range(len(datasLine)):
            for j in range(len(datasLine[i])):
                if datasLine[i][j] == '':
                    datasLine[i][j] = 0

        return datasLine
    
    def replaceWords(expression, symbol, text):
        newExpression = [word.replace(symbol, text) for word in expression]
        return newExpression
    
    def replaceWordInList(wordList, symbol, text):
        new_wordLists = [[word.replace(symbol, text, 1) for word in innerList]\
                            for innerList in wordList]
        return new_wordLists