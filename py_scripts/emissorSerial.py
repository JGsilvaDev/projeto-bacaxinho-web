import serial
import time


def enviarSerial(texto):
    # Abre a conexão serial com o Arduino
    arduino = serial.Serial('<PORTA USB ONDE O ARDUINO ESTÁ>', 9600) #gera a conexão nessa porta
    # pequeno delay para garantir conexão
    time.sleep(2)
    mensagem = texto
    arduino.write(mensagem.encode())
    # Fecha a conexão
    arduino.close()