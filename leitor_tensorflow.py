import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
import csv


#region treino carregamento e salvamento
def train(epochs_num):
    history = model.fit(
        training_sequences,
        training_labels,
        epochs=epochs_num,
        validation_data=(testing_sequences, testing_labels)
    )

def save():
    # salva o modelo com esse nome
    model.save('baxacinho.0.3')

def load():
    global model
    model = load_model('baxacinho.0.3')
#endregion

# todo o csv e passa para a varivale base_treinamento
with open('treinamento.csv', newline='', encoding='iso-8859-1') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')

    base_treinamento = [tuple(row) for row in reader]

    #print(base_treinamento)

#cria um data frame para adicionar as colunas
data = pd.DataFrame(base_treinamento)
data.columns = ['Frase', 'Sentimento']

#mapeia todas os sentimentos e depois compara e troca os nomes por valores
mapping = {'alegria': 0, 'neutro': 1, 'tristeza': 2, 'raiva': 3}
data['Sentimento'] = data['Sentimento'].map(mapping)

#pega os values das frases e sentimentos
texts = data['Frase'].values
labels = data['Sentimento'].values

#faz a tokenização das frases
tokenizer = Tokenizer(num_words=100000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

#A PARTIR DAQUI PODE COMENTAR PARA QUANDO NÃO FOR TREINAR
padded_sequences = pad_sequences(sequences, maxlen=100, truncating='post', padding='post')

training_size = int(len(padded_sequences) * 0.8)
training_sequences = padded_sequences[:training_size]
training_labels = labels[:training_size]

testing_sequences = padded_sequences[training_size:]
testing_labels = labels[training_size:]

model = Sequential([
    Embedding(10000, 64),
    Bidirectional(LSTM(64)),
    Dense(64, activation='relu'),
    Dense(4, activation='softmax')
])

#compila e executa todo o treinamento e testa
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#load()

# aqui faz o teste e calcula a acuracia do modelo
test_loss, test_acc = model.evaluate(testing_sequences, testing_labels)
#print('Test Accuracy:', test_acc)

#NÃO COMENTAR ESSA FUNÇÃO
def sentimento(alegria, raiva, tristeza, neutro):
    if alegria > raiva and alegria > tristeza and alegria > neutro:
        # print('O sentimento que está sentido é alegria')
        return "alegria"

    elif raiva > alegria and raiva > tristeza and raiva > neutro:
        # print('O sentimento que está sentido é raiva')
        return "raiva"

    elif tristeza > alegria and tristeza > raiva and tristeza > neutro:
        # print('O sentimento que está sentido é tristeza')
        return "tristeza"

    elif neutro > alegria and neutro > raiva and neutro > tristeza:
        # print('O sentimento que está sentido é neutro')
        return "neutro"

    else:
        # print('O sentimento não encontrado')
        return "desconhecido"


#funções para treinar e salvar dados
#train(13)
#save()