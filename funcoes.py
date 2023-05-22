# import pyttsx3 as py
import datetime as dt
import speech_recognition as sr
import os
import webbrowser as wb
import openai as op

import sqlite3
import datetime

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from googletrans import Translator

from tensorflow.keras.models import load_model
import leitor_tensorflow as tf

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import json

# texto_fala = py.init()

# variáveis de controle
# modo texto, se for verdadeiro, irá alternar a fala do microfone para modo de teclado
text_mode = True
acordado = False
bot_name = 'bacaxinho'  # nome do bot

# funcoes de configuração

# def falar(audio):

#     # print do que o robo falar, para funções de debug
#     print(bot_name+': ' + audio)

#     rate = texto_fala.getProperty('rate')
#     texto_fala.setProperty(rate, 999)

#     rate = texto_fala.getProperty('rate')
#     texto_fala.setProperty(rate, 120)

#     volume = texto_fala.getProperty('volume')
#     texto_fala.setProperty(volume, 1.0)

#     voices = texto_fala.getProperty('voices')
#     texto_fala.setProperty('voice', voices[0].id)

#     texto_fala.say(audio)
#     texto_fala.runAndWait()

def textMode():
    global text_mode
    text_mode = not text_mode

# def microfone():
#     r = sr.Recognizer()

#     with sr.Microphone() as mic:
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(mic)
#         audio = r.listen(mic)

#     try:
#         print("Reconhecendo...")
#         comando = r.recognize_google(audio, language='pt-BR')
#         print(comando)

#     except Exception as e:
#         print(e)
#         print("Por favor repita, não te escutei!")

#         return "None"

#    return comando

def openia(fala):
    return ('Pesquisa por OPENAI desativada por enquanto...')

def searchKey(dc, keywords, comando):

    for i in keywords:
        if i in comando:
            return keywords.index(i)

    return -1

# def ouvir():
#     print('escutando microfone...')
#     listener = sr.Recognizer()
#     sr.Microphone.list_microphone_names()

#     try:
#         with sr.Microphone(device_index=1) as source:
#             print('Listening...')
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice, language='pt-PT')
#             print(command)
#             return command
#     except:
#         return 'No Sound'

def spotify():
    return 'spotify desativado por enquanto'

def endapp():
    print('até a próxima')
    exit()

def tempo():
    Tempo = dt.datetime.now().strftime("%I:%M")
    return ("Agora são: " + Tempo)

def data():
    meses = {'1': 'janeiro', '2': 'fevereiro', '3': 'março', '4': 'abril', '5': 'maio', '6': 'junho',
             '7': 'julho', '8': 'agosto', '9': 'setembro', '10': 'outubro', '11': 'novembro', '12': 'dezembro'}
    ano = str(dt.datetime.now().year)
    mes = str(dt.datetime.now().month)
    dia = str(dt.datetime.now().day)

    return('Hoje é dia '+ dia + ' de ' + meses[mes] + ' de ' + ano)

def saudacao():
    print("Olá poderosíssimo Mago. Bem vindo de volta!")
    print(bot_name+" a sua disposição! Lance a braba!")

def comoestou():
    return ('estou muito bem, obrigado!')

def melhortime():
    return ('O melhor time certamente é o corinthians')

def quemsoueu():
    return ('Eu sou o ' + bot_name + ' e é um prazer em conhecer você')

def codigofonte():
    wb.open('https://github.com/MeirellesDEV/Assistente_Virtual')

def apresentacao():
    return 'Rodrigo, responsável pela integração entre front e back end<br><a href="https://github.com/RodrigoTheDev">https://github.com/RodrigoTheDev</a><br>Meirelles, desenvolvedora auxiliar do back end<br><a href="https://github.com/MeirellesDEV">https://github.com/MeirellesDEV</a><br>João, responsável pelos bancos de dados e back end<br><a href="https://github.com/JGsilvaDev">https://github.com/JGsilvaDev</a>'

def chamou(list, command):
    for i in list:
        if i in command:
            return True
    return False

def recebeInput():
    if text_mode is True:
        print('digite alguma coisa: ')
        comando = input('>> ')
    else:
        comando = microfone().lower()

    return comando

def tradutor(fala):
    trans = Translator()

    LANGUAGES = {
        'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani',
        'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan',
        'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)',
        'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english',
        'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian',
        'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole',
        'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong',
        'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian',
        'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean',
        'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian',
        'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese',
        'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian',
        'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi',
        'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho',
        'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali',
        'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil',
        'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek',
        'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'
    }

    txt = str(fala.replace('como fala', '').replace('em', '')).split()
    lang = txt[-1]

    idioma = str(trans.translate(lang, dest="en").text).lower()

    items = LANGUAGES.items()

    for item in items:
        if (item[1] == idioma):
            codLang = item[0]

    txt.pop()  # retira a linguagem do array
    conteudo = ' '.join(txt)

    print(trans.translate(conteudo, dest=codLang).text)

def analisarFrase(str, id):

    model = load_model('baxacinho.0.3')

    frase = str
    nova_sequencia = tf.tokenizer.texts_to_sequences([frase])
    nova_sequencia_padded = tf.pad_sequences(
        nova_sequencia, maxlen=100, truncating='post', padding='post')
    prediction = model.predict(nova_sequencia_padded)[0]

    mapping_reverse = {0: 'alegria', 1: 'neutro', 2: 'tristeza', 3: 'raiva'}

    for i, prob in enumerate(prediction):
        # print(f'{mapping_reverse[i]}: {prob:.3f}')

        if f'{mapping_reverse[i]}' == 'alegria':
            alegria = f'{prob:.3f}'

        if f'{mapping_reverse[i]}' == 'raiva':
            raiva = f'{prob:.3f}'

        if f'{mapping_reverse[i]}' == 'tristeza':
            tristeza = f'{prob:.3f}'

        if f'{mapping_reverse[i]}' == 'neutro':
            neutro = f'{prob:.3f}'

    sentimento = tf.sentimento(alegria, raiva, tristeza, neutro)

    conn = sqlite3.connect('bacaxinho.db')
    cursor = conn.cursor()

    cursor.execute("SELECT identificador FROM usuario u WHERE u.id = "+id)
    resultado = cursor.fetchall()
    nomeTabela = resultado[0][0]

    cursor.execute(
        "SELECT id FROM sentimento s WHERE s.nome = '"+sentimento+"'")
    sent = cursor.fetchall()
    id_sentimento = sent[0][0]

    dataAtual = datetime.date.today().strftime("%d/%m/%Y")

    cursor.execute("INSERT INTO "+nomeTabela +
                   "(id_usuario,id_sentimento,dt_insercao)VALUES(?,?,?)", (id, id_sentimento, dataAtual))
    conn.commit()

    return sentimento

def analisar_input(input_usuario):
    resposta = ""


    palavras_chave = json.loads(open('input/palavras_chave.json', 'r').read())

    input_usuario = input_usuario.lower()
    
    # tokeniza o input em palavras
    palavras = word_tokenize(input_usuario)
    
    # remove as stop words (palavras comuns sem significado, como "em", "de", "a", etc.)
    palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords.words('portuguese')]
    
    # realiza a lematização das palavras (transformação das palavras para sua forma base)
    lemmatizer = WordNetLemmatizer()
    palavras_lemmatizadas = [lemmatizer.lemmatize(palavra) for palavra in palavras_sem_stopwords]

    funcao_executada = False

    for row in palavras_chave:
        indice = row['indice']
        for palavra in palavras_lemmatizadas:
            # print(palavra)
            # print(palavras_lemmatizadas)
            if palavra in indice:
                resposta = eval(row['funcao'])
                funcao_executada = True
                break

    if not funcao_executada:
        return openia(input_usuario)
    
    #retornando resposta
    return resposta

def ultimoSentimento(id):

    conn = sqlite3.connect('bacaxinho.db')
    cursor = conn.cursor()

    cursor.execute("SELECT identificador FROM usuario u WHERE u.id = "+id)
    resultado = cursor.fetchall()
    nomeTabela = resultado[0][0]

    cursor.execute("SELECT id_sentimento FROM "+nomeTabela+" ORDER BY id desc")
    idsent = cursor.fetchall()
    id_sentimento = idsent[0][0]

    cursor.execute(
        "SELECT s.nome FROM sentimento s WHERE s.id = '"+str(id_sentimento)+"'")
    sent = cursor.fetchall()
    sentimento = sent[0][0]

    return sentimento
