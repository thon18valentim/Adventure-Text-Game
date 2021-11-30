# USE THIS FILE TO BUILD BACK END APPLICATION

from gameManager import QuestionsBuild
from gameManager import GameManager
import socket

gameManager = GameManager()
questionManager = QuestionsBuild()

HOST = ''               #endereco de IP é o da maquina atual
PORT = 21242
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
enderecoServidor = (HOST, PORT)
socketServidor.bind(enderecoServidor)
socketServidor.listen(1)

step = gameManager.getStep()

while True :
    socketCliente, enderecoCliente = socketServidor.accept()
    print('Client connected => ', enderecoCliente)
    while True :
        pergunta = questionManager.getQuestion(step)
        clientText = pergunta.text + "\n" + pergunta.getAnswerText()

        socketCliente.send(clientText.encode())

        escolha = socketCliente.recv(100)

        if pergunta.getId() == 66 or pergunta.getId() == 67:
            break

        if pergunta.getId() == 100:
            break

        # Save answer in log.txt
        gameManager.saveAnswer(step,escolha.decode())

        esc = int(escolha.decode())

        nextQuestionId = questionManager.getNextQuestion(step,esc)

        # Advancing for the next question
        gameManager.advanceStep(nextQuestionId)
        step = gameManager.getStep()

    print('Conexao finalizada com o cliente ', enderecoCliente)
    socketCliente.close()