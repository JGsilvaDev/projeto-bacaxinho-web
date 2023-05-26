import serial
import time


def enviarSerial(texto):
    try:
        # Abre a conexão serial com o Arduino
        arduino = serial.Serial('/dev/ttyACM0', 9600) #gera a conexão nessa porta
        # pequeno delay para garantir conexão
        time.sleep(2)
        mensagem = texto
        arduino.write(mensagem.encode())
        # Fecha a conexão
        arduino.close()
    except:
        print('serial não disponível')