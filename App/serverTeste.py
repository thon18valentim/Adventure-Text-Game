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

        if(escolha.decode() == "1"):
            print("Deu certo")

    print('Conexao finalizada com o cliente ', enderecoCliente)
    socketCliente.close()