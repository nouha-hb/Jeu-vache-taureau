from tkinter import *
import string
import random
from tkinter.messagebox import *
class Functions():
    def __init__(self,):
        self.nbessai = 10
        self.x = 560
        self.y = 391

    # une liste des chiffre d'un nombre
    def list_chiffre(self,nombre):
        list = []
        nombre = str(nombre)
        for i in range(4):
            list.append(nombre[i])
        return list

    # verifier si les chiffres d'un nombre sont differents
    def chiffre_differ(self,nombre):
        mum_list = self.list_chiffre(nombre)
        return len(mum_list) == len(set(mum_list))

    # construire le code secret
    def code_secret(self):
        while True:
            nombre = random.randint(1000, 9999)
            if self.chiffre_differ(nombre):
                print(nombre)
                return nombre

    # verifier len(nombre)==4
    def verifier_longeur(self,nombre):
        if len(nombre) == 4:
            return True

    # verifier que le nombre ne contient que des chiffres
    def verifier_tous_des_chiffres(self,nombre):
        nb = 0
        for i in range(4):
            if nombre[i] not in string.digits:
                nb = nb + 1
        if nb == 0:
            return True

    def verifier_deux_a_deux_different(self,nombre):
        for i in range(3):
            for j in range(i + 1, 4):
                if nombre[i] == nombre[j]:
                    return False
        return True


