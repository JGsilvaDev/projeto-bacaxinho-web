import sqlite3
import random
import string
import hashlib
import base64

import funcoes as fc
import datetime


#script que gerencia usuários, adicionando lidando com eles

def criptografar(senha):
	# criar um objeto de hash SHA-256
	hash_obj = hashlib.md5()

	# atualizar o objeto de hash com a senha em bytes
	hash_obj.update(senha.encode('utf-8'))

	# obter o hash em bytes
	hash_bytes = hash_obj.digest()

	# converter o hash em bytes para uma string base64 com 20 caracteres
	hash_str = base64.b64encode(hash_bytes)[:20].decode('utf-8')

	return hash_str

#-----------------------------------------------------------------------


def criaUsuario(usuario,email,senha):

	#conectando o banco de dados
	conn = sqlite3.connect('bacaxinho.db')
	cursor = conn.cursor()

	tamanho = 5
	caracteres = string.ascii_letters + string.digits
	nomeTabela = ''.join(random.choice(caracteres) for i in range(tamanho))

	
	senha_criptografada = criptografar(senha)

	# Criando o usuario e inserindo no banco
	cursor.execute("INSERT INTO usuario(nome,email,senha,identificador)VALUES(?,?,?,?)",(usuario,email,senha_criptografada,nomeTabela))
	conn.commit()

	print(usuario+'registrado com sucesso!')

	# time.sleep(2)

	cursor.execute("SELECT id FROM usuario u WHERE u.identificador = '"+nomeTabela+"'")
	resultado = cursor.fetchall()
	id_usuario = resultado[0][0]

	# time.sleep(2)

	cursor.execute("INSERT INTO identificadores(identificador, id_usuario)VALUES(?,?)",(nomeTabela, id_usuario))
	conn.commit()

	# time.sleep(2)

	# Cria uma tabela "clientes"
	cursor.execute('''CREATE TABLE '''+nomeTabela+'''(
		id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
		id_usuario INTEGER NOT NULL,
		id_sentimento INTEGER NOT NULL,
		dt_insercao DATE NOT NULL,
		
		FOREIGN KEY (id_usuario) REFERENCES usuario(id),
		FOREIGN KEY (id_sentimento) REFERENCES sentimento(id)
	)''')


	#envia tudo e fecha a conexão
	cursor.execute("INSERT INTO "+nomeTabela +"(id_usuario,id_sentimento,dt_insercao)VALUES(?,?,?)", (id_usuario, 3, datetime.date.today().strftime("%d/%m/%Y")))
	conn.commit()



	conn.close()
	


#-----------------------------------------------------------------------

#essa função retorna a quantidade de usuários com esse nome e senha
def buscaUsuario(nome,senha):

	#conectando o banco de dados
	conn = sqlite3.connect('bacaxinho.db')
	cursor = conn.cursor()

	senhaHASH = criptografar(senha)
	cursor.execute("SELECT COUNT(id) FROM usuario u WHERE u.nome = '"+str(nome)+"' and u.senha = '"+str(senhaHASH)+"'")
	resultado = cursor.fetchall()
	busca = resultado[0][0]
	conn.close()

	return busca

def getUsuario(nome,senha):
	#conectando o banco de dados
	conn = sqlite3.connect('bacaxinho.db')
	cursor = conn.cursor()

	senhaHASH = criptografar(senha)
	cursor.execute("SELECT nome FROM usuario u WHERE u.nome = '"+str(nome)+"' and u.senha = '"+str(senhaHASH)+"'")
	resultado = cursor.fetchall()
	busca = resultado[0][0]
	conn.close()


	#retorno
	return busca

def getId(nome,senha):
	#conectando o banco de dados
	conn = sqlite3.connect('bacaxinho.db')
	cursor = conn.cursor()

	senhaHASH = criptografar(senha)

	cursor.execute("select id from usuario where nome='"+nome+"' and senha='"+senhaHASH+"'")

	resultado = cursor.fetchall()
	busca = resultado[0][0]
	conn.close()

	# print('identificador: '+str(busca))

	return busca

print('script de login importado com sucesso!')

