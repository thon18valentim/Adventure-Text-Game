# USE THIS FILE TO BUILD FRONT END APPLICATION

import socket
import tkinter as tk
from tkinter.constants import LEFT
from tkinter import *

# Connection configurations
PORT = 21242
HOST = socket.gethostbyname(socket.gethostname())
socketCliente = None
print(HOST)

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb  

def apply_settings(frame):
    global PORT
    global HOST
    PORT = int(configureFrame_PortField.get("1.0", "end"))
    HOST = configureFrame_IpField.get("1.0", "end")
    frame.destroy()

def apply_name(frame):
    file = open("log.txt", "a")
    file.write("Respostas do jogador -> %s" % insertNameFrame_Field.get('1.0', 'end'))
    file.close()
    frame.destroy()

def advance_gameplay(title, button1, button2, button3):
    title.destroy()
    button1.destroy()
    button2.destroy()
    button3.destroy()

main_screen = tk.Tk()
main_screen.title("Andarilho")
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

menu_title = tk.Label(main_screen, text="Andarilho", font=("Arial",15))
menu_title.pack(pady=25)

menu_btn1 = tk.Button(main_screen, text="Play", command=lambda: show_frame(insertNameFrame), width=40, height=2, bg=rgb_hack((207, 87, 61)))
menu_btn1.pack(pady=5)

menu_btn2 = tk.Button(main_screen, text="Settings", command=lambda: show_frame(configureFrame), width=40, height=2, bg=rgb_hack((207, 87, 61)))
menu_btn2.pack(pady=5)

menu_btn3 = tk.Button(main_screen, text="Exit", command= main_screen.destroy, width=35, height=2, bg='red')
menu_btn3.pack(pady=5)

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

############### Insert Frame Code ###############
def build_connection():
    global HOST, PORT, socketCliente
    # Building connection
    socketCliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    enderecoServidor = (HOST, PORT)
    socketCliente.connect(enderecoServidor)
    print("Conectado")

insertNameFrame = tk.Frame(main_screen, bg=rgb_hack((207, 87, 61)))
insertNameFrame_title= tk.Label(insertNameFrame, text="Insert Name", bg=rgb_hack((207, 87, 61)))
insertNameFrame_title.pack()
insertNameFrame_Field = tk.Text(insertNameFrame, height=2, width=30)
insertNameFrame_Field.pack()
insertNameFrame_applyBtn = tk.Button(insertNameFrame, text="Apply", command=lambda: [apply_name(insertNameFrame), advance_gameplay(menu_title, menu_btn1, menu_btn2, menu_btn3), build_connection(), gameplay()])
insertNameFrame_applyBtn.pack(pady=3)

#--------------------------------------------#
## Gameplay ##
question_text = tk.Label(main_screen, text="Question", bg=rgb_hack((207, 87, 61)))
question_btn1 = tk.Button(main_screen, text="Option1", bg=rgb_hack((207, 87, 61)))
question_btn2 = tk.Button(main_screen, text="Option2", bg=rgb_hack((207, 87, 61)))
question_btn3 = tk.Button(main_screen, text="Sair do Jogo", bg=rgb_hack((207, 87, 61)))

def show_new_question(text, button1, button2):
    text.pack()
    button1.pack()
    button2.pack()

def close_socket(screen):
    global socketCliente
    socketCliente.close()
    screen.destroy()

def send_message(id):
    global socketCliente

    if id == 0:
        socketCliente.send("1".encode())
    else:
        socketCliente.send("2".encode())
    
    gameplay()

def gameplay():

    global question_text
    global question_btn1
    global question_btn2
    global question_btn3

    global main_screen

    question_text.pack()
    question_btn1.pack()
    question_btn2.pack()
    question_btn3.pack()

    perguntaRecebida = socketCliente.recv(1024)

    question_text.destroy()
    question_btn1.destroy()
    question_btn2.destroy()
    question_btn3.destroy()

    question_text = tk.Label(main_screen, text=perguntaRecebida, bg=rgb_hack((207, 87, 61)))
    question_btn1 = tk.Button(main_screen, text="Option1", bg=rgb_hack((207, 87, 61)), command=lambda: send_message(0))
    question_btn2 = tk.Button(main_screen, text="Option2", bg=rgb_hack((207, 87, 61)), command=lambda: send_message(1))
    question_btn3 = tk.Button(main_screen, text="Sair do Jogo", bg=rgb_hack((207, 87, 61)), command=lambda: close_socket(main_screen))

    question_text.place(y=10, x= 50)
    question_btn1.place(x= 260, y=240,height='40', width="80")
    question_btn2.place(x= 260, y=300,height='40', width="80")
    question_btn3.place(x= 500, y=320,height='40', width="80")

main_screen.mainloop()