# USE THIS FILE TO BUILD BACK END APPLICATION

from gameManager import QuestionsBuild
from gameManager import GameManager
import socket, threading

gameManager = GameManager()
questionManager = QuestionsBuild()

HOST = ''               #endereco de IP é o da maquina atual
PORT = 21242
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
enderecoServidor = (HOST, PORT)
socketServidor.bind(enderecoServidor)
socketServidor.listen(1)

step = gameManager.getStep()

time = 0

def advance_time():
    global time
    time+=1

def get_time():
    global time
    return "\nDay: " + str(time)

while True :
    socketCliente, enderecoCliente = socketServidor.accept()
    print('Client connected => ', enderecoCliente)
    while True :
        pergunta = questionManager.getQuestion(step)
        clientText = pergunta.text + "\n" + pergunta.getAnswerText()

        threading.Thread(target=advance_time).start()

        socketCliente.send((clientText + get_time()).encode())

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
    break