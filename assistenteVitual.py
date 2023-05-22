import funcoes as fc

# variáveis de comandos
AWAKE_COMMANDS = ['bacaxinho', 'abacaxi', 'cachinho', 'cachimbo', 'ximbinha',
                  'maluco', 'acorda porra', 'zé ruela', 'cabeça de lata']

if __name__ == "__main__":

    id = '9'

    # loop principal
    while True:

        #print('Aguardando chamada...')
        # aguardando chamada
        # comando = fc.recebeInput()
        # if fc.chamou(AWAKE_COMMANDS, comando):
        #     #ultimoSentimento = fc.ultimoSentimento()
        #     fc.saudacao()
        #     fc.awake()

        #     id = '9'

        # ao chamar
        #while True:
        print("Escutando...")

        comando=fc.recebeInput()

        

        # função que salva o sentimento no banco
        # fc.analisarFrase(comando, id)

        #função que analisa a melhro resposta
        print(fc.analisar_input(comando))
