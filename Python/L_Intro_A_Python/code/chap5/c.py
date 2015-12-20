#!c:\python\python.exe
def c(p) :
	spy = 60 * 60 * 24 * 365.2422
	n = long(spy) * long(p)
	return n

if __name__ == "__main__" :
	n =c (300000)
	print n