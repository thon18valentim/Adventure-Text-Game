# USE THIS FILE TO BUILD BACK END APPLICATION

from gameManager import QuestionsBuild
from gameManager import GameManager
import socket

gameManager = GameManager()
questionManager = QuestionsBuild()

HOST = ''               #endereco de IP é o da maquina atual
PORT = 54321
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
enderecoServidor = (HOST, PORT)
socketServidor.bind(enderecoServidor)
socketServidor.listen(1)

step = 1

while True :
    socketCliente, enderecoCliente = socketServidor.accept()
    print('Client connected => ', enderecoCliente)
    while True :

        pergunta = questionManager.getQuestionText(step) + "\n" + questionManager.getQuestionAnswers(step)
        socketCliente.send(pergunta.encode())

        escolha = socketCliente.recv(100)

        # Save answer in log.txt
        gameManager.saveAnswer(step,escolha.decode())

        esc = int(escolha.decode())
        print("Escolha -> %d" % esc)
        print("Step -> %d" % step)

        nextQuestionId = questionManager.getNextQuestion(step,esc)
        print("Next Question Id -> %d" % nextQuestionId)
 
        # Capturing question
        #question = questionManager.getQuestion(gameManager.getStep())
        # Advancing for the next question
        gameManager.advanceStep(nextQuestionId)
        step = gameManager.getStep()
        
        # Starting game
        # if gameManager.getStep() == 0:
        #     pergunta = questionManager.getQuestionText(1) + "\n" + questionManager.getQuestionAnswers(1)
        #     socketCliente.send(pergunta.encode())

        #     escolha = socketCliente.recv(100)

        #     gameManager.saveAnswer("1",escolha.decode())
        #     gameManager.advanceStep()
        #     socketCliente.send(" ".encode())
        
    print('Conexao finalizada com o cliente ', enderecoCliente)
    socketCliente.close()