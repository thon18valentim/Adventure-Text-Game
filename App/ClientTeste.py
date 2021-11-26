# USE THIS FILE TO BUILD FRONT END APPLICATION

import socket
import tkinter as tk
from tkinter.constants import LEFT
from tkinter import *

# Connection configurations
PORT = 34516
HOST = socket.gethostbyname(socket.gethostname())
print(HOST)

main_screen = tk.Tk()
main_screen.title("Adventure Game")
main_screen.resizable(False, False)
#main_screen.iconbitmap("img/sunIcon.ico")

main_screen.iconbitmap(r"App\img\sunIcon.ico")

c = Canvas(main_screen, bg = "gray16", height=400, width=600)
filename = PhotoImage(file=r"App\img\Background.png")
background_label = Label(main_screen,image=filename)
background_label.place(x=0,y=0, relwidth=1, relheight=1)
c.pack()

#Window Resolution
window_width = 600
window_heigh = 400

# Screen Resolution
screen_width = main_screen.winfo_screenwidth()
screen_heigh = main_screen.winfo_screenheight()

# Window position
posx = screen_width/2 - window_width/2
posy = screen_heigh/2 - window_heigh/2

main_screen.geometry("%dx%d+%d+%d" % (window_width, window_heigh, posx, posy))

menu_btn = tk.Button(main_screen, text="Play", command=lambda: print("Jogar"))
menu_btn.pack()

menu_btn = tk.Button(main_screen, text="Settings", command=lambda: print("Configurar"))
menu_btn.pack()

menu_btn = tk.Button(main_screen, text="Exit", command=lambda: print("Fechar aplicação"))
menu_btn.pack()

main_screen.mainloop()

while True:
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


while True:
    perguntaRecebida = socketCliente.recv(1024)

    print(perguntaRecebida.decode())
    resposta = input("\n\nEntrada ----> ").encode()
    if resposta.decode() == '0':
        socketCliente.close()
        break
    print("\n\n")
    socketCliente.send(resposta)

socketCliente.close()
