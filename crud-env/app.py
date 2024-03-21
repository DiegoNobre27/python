from connection.connection import Connection

from controller.tableController import TableController
from controller.fileController import FileController

from model.tableModel import TableModel
from model.fileModel import FileModel

#from flask import Flask, render_template, request, redirect, url_for

#app = Flask(__name__)

# ARQUIVO
diretorio = 'C:\\Users\\D003238\\Documents\\diegoNobreD003238\\arquivos\\csv\\modeloDeRisco'
nomeArquivo = None
tipoArquivo = 'csv'

# CONEXÃO
tipoSGBD = 'postgresql'
host = 'localhost'
usuario = 'postgres'
senha = 'postgres'
bancoDeDados = 'teste'
porta = '5433'

# TABELA
tabela = 'teste_Modelo_Risco'
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
tipoDasColunas = arquivo[1]
dados = arquivo[2]

controle = TableController(modelObject=modelo)
existeTabela = controle.checkTable(tableName=tabela)

controle.createTable(tableName=tabela, columnsName=colunas, columnsTypes=tipoDasColunas, existTable=existeTabela)
controle.setRegisterTable(tableName=tabela, columnsName=colunas, dataTable=dados)

modelo.disconnect()