# USE THIS FILE TO BUILD FRONT END APPLICATION

import socket
import tkinter as tk
from tkinter.constants import LEFT
from tkinter import *

# Connection configurations
PORT = 34516
HOST = socket.gethostbyname(socket.gethostname())
print(HOST)

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb  

def apply_settings(frame):
    global PORT
    global HOST
    PORT = int(configureFrame_PortField.get("1.0", "end"))
    HOST = configureFrame_IpField.get("1.0", "end")
    frame.destroy()

def advance_gameplay(title):
    title.destroy()

main_screen = tk.Tk()
main_screen.title("Adventure Game")
main_screen.resizable(False, False)

main_screen.iconbitmap(r"App\img\sunIcon.ico")

c = Canvas(main_screen, bg = "gray16", height=400, width=600)
filename = PhotoImage(file=r"App\img\Background.png")
background_label = Label(main_screen,image=filename)
background_label.place(x=0,y=0, relwidth=1, relheight=1)
#c.pack()

#Window Resolution
window_width = 600
window_heigh = 400

# Screen Resolution
screen_width = main_screen.winfo_screenwidth()
screen_heigh = main_screen.winfo_screenheight()

# Frames
def show_frame(frame):
    frame.pack()

configureFrame = tk.Frame(main_screen, bg=rgb_hack((207, 87, 61)))
insertNameFrame = tk.Frame(main_screen)

background_label.place(x=0,y=0, relwidth=1, relheight=1)

# Window position
posx = screen_width/2 - window_width/2
posy = screen_heigh/2 - window_heigh/2

main_screen.geometry("%dx%d+%d+%d" % (window_width, window_heigh, posx, posy))

menu_title = tk.Label(main_screen, text="Adventure Game", font=("Arial",15))
menu_title.pack(pady=25)

menu_btn = tk.Button(main_screen, text="Play", command=lambda: advance_gameplay(menu_title), width=40, height=2, bg=rgb_hack((207, 87, 61)))
menu_btn.pack(pady=5)

menu_btn = tk.Button(main_screen, text="Settings", command=lambda: show_frame(configureFrame), width=40, height=2, bg=rgb_hack((207, 87, 61)))
menu_btn.pack(pady=5)

menu_btn = tk.Button(main_screen, text="Exit", command= main_screen.destroy, width=35, height=2, bg='red')
menu_btn.pack(pady=5)

# for frame in (configureFrame, insertNameFrame, gameplayFrame):
#     frame.grid(row=0, column=0,sticky='nsew')

############### Configure Frame Code ###############
configureFrame_title = tk.Label(configureFrame, text="Settings", bg=rgb_hack((207, 87, 61)))
configureFrame_title.pack()

configureFrame_IpTitle = tk.Label(configureFrame, text="Ipv4", bg=rgb_hack((207, 87, 61)))
configureFrame_IpTitle.pack()
configureFrame_IpField = tk.Text(configureFrame, height=2, width=30)
configureFrame_IpField.pack()

configureFrame_PortTitle = tk.Label(configureFrame, text="Port", bg=rgb_hack((207, 87, 61)))
configureFrame_PortTitle.pack()
configureFrame_PortField = tk.Text(configureFrame, height=2, width=30)
configureFrame_PortField.pack()

configureFrame_applyBtn = tk.Button(configureFrame, text="Apply", command=lambda: apply_settings(configureFrame))
configureFrame_applyBtn.pack(pady=3)

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
