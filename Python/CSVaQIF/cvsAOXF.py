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


"""
La classe Application est une classe Frame
"""
class Application(Frame):
	""" """

	def OuvrirFichierDestination (self, name):
		self.dst = open(name, 'w')

	def FermerFichierDestination (self):
		self.dst.close()

	def OuvrirFichierSource (self, name):
		self.src = open(name, 'r')
		
	def FermetFichierSource (self):
		self.src.close()

	def EnteteFichier (self):
		""" """
		ligneEntete = ["OFXHEADER: 100", "DATA: OFXSGML", "VERSION: 102", "SECURITY: TYPE1",
				 "ENCODING: USASCII", "CHARSET: 1252", "COMPRESSION: NONE", "OLDFILEUID: NONE",
				 "NEWFILEUID: NONE" ]
		for ligne in ligneEntete:
			self.dst.write(ligne + "\n")

	def EnTeteOfx (date="20100409003507"):
		ligneOfx1 = ["<OFX>", "<SIGNONMSGSRSV1>", "<SONRS>", "<STATUS>", "<CODE>0", 
					"<SEVERITY>INFO", "</STATUS>" ]

		ligneOfxDTSERVER = ["<DTSERVER>" ]
		ligneOfx2 = [   "<LANGUAGE>FRE",
						"<INTU.BID>00014",
						"</SONRS>",
						"</SIGNONMSGSRSV1>" ]

		for ligne in ligneOfx1:
			self.dst.write(ligne + "\n")

		self.dst.write(ligneOfxDTSERVER + date + "[-5:EST]" + "\n")

		for ligne in ligneOfx2:
			self.dst.write(ligne + "\n")


	def Entete (self):
		self.OuvrirFichierDestination(name = "q.txt")
		self.EnteteFichier()
		self.EnTeteBanque( )
		self.FermerFichierDestination()


	def EnTeteBanque (self):
		ligneOfx = [   "<BANKMSGSRSV1>",
						"<STMTTRNRS>",
						"<TRNUID>0",
						"<STATUS>",
						"<CODE>0",
						"<SEVERITY>INFO",
						"</STATUS>",
						"<STMTRS>",
						"<CURDEF>CAD",
						"<BANKACCTFROM>",
						"<BANKID>800000100",
						"<ACCTID>",
						"<ACCTTYPE>CHECKING",
						"</BANKACCTFROM>",
						"<BANKTRANLIST>"
						 ]



	def Convertir (self):
		txt = ""
		fs = open("detail03172010.csv", 'r')
		fd = open("d.oxf", 'w')
		txt = fs.readline()
		print(txt)
		## Première ligne 
		### Date de l'opération,Date d'inscription au compte,Description,Montant
		ind = txt.find("Date")
		if ind == 0:
			# Ecrire l'entete.
			#fd.write("!Type:Bank\n")
			#Balayer toutes les lignes du fichier
			## "02/03/2010","02/03/2010","PAIEMENT CARTES CITI ENLIGNE ","-1,724.74"
			j = 0
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
						#print(table[0])
						date = table[0].strip('"')
						#print(table[1])
						date1 = table[1].strip('"')
						#print(table[2])
						comment = table[2].strip('"')
						#print(table[3])
						prix = table[3].strip('"\n\a ')
						#ind1 = prix.find('"')
						#prix[ind1] = 0
					print( date, "::", date1, "::", comment, "::", prix, "::")
					self.base.append( [date, comment, prix] )
					fd.write("D" + date[3] + date[4] + "/" + date[0] + date[1] + "/" + date[8] + date[9] + "\n")
					fd.write("T" + prix + "\n")
					fd.write("P" + comment + "\n")
					fd.write("^\n")
					print(j)
					j += 1

				else:
					le = len(self.base)
					print( le )
					i = 0
					while i < le:
						el = self.base[i]
						#print( i, ":", le, ":", el[0], el[1], el[2] )
						#print( i, ":", le, ":", el[0], el[1], el[2] )
						i += 1
						#print( el )
					break
					

		print("Fermer le fichier")
		fs.close()
		fs.close()
		
		return

	def CreateWidgets (self):
		self.can = Canvas(self, bg='white', height=self.Ylim, width=self.Xlim)


		self.Quit = Button(self, text='Quit', command=self.quit)
		self.can.grid(row=3, column=0, rowspan=7, columnspan=4, padx=10, pady=5)
		self.Quit.grid(row=6,column=6)

		self.Convertir = Button(self, text='Convertir', command=self.Convertir)
		self.Convertir.grid(row=7,column=6)

		self.Entete = Button(self, text='Entete', command=self.Entete)
		self.Entete.grid(row=8,column=6)

	def __init__ (self, master=None):
		Frame.__init__(self,master)
		self.dst = 0
		self.src = 0
		self.base = []
		self.Ylim = 150
		self.Xlim = 0
		self.CreateWidgets()
		self.pack()
		print(self.__doc__)

#################################################################################
# Programme principale (__main__)

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
