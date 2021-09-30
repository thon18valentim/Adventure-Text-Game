# USE THIS FILE TO BUILD BACK END APPLICATION

from scripts.gameManager import QuestionsBuild
from scripts.gameManager import GameManager
import socket

gameManager = GameManager()
questionManager = QuestionsBuild()

HOST = ''               #endereco de IP é o da maquina atual
PORT = 12345
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
enderecoServidor = (HOST, PORT)
socketServidor.bind(enderecoServidor)
socketServidor.listen(1)
i = 0

while True :
    socketCliente, enderecoCliente = socketServidor.accept()
    print('Client connected => ', enderecoCliente)
    while True :
        
        # Starting game
        if gameManager.getStep() == 0:
            pergunta = questionManager.getQuestionText(1) + "\n" + questionManager.getQuestionAnswers(1)
            socketCliente.send(pergunta.encode())

            escolha = socketCliente.recv(100)

            if(escolha.decode() == "1" and questionManager.questions[0].getIsAdeath() == True):
                print("Você Morreu")
            elif(escolha.decode() == "1" and questionManager.questions[0].getIsAdeath() == False):
                print("Sobreviveu")
            elif(escolha.decode() == "2" and questionManager.questions[0].getIsBdeath() == True):
                print("Você Morreu")
            else:
                print("Sobreviveu") 

            gameManager.advanceStep()

        elif gameManager.getStep() == 1:
            pergunta = questionManager.getQuestionText(2) + "\n" + questionManager.getQuestionAnswers(2)
            socketCliente.send(pergunta.encode())

            escolha = socketCliente.recv(100)

            if(escolha.decode() == "1" and questionManager.questions[1].getIsAdeath() == True):
                print("Você Morreu")
            elif(escolha.decode() == "1" and questionManager.questions[1].getIsAdeath() == False):
                print("Sobreviveu")
            elif(escolha.decode() == "2" and questionManager.questions[1].getIsBdeath() == True):
                print("Você Morreu")
            else:
                print("Sobreviveu") 

            gameManager.advanceStep()

    print('Conexao finalizada com o cliente ', enderecoCliente)
    socketCliente.close()