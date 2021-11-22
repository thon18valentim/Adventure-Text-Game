import tkinter as tk
from tkinter.constants import LEFT

class Janela2:
    def __init__(self, master, root):
        
        self.nova = master
        self.nova.title("Configuração")
        self.fontePadrao = ("Verdana", "12", "bold")

        self.origem = root

        self.container1 = tk.Frame(master) #define o tamanho do pady
        self.container1["pady"] = 10
        self.container1.pack()
        
        self.container2 = tk.Frame(master)
        self.container2["pady"] = 20
        self.container2.pack()
        
        self.container3 = tk.Frame(master)
        self.container3["pady"] = 20
        self.container3.pack()
        
        self.container4 = tk.Frame(master)
        self.container4["pady"] = 30
        self.container4.pack()
        
        self.container5 = tk.Frame(master)
        self.container5["pady"] = 30
        self.container5.pack()
        
        self.lbTitulo = tk.Label(self.container1) #titulo
        self.lbTitulo["text"] = "Configuração"
        self.lbTitulo["font"] = self.fontePadrao
        self.lbTitulo.pack()

        self.lbIpv4 = tk.Label(self.container2) #container para adicionar o ip 
        self.lbIpv4["text"] = "IPV4"
        self.lbIpv4["font"] = self.fontePadrao
        self.lbIpv4.pack(side=LEFT)

        self.tbIpv4 = tk.Entry(self.container2) #pega o conteudo digitado
        self.tbIpv4["width"] = 30
        self.tbIpv4.pack(side=LEFT)
        
        self.lbPorta = tk.Label(self.container3) #container para adicionar o porta 
        self.lbPorta["text"] = "PORTA"
        self.lbPorta["font"] = self.fontePadrao
        self.lbPorta.pack(side=LEFT)

        self.tbPorta = tk.Entry(self.container3) #pega o conteudo digitado
        self.tbPorta["width"] = 30
        self.tbPorta.pack(side=LEFT)

        self.btnAutenticar = tk.Button(self.container4) #verifica o conteudo digitado
        self.btnAutenticar["text"] = "Atualizar"
        self.btnAutenticar["font"] = self.fontePadrao
        self.btnAutenticar["width"] = 12
        self.btnAutenticar["command"] = self.verificar
        self.btnAutenticar.pack()
        
        self.lbAutenticar = tk.Label(self.container4) #imprime a autenticação
        self.lbAutenticar["text"] = ""
        self.lbAutenticar["font"] = self.fontePadrao
        self.lbAutenticar.pack()
        # self.lbAutenticar = tk.Button(self.container4, command=self.voltarmenu)
        # self.btnAutenticar["text"] = "Atualizar"
        
        # self.btnexit = tk.Button(self.container5, command=self.voltarmenu) #volta ao menu
        # self.btnexit["text"] = "Começar"
        # self.btnexit["font"] = self.fontePadrao
        # self.btnexit["width"] = 12
        # self.btnexit.pack()
        
    def verificar(self):
        ipv4 = self.tbIpv4.get()
        porta = self.tbPorta.get()
        
        if ipv4 == "" or porta == "" :
            self.lbAutenticar["text"] = "Não autenticado"
        else :
            self.nova.withdraw()
            self.inicio = tk.Toplevel(self.nova)
            Janela3(self.inicio, self.nova)

    def voltar(self):
        self.origem.deiconify()
        self.nova.destroy() #vai fechar a janela
    
    def voltarmenu(self):
        self.nova.withdraw()
        self.inicio = tk.Toplevel(self.nova)
        Janela3(self.inicio, self.nova)
        
class Janela3:
    def __init__(self, master, root):
        
        self.nova = master
        self.nova.title("Configuração")
        self.fontePadrao = ("Verdana", "12", "bold")

        self.origem = root
        
        self.container1 = tk.Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        
        self.container2 = tk.Frame(master)
        self.container2["pady"] = 20
        self.container2.pack()
        
        self.container3 = tk.Frame(master)
        self.container3["pady"] = 20
        self.container3.pack()
        
        self.container4 = tk.Frame(master)
        self.container4["pady"] = 30
        self.container4.pack()
        
        self.lbTitulo = tk.Label(self.container1)
        self.lbTitulo["text"] = "Bem-Vindo ao Adventure Game Launcher"
        self.lbTitulo["font"] = self.fontePadrao
        self.lbTitulo.pack()

        self.lbNome = tk.Label(self.container2)
        self.lbNome["text"] = "Nome"
        self.lbNome["font"] = self.fontePadrao
        self.lbNome.pack(side=LEFT)

        self.tbNome = tk.Entry(self.container2)
        self.tbNome["width"] = 30
        #self.tbNome["text"] = self.fontePadrao
        self.tbNome.pack(side=LEFT)
        
        self.btnupdate = tk.Button(self.container3)
        self.btnupdate["text"] = "Começar"
        self.btnupdate["font"] = self.fontePadrao
        self.btnupdate["width"] = 12
        self.btnupdate.pack()
        
        self.btnexit = tk.Button(self.container4)
        self.btnexit["text"] = "Sair"
        self.btnexit["font"] = self.fontePadrao
        self.btnexit["width"] = 12
        self.btnexit.pack()
        
    def voltar(self):
        self.origem.deiconify()
        self.nova.destroy() #vai fechar a janela 
        
        
class Tela:
    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title("Adventure Game Launcher")
        self.fontePadrao = ("Verdana", "12", "bold")
        
        self.container1 = tk.Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        
        self.container2 = tk.Frame(master)
        self.container2["pady"] = 20
        self.container2.pack()
        
        self.container3 = tk.Frame(master)
        self.container3["pady"] = 20
        self.container3.pack()
        
        self.container4 = tk.Frame(master)
        self.container4["pady"] = 20
        self.container4.pack()
        
        self.lbTitulo = tk.Label(self.container1)
        self.lbTitulo["text"] = "Bem-Vindo ao Adventure Game Launcher"
        self.lbTitulo["font"] = self.fontePadrao
        self.lbTitulo.pack()
        
        self.btnplay = tk.Button(self.container2, command=self.playing)
        self.btnplay["text"] = "Começar"
        self.btnplay["font"] = self.fontePadrao
        self.btnplay["width"] = 12
        self.btnplay.pack()
        
        self.btnconfig = tk.Button(self.container3, command=self.abrir)
        self.btnconfig["text"] = "Configuração"
        self.btnconfig["font"] = self.fontePadrao
        self.btnconfig["width"] = 12
        self.btnconfig.pack()
        
        self.btnexit = tk.Button(self.container4)
        self.btnexit["text"] = "Sair"
        self.btnexit["font"] = self.fontePadrao
        self.btnexit["width"] = 12
        self.btnexit.pack()
        
        #self.btn = tk.Button(self.nossaTela, text="Abrir interface", command=self.abrir)
        #self.btn.pack(padx=200, pady=200)
        
    def abrir(self):
        self.nossaTela.withdraw()
        self.novaTela = tk.Toplevel(self.nossaTela)
        Janela2(self.novaTela, self.nossaTela)
    
    def playing(self):
        self.nossaTela.withdraw()
        self.telaplay = tk.Toplevel(self.nossaTela)
        Janela3(self.telaplay, self.nossaTela)
    
janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()