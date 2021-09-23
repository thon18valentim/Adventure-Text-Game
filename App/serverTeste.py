import socket
HOST = ''               #endereco de IP é o da maquina atual
PORT = 12345
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
enderecoServidor = (HOST, PORT)
socketServidor.bind(enderecoServidor)
socketServidor.listen(1)
i = 0

while True :
    socketCliente, enderecoCliente = socketServidor.accept()
    print('Cliente conectado => ', enderecoCliente)
    while True :
        resposta1 = socketCliente.recv(100)
        if not resposta1 : break
        print(enderecoCliente, resposta1.decode())
        if resposta1.decode() == '1':
            i += 1
            print(i)
            teste = i
            socketCliente.send(teste.encode())
        elif resposta1.decode() == '0' :
            i -= -1
            teste = 'Escolheu opção B'
            socketCliente.send(teste.encode())
        else:
            mensagemEnviada = 'Não seu do que você esta falando'
            socketCliente.send(mensagemEnviada.encode())
    print('Conexao finalizada com o cliente ', enderecoCliente)
    socketCliente.close()