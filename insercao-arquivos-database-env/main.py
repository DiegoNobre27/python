from controller.Arquivos import Arquivo
from connection import OperationTables as ot

import os

if __name__ == '__main__':
    arquivos = Arquivo(fileName='endereco', fileType='csv', directory=f'{os.path.dirname(__file__)}')
    dados = arquivos.readFiles()
    colunas = dados[0]
    dados = dados[1]
    tabela = 'Endereco'#'Pessoa'
    tipos = ['varchar(100)','varchar(10)','varchar(100)','varchar(15)','varchar(100)','varchar(100)','char(2)',]#['varchar(100)', 'varchar(100)', 'int', 'char(1)']

    
    conn = ot.OperationTables(dataBaseType='postgresql', user='postgres', password='postgres', host='localhost', database='teste')
    existTable = conn.checkTable(nameTable=tabela)
    conn.createTable(nameTable = tabela, columnsName = colunas, columnsTypes = tipos, existTable=existTable)
    conn.insertDataTables(table = tabela, dataTable = dados, columnNames = colunas, existTable=existTable)