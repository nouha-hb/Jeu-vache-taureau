
from tkinter import *
import string
import random
from function import Functions
from tkinter.messagebox import *


class Main(Functions):

    def __init__(self):
        super().__init__()
        self.root = Tk()
        self.root.title("Jeu Taureaux et Vaches ")
        self.root.geometry("986x720")
        self.root.iconbitmap("logo.ico")
        self.root.resizable(width=False, height=False)
        self.bg = PhotoImage(file="background.png")
        # create a canvas
        # create a canvas
        self.canvas1 = Canvas(self.root, width=986, height=720)
        self.canvas1.pack(fill="both", expand=True)
        # set image in canvas
        self.canvas1.create_image(0, 0, image=self.bg, anchor="nw")
        # buttons home page
        self.btStart = Button(text='JOUER', font=("Algerian", 17), fg="white", bg="#f00020", width=17, height=2,
                         command=self.start_game)


        self.btHow = Button(text='REGLES DU JEU', font=("Algerian", 17), fg="white", bg="#f00020", width=17, height=2,
                            command=  self.how_play)


        self.btQuit = Button(text='QUITTER', font=("Algerian", 17), fg="white", bg="#f00020", width=17, height=2,
                        command=quit)

        self.btStart_window = self.canvas1.create_window(330, 310, anchor="nw", window=self.btStart)
        self.btHow_window = self.canvas1.create_window(330, 410, anchor="nw", window=self.btHow)
        self.btQuit_window = self.canvas1.create_window(330, 510, anchor="nw", window=self.btQuit)

        self.root.mainloop()


    #meth start game

    def start_game(self):
        self.root.destroy()
        global screen1
        global btSubmit
        global code_secret
        global e

        my_font1 = ('Times', 18, 'bold')
        my_font2 = ('Times', 30, 'bold')
        font_btn = ('Times', 15)

        screen1 = Tk()
        screen1.title("Le jeu a commencé ! ")
        screen1.iconbitmap("logo.ico")
        screen1.geometry("986x720")
        screen1.resizable(width=False, height=False)
        bg1 = PhotoImage(file="bg2.png")
        # create a canvas
        canvas2 = Canvas(screen1, width=986, height=767)
        canvas2.pack(fill="both", expand=True)

        # set image in canvas
        canvas2.create_image(0, 0, image=bg1, anchor="nw")
        canvas2.create_text(250, 320, text="Entrez votre proposition :", font=my_font2, )
        code_secret = self.code_secret()
        canvas2.create_text(720, 370, text="Nombre:          Taureau          Vache", font=my_font1, fill="red")

        e = Entry(screen1, highlightcolor="gray", width=50, borderwidth=5)
        e.place(x=80, y=380)

        # bouttons de clavier
        btSubmit = Button(screen1, text="OK", font=font_btn,padx=10, pady=10, width=5,command=self.game)
        btSubmit_window = canvas2.create_window(310, 440, anchor="nw", window=btSubmit)
        btDelt = Button(screen1, text="DEL", font=font_btn, command=self.button_delete, padx=10, pady=10, width=5)
        btDelt_window = canvas2.create_window(310, 510, anchor="nw", window=btDelt)
        bt0 = Button(screen1, text="0", font=font_btn, command=lambda: self.button_click(0), padx=10, pady=10, width=5)
        bt0_window = canvas2.create_window(310, 580, anchor="nw", window=bt0)

        bt1 = Button(screen1, text="1", font=font_btn, command=lambda: self.button_click(1), padx=10, pady=10, width=3)
        bt1_window = canvas2.create_window(80, 440, anchor="nw", window=bt1)
        bt2 = Button(screen1, text="2", font=font_btn, command=lambda: self.button_click(2), padx=10, pady=10, width=3)
        bt2_window = canvas2.create_window(150, 440, anchor="nw", window=bt2)
        bt3 = Button(screen1, text="3", font=font_btn, command=lambda: self.button_click(3), padx=10, pady=10, width=3)
        bt3_window = canvas2.create_window(220, 440, anchor="nw", window=bt3)

        bt4 = Button(screen1, text="4", font=font_btn, command=lambda: self.button_click(4), padx=10, pady=10, width=3)
        bt4_window = canvas2.create_window(80, 510, anchor="nw", window=bt4)
        bt5 = Button(screen1, text="5", font=font_btn, command=lambda: self.button_click(5), padx=10, pady=10, width=3)
        bt5_window = canvas2.create_window(150, 510, anchor="nw", window=bt5)
        bt6 = Button(screen1, text="6", font=font_btn, command=lambda: self.button_click(6), padx=10, pady=10, width=3)
        bt6_window = canvas2.create_window(220, 510, anchor="nw", window=bt6)

        bt7 = Button(screen1, text="7", font=font_btn, command=lambda: self.button_click(7), padx=10, pady=10, width=3)
        bt7_window = canvas2.create_window(80, 580, anchor="nw", window=bt7)
        bt8 = Button(screen1, text="8", font=font_btn, command=lambda: self.button_click(8), padx=10, pady=10, width=3)
        bt8_window = canvas2.create_window(150, 580, anchor="nw", window=bt8)
        bt9 = Button(screen1, text="9", font=font_btn, command=lambda: self.button_click(9), padx=10, pady=10, width=3)
        bt9_window = canvas2.create_window(220, 580, anchor="nw", window=bt9)
        canvas2.pack()
        screen1.mainloop()
        #methode game

    def game(self):
        # le nombre des V et T
        def verifier_proposition(nombre, proposition):
            global e
            global y
            fontEssai = ('Times', 30, 'bold')
            self.nbessai -= 1
            # mise en place du compteur
            compteur = Label(screen1, text=str(self.nbessai), fg="black", bg="#CD853F", font=fontEssai, width=2)
            compteur.pack()
            compteur.place(x=110, y=220)

            font_btn = ('Times', 12)
            vach_tauro = [0, 0]
            nombre_li = self.list_chiffre(nombre)
            proposition_li = self.list_chiffre(proposition)

            for i, j in zip(nombre_li, proposition_li):
                if j in nombre_li:
                    if i == j:
                        vach_tauro[0] += 1
                    else:
                        vach_tauro[1] += 1

            resultat = Label(screen1, text=proposition + " :                                 " + str(
                vach_tauro[0]) + " T                          " + str(vach_tauro[1]) + " V    ",bg="white",
                             font=font_btn)
            resultat.pack()
            self.y = self.y + 23
            resultat.place(x=self.x, y=self.y)

            if (vach_tauro[0] == 4):
                e.delete(0, len(proposition))
                self.win()
            else:
                e.delete(0, len(proposition))

        global nbessai
        propsition = e.get()
        if propsition != "":
            if not self.verifier_longeur(propsition):
                showwarning('Erreur', 'votre code doit contenir exactement 4 chiffres ')
                e.delete(0, len(propsition))
            elif not self.verifier_tous_des_chiffres(propsition):
                showwarning('Erreur', 'votre code doit contenir seulement des chiffres ')
                e.delete(0, len(propsition))
            elif not self.verifier_deux_a_deux_different(propsition):
                showwarning('Erreur', 'votre code doit contenir  4 chiffres  deux a deux differents ')
                e.delete(0, len(propsition))
            else:
                verifier_proposition(code_secret, propsition)

                if self.nbessai <= 0:
                    self.lose()


    def win(self):
        screen1.destroy()
        win_scr = Tk()
        win_scr.iconbitmap("logo.ico")
        win_scr.title("BRAVO! Vous avez gagné")
        win_scr.geometry("512x512")
        win_scr.resizable(width=False, height=False)
        win_scr.resizable(width=False, height=False)
        win_bg = PhotoImage(file="winn.png")
        canvas3 = Canvas(win_scr, width=500, height=500)
        canvas3.pack(fill="both", expand=True)
        canvas3.create_image(0, 0, image=win_bg, anchor="nw")
        def clicker():
            win_scr.destroy()
            self.__init__()

        btREStart = Button(text='REJOUER', font=("Algerian", 12), fg="white", bg="#f00020", width=10, height=2,
                           command=clicker)
        btQuit = Button(text='QUITTER', font=("Algerian", 12), fg="white", bg="#f00020", width=10, height=2,
                        command=quit)
        canvas3.create_text(250, 30,fill="black",font=("bold",15), text="Bravoo! Vous avez deviné le code secret :"+str(code_secret))
        btREStart_window = canvas3.create_window(10, 400, anchor="nw", window=btREStart)
        btQuit_window = canvas3.create_window(390, 400, anchor="nw", window=btQuit)
        win_scr.mainloop()

    def button_click(self,number):


        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def button_delete(self):
        current = e.get()
        e.delete(len(current) - 1, END)
    def lose(self):
        screen1.destroy()
        scr = Tk()
        scr.iconbitmap("logo.ico")
        scr.title("Vous avez perdu!!!")
        scr.geometry("512x512")
        scr.resizable(width=False, height=False)
        win_bg = PhotoImage(file="cry.png")
        canvas3 = Canvas(scr, width=500, height=500)
        canvas3.pack(fill="both", expand=True)
        canvas3.create_image(0, 0, image=win_bg, anchor="nw")
        def clicker():
            scr.destroy()
            self.__init__()
        btREStart = Button(text='REJOUER', font=("Algerian", 12), fg="white", bg="#f00020", width=10, height=2,
                           command=clicker)
        btQuit = Button(text='QUITTER', font=("Algerian", 12), fg="white", bg="#f00020", width=10, height=2,
                        command=quit)
        canvas3.create_text(260, 30,fill="black",font=("bold",17), text="        Vous avez perdu !\n  le  code secret est :"+str(code_secret))


        btREStart_window = canvas3.create_window(9, 420, anchor="nw", window=btREStart)
        btQuit_window = canvas3.create_window(400, 420, anchor="nw", window=btQuit)
        scr.mainloop()

    def how_play(self):
        self.root.destroy()
        global screen2
        screen2 = Tk()
        font1 = ('Times', 20, 'bold')
        font2 = ('Arial', 11)
        screen2.resizable(width=False , height=False)
        screen2.iconbitmap("logo.ico")
        screen2.title("Les règles du jeu Taureaux et Vaches")
        screen2.geometry("986x767")
        def clicker():
            screen2.destroy()
            self.__init__()
        bg2 = PhotoImage(file="src3.png")
        canvas3 = Canvas(screen2, width=986, height=767)
        canvas3.pack(fill="both", expand=True)
        canvas3.create_image(0, 0, image=bg2, anchor="nw")
        canvas3.create_text(280, 40, text="Taureaux et vaches, un jeu avec des nombres", font=font1)
        canvas3.create_text(300, 215, font=font2, text="""                                         Le principe de ce jeu consiste à deviner un nombre à 4 chiffres à condition que :\n
                                              ! Ce nombre ne doit pas commencer par 0.\n
                                              ! Aucun de ses  chiffres ne se répète.\n
                                              Le résultat obtenu est sous forme des vaches et des taureaux, \n
                                               une vache indique qu'il existe un chiffre correcte mais n'est pas à sa place\n
                                               un taureau indique qu'il existe un chiffre correcte et à sa place\n

                                              Comme vous savez un jeu qui ne se perd plus n'a pas de gout alors le jeu se termine si vous échouez\n
                                              à trouver ce nombre dans 10 essais \n
                                              sinon si vous trouvez le nombre avant ou bien au 10éme essai vous gagnez.""")

        canvas3.create_text(80, 390, text="Exemple :", font=font1)
        canvas3.create_text(100, 540, font=font2, text="""    Code secret: 2567\n
             Essai 1: 1234 : 0T, 1V\n
             Essai 2: 5678 : 0T, 3V\n
             Essai 3: 3867 : 2T, 0V\n
             Essai 4: 2865 : 2T, 1V\n
             Essai 5: 2567 : 4T, 0V\n
             Bravo ! vous avez gagné""")
        btRET = Button(text='<--- ', font=("Algerian", 20), fg="white", bg="BLUE",
                       command=clicker)
        btREt_window = canvas3.create_window(850, 40, anchor="nw", window=btRET)

        screen2.mainloop()



