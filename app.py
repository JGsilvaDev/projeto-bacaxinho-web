from flask import Flask, render_template, request, redirect, jsonify, url_for, make_response

from py_scripts import userManager as uman
from py_scripts import emissorSerial as es

import funcoes as fc #funções do bacaxinho

retorno = None
voiceChat = None
emocao = 'neturo'

app = Flask(__name__, static_url_path='/static')

@app.before_request
def delete_cookies():
    response = make_response()
    response.delete_cookie('username')


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
    global retorno, emocao
    input = request.form['usermsg']

    retorno = fc.analisar_input(input)

    emocao = fc.analisarFrase(input,fc.identificador_usuario)

    print('o usuario disse: '+input+' e o bot entendeu como: '+emocao)

    es.enviarSerial(emocao)

    return jsonify({'status': 'OK'})

#-----------------------------------------------
@app.route('/obter_dados', methods=['GET'])
def obter_dados():


    dados = {'retorno': retorno, 'emocao_usuario':emocao, 'voice':voiceChat}
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

    if uman.buscaUsuario(str(username),str(password)) == 1:
        fc.identificador_usuario = uman.getId(username,password)

    print(fc.identificador_usuario)


    return redirect(url_for('get_login', usr = username, pwd=password))

@app.route('/get_login', methods=['GET'])
def get_login():
    username = request.args.get('usr')
    password = request.args.get('pwd')

    userfound = uman.buscaUsuario(str(username),str(password))

    print(userfound)

    return jsonify({'userfound':userfound})

#-----------------------------------------------

@app.route('/get-voice', methods=['POST'])
def get_voice():
    global retorno, emocao, voiceChat

    voiceChat = fc.escutarVoz()

    retorno = fc.analisar_input(voiceChat)

    emocao = fc.analisarFrase(voiceChat,fc.identificador_usuario)

    print('o usuario disse: '+voiceChat+' e o bot entendeu como: '+emocao)

    es.enviarSerial(emocao)

    return jsonify({'status':'OK'})





#endregion





if __name__ == '__main__':

    app.run(host='0.0.0.0')
