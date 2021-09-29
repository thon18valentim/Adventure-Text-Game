# USE THIS FILE TO BUILD FRONT END APPLICATION

import socket

# Connection configurations
HOST = '192.168.15.46' 
PORT = 12345

while True:
    print("\t\t -- Welcome to Adventure Game launcher -- ")
    print("\n(1) | Start |")
    print("\n(2) | Configurations |")
    resp = int(input("\nA.: "))

    if resp == 1:
        break
    else:
        print("\n\n\t\t -- Configurations -- ")
        HOST = input("Ipv4: ")
        PORT = int(input("Port: "))

# Building connection
socketCliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
enderecoServidor = (HOST, PORT)
socketCliente.connect(enderecoServidor)

#print('Digite X para sair')
#mensagem = input('Digite seu mensagem : ').encode()

print("\n\n\t\t -- Adventure Game -- ")
print("\n\t\t - Can you survive?")
escolha = int(input("(1) | Start Run |\n(0) | Exit Game |\n\nA.: "))

while escolha != 0:
    perguntaRecebida = socketCliente.recv(1024)

    print(perguntaRecebida.decode())
    resposta = input("\n\nA.: ").encode()
    socketCliente.send(resposta)

socketCliente.close()
