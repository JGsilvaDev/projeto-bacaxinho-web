from flask import Flask, render_template, request, redirect, jsonify, url_for

from py_scripts import userManager as uman

import funcoes as fc #funções do bacaxinho


retorno = ""

app = Flask(__name__, static_url_path='/static')


#region rotas para páginas
#-----------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

#-----------------------------------------------

@app.route('/login')
def login():
    return render_template('login.html')

#-----------------------------------------------

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

#-----------------------------------------------

#endregion

#region rotas de form

#form de comunicação
@app.route('/atualizar_dados', methods=['POST'])
def atualizar_dados():
    global retorno
    input = request.form['usermsg']
    retorno = fc.analisar_input(input)
    print("")
    print("bot: "+retorno)

    return jsonify({'status': 'OK'})

#-----------------------------------------------
@app.route('/obter_dados', methods=['GET'])
def obter_dados():
    
    dados = {'retorno': retorno}
    return jsonify(dados)

#-----------------------------------------------
#form de registro de usuário
@app.route('/post_registro', methods=['POST'])
def post_registro():

    username = request.form['username']
    email    =    request.form['email']
    password = request.form['password']


    uman.criaUsuario(username,email,password)

    return jsonify ({'status':'OK'})


#-----------------------------------------------

@app.route('/post_login', methods=['POST'])
def post_login():

    username = request.form['username']
    password = request.form['password']

    return redirect(url_for('get_login', usr = username, pwd=password))

@app.route('/get_login', methods=['GET'])
def get_login():
    username = request.args.get('usr')
    password = request.args.get('pwd')

    userfound = uman.buscaUsuario(str(username),str(password))

    print(userfound)

    return jsonify({'userfound':userfound})

#-----------------------------------------------
#endregion

if __name__ == '__main__':
    app.run(host='localhost')
