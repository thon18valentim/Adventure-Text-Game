# USE THIS FILE TO BUILD FRONT END APPLICATION

import socket

# Connection configurations
PORT = 54321
HOST = socket.gethostbyname(socket.gethostname())
print(HOST)

def limpar():
    print("\n" * 100)

while True:
    limpar()
    print("\t\t\t\t -----------------------------------------")
    print("\t\t\t\t | Bem-Vindo ao Adventure Game launcher | ")
    print("\t\t\t\t -----------------------------------------")
    print("\n    ----------------")
    print("(1) | Começar      |")
    print("    ----------------")
    print("    ----------------")
    print("(2) | Configuração |")
    print("    ----------------")
    resp = int(input("\nEntrada ----> "))
    limpar()
    if resp == 1:
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

print("\t\t ---------------------------")
print("\t\t |    Jogo de aventura     | ")
print("\t\t ---------------------------")
print("\t\t ---------------------------")
print("\t\t |  Você pode sobreviver?  |")
print("\t\t ---------------------------\n\n")

escolha = int(input("(1) | Start Run |\n(0) | Exit Game |\n\nEntrada ----> "))
limpar()

while escolha != 0:
    perguntaRecebida = socketCliente.recv(1024)

    print(perguntaRecebida.decode())
    resposta = input("\n\nEntrada ----> ").encode()
    print("\n\n")
    socketCliente.send(resposta)
    limpar()

socketCliente.close()
