# -*- coding:Latin-1 -*-
#################################################################################
# Programme: Convertisseur de fichier format csv vers qif.
# Référence: Format QIF
# Auteur: Benoit Massé
# Licence : GPL
#################################################################################

#################################################################################
# Importation des fonctions externes.
from tkinter import *
from math import *

#################################################################################
# Fonctions locales.



class Application(Frame):
    """ """
    def Convertir (self):
        txt = ""
        fs = open("detail03172010.csv", 'r')
        fd = open("d.qif", 'w')
        txt = fs.readline()
        print(txt)
        ## Première ligne 
        ### Date de l'opération,Date d'inscription au compte,Description,Montant
        ind = txt.find("Date")
        if ind == 0:
            # Ecrire l'entete.
            fd.write("!Type:Bank\n")
            #Balayer toutes les lignes du fichier
            ## "02/03/2010","02/03/2010","PAIEMENT CARTES CITI ENLIGNE ","-1,724.74"
            while 1:
                txt = fs.readline()
                if (len(txt) > 11) and (txt != '') :
                    table = txt.split("\",\"")
                    if len(table) == 5:
                        date = table[0].strip('"')
                        date1 = table[1].strip('"')
                        comment = table[2].strip('"')
                        prix = table[3].strip('"') + table[4].strip('"\n\a ')
                        #ind1 = prix.find('"')
                        #prix[ind1] = ''
                    else:
                        print(table[0])
                        date = table[0].strip('"')
                        print(table[1])
                        date1 = table[1].strip('"')
                        print(table[2])
                        comment = table[2].strip('"')
                        print(table[3])
                        prix = table[3].strip('"\n\a ')
                        #ind1 = prix.find('"')
                        #prix[ind1] = 0
                    print( date, "::", date1, "::", comment, "::", prix, "::")
                    fd.write("D" + date[3] + date[4] + "/" + date[0] + date[1] + "/" + date[8] + date[9] + "\n")
                    fd.write("T" + prix + "\n")
                    fd.write("P" + comment + "\n")
                    fd.write("^\n")

                else:
                    break
                    


        fs.close()
        fd.close()
        return

    def CreateWidgets (self):
        self.can = Canvas(self, bg='white', height=self.Ylim, width=self.Xlim)


        self.Quit = Button(self, text='Quit', command=self.quit)
        
        self.can.grid(row=3, column=0, rowspan=7, columnspan=4, padx=10, pady=5)
        self.Quit.grid(row=6,column=6)

        self.Convertir = Button(self, text='Convertir', command=self.Convertir)
        self.Convertir.grid(row=7,column=6)

    def __init__ (self, master=None):
		# Appel à la fonction Frame de Tkinter
        Frame.__init__(self,master)
        self.Ylim = 300
        self.Xlim = 300
        self.CreateWidgets()
        self.pack()
        print(self.__doc__)

#################################################################################
# Programme principale (__main__)

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
