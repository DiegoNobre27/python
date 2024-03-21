from connection.connection import Connection

from controller.tableController import TableController
from controller.fileController import FileController

from model.tableModel import TableModel
from model.fileModel import FileModel

from urllib.parse import quote

#from flask import Flask, render_template, request, redirect, url_for

#app = Flask(__name__)

# ARQUIVO
diretorio = '/media/diego/Arquivos/arquivos/csv'
nomeArquivo = 'movies'
tipoArquivo = 'csv'

# CONEXÃO
tipoSGBD = 'postgresql'
host = 'localhost'
usuario = 'postgres'
senha = quote('D@ni3l2oo8', safe='')
bancoDeDados = 'testes'
porta = '5433'

# TABELA
tabela = 'filmes'
colunas = []
dados = []
tipoDasColunas = []

arquivoModelo = FileModel()
arquivoController = FileController(arquivoModelo)
conexao = Connection()

conexaoString = conexao.createStringConnection(databaseType=tipoSGBD, host=host, user=usuario, password=senha, database=bancoDeDados, port=porta)
modelo = TableModel(databaseType=tipoSGBD, stringConnection=conexaoString)

#@app.route('/')
#def index():
#    ...

arquivo = arquivoController.readFile(directory=diretorio, fileName=nomeArquivo, fileType=tipoArquivo)

colunas = arquivo[0]
print(colunas)
tipoDasColunas = arquivo[1]
dados = arquivo[2]

controle = TableController(modelObject=modelo)
existeTabela = controle.checkTable(tableName=tabela, databaseType=tipoSGBD)

#controle.createTable(tableName=tabela, columnsName=colunas, columnsTypes=tipoDasColunas, existTable=existeTabela)
#controle.setRegisterTable(tableName=tabela, columnsName=colunas, dataList=dados)

dadosRetornados = controle.getRegisterTable(tableName=tabela, databaseType=tipoSGBD, limit=5)
print(dadosRetornados)

atualizarDados = {"genre":"Filmes pra chorar"}
condicao = {"genre": "Romance"}

dadosAtualizados = controle.updateRegisterTable(tableName=tabela, dataForUpdate=atualizarDados, conditions=condicao)
print(dadosAtualizados)

dadosRetornados = controle.getRegisterTable(tableName=tabela, databaseType=tipoSGBD, limit=5)
print(dadosRetornados)

modelo.disconnect()