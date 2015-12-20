#!c:\python\python.exe
# coding: latin-1

import sys
import os
import errno
import time
import math

class chap4:
	def __init__(self):
		print "chap4.__init__"
	def toto(self):
		print "chap4.toto"
	def if_test(self):
		print "chap4.if_test"
		self.a = 1
		self.googol = 10 ** 100
		if self.a > self.googol:
			print "a > googol"
		elif self.a == self.googol:
			print "a == googol"
		elif self.a < self.googol:
			print "a < googol"
		else:
			print "a est ni plus petit, ni plus grand, ni egal à googol, c'est etrange"
		
	def for_loop(self):
		print "chap4_for_loop"
		self.list1 = 1,2,3,4
		self.list2 = (1,2,3,4)
		self.list3 = ("a    bonjour   ", 1, 2, 3, "e" )
		self.list4 = ["a    bonjour   ", 1, 2, 3, "e" ]
		for i in self.list1:
			print i
		for i in self.list2:
			print i
		for i in self.list3:
			print i
		for i in self.list4:
			print i
		self.range1 = range(10)
		# Produit un range vide.
		self.range2 = range(-10)
		# Produit un range vide.
		self.range3 = range(0)
		# Va de -5 à 9 par pas de 1.
		self.range4 = range(-5,10)
		# self.range5 = range(-9,9,0.01) cela donne une erreur
		# Va de -9 a 8 par pas de 1.
		self.range5 = range(-9,9,1.01) # donne un increment de 1
		# Compte à rebour par pas de 2 de 10 à 0.
		self.range6 = range(10,-2,-2) # donne un increment de 1
		
		for i in self.range1:
			print i
		for i in self.range2:
			print i
		for i in self.range3:
			print i
		for i in self.range4:
			print i
		for i in self.range5:
			print i
		for i in self.range6:
			if i != 0:
				print i
			else:
				print "Mise à feu"
		for i in self.range6:
			if i != 0:
				print i
			else:
				print "Mise à feu"
				break
	def while_loop(self):
		self.y = -800
		self.b = "non"
		while self.y < 2500:
			if self.b == "oui":
				print "L'année est ", self.y
				break
			if (self.y % 400) == 0:
				print self.y, "est bissextile dans les deux calendriers"
			elif (self.y % 100) == 0:
				print self.y, "est bissextile dans le calendrier julien"
			if (self.y >= 0 ):
				self.b = "oui"
			self.y = self.y + 100
		while self.y < 3000:
			if (self.y % 700 ) == 0:
				print self.y, " est divisible par 700"
			self.y = self.y + 100
			if (self.y % 300):
				# Ne fait rien, comme un no-op.
				pass
			# Retourne au debut de la boucle.
			continue
		else:
			print "Ici est le else du while"
			

class now:
   def __init__(self):
       self.t = time.time()
       self.storetime()
   def storetime(self):
       self.year, \
       self.month, \
        self.day, \
        self.hour, \
        self.minute, \
        self.second, \
        self.dow, \
        self.doy, \
        self.dst = time.localtime(self.t)
   def __str__(self):
        return time.ctime(self.t)

class now1:
	def __init__(self):
		self.t = time.time()
		self.storetime()
	def storetime(self):
		self.year, \
		self.month, \
		self.day, \
		self.hour, \
		self.minute, \
		self.second, \
		self.dow, \
		self.doy, \
		self.dst = time.localtime(self.t)
	def __str__(self):
		return time.ctime(self.t)

if __name__ == "__main__":
	
	n = now1()
	print "The year is", n.year
	print "__main__"

	#n1 = chap1()
	#n1.toto()
	#ch4 = chap4()
	#ch4.toto()
	#ch4.if_test()
	#ch4.for_loop()

	test = chap4()
	test.while_loop()
	
	

	


	
	

	
	