# USE THIS FILE TO BUILD FRONT END APPLICATION

import socket

# Connection configurations
PORT = 34516
HOST = socket.gethostbyname(socket.gethostname())
print(HOST)

def limpar():
    print("\n" * 100)

while True:
    limpar()
    print("\t\t\t\t -----------------------------------------")
    print("\t\t\t\t | Bem-Vindo ao Adventure Game launcher | ")
    print("\t\t\t\t -----------------------------------------")
    print("\n      ----------------")
    print("|1| - | Começar      |")
    print("      ----------------")
    print("      ----------------")
    print("|0| - | Configuração |")
    print("      ----------------")
    resp = int(input("\nEntrada ----> "))
    limpar()
    if resp == 1:
        name = input("Entre com seu nome: ")
        file = open("log.txt", "a")
        file.write("Respostas do jogador -> " + name + "\n")
        file.close()
        break
    else:
        print("\t\t ----------------")
        print("\t\t | Configuração | ")
        print("\t\t ----------------")
        HOST = input("Ipv4 ----> ")
        PORT = int(input("Porta ----> "))
        limpar()

# Building connection
socketCliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
enderecoServidor = (HOST, PORT)
socketCliente.connect(enderecoServidor)

print("\n\n\t\t ---------------------------")
print("\t\t |    Adventure Game       | ")
print("\t\t ---------------------------")
print("\t\t ---------------------------")
print("\t\t |  Você pode sobreviver?  |")
print("\t\t ---------------------------\n\n")

print("\n      ----------------")
print("|1| - | Começar      |")
print("      ----------------")
print("      ----------------")
print("|0| - | Sair         |")
print("      ----------------")
escolha = int(input("\nEntrada ----> "))

limpar()

while True:
    perguntaRecebida = socketCliente.recv(1024)

    print(perguntaRecebida.decode())
    resposta = input("\n\nEntrada ----> ").encode()
    if resposta.decode() == '0':
        socketCliente.close()
        break
    print("\n\n")
    socketCliente.send(resposta)
    limpar()

socketCliente.close()
