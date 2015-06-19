from subprocess import call
import sys, re

def regEx(f):
	out=""
	llista = []
	for line in f:
		m = re.findall('\s+[A-Za-z]+=[0-9]+',line,0)
		n = re.findall('Violated property:',line,0)
		if m:
			tractant = ''.join(m)
			tractant = tractant.replace(" ", "")
			temporal = tractant.split("=")
			if temporal[0] not in llista:
				llista.append(temporal[0])
				out =  tractant +"\n"+ out
		elif n:
			line = next(f)
			line = next(f)
			out =  "Test case for branch point: "+line +"\n"+ out
	print out
def readProperties(f):
	out2=""
	llista2 = []
	for line in f:
		m = re.findall('Property\s+'+sys.argv[2]+'[A-Za-z.0-9]+:',line,0)
		if m:
			tractant = ''.join(m)
			tractant = tractant.replace(":", "")
			temporal = tractant.split(" ")
			llista2.append(temporal[1])
	for l in llista2:
		f=open("test.out","w")
		comando_y_argumentos = ['cbmc',sys.argv[1],'--function',sys.argv[2],'--unwind',sys.argv[3],'--property',l]
		call(comando_y_argumentos,stdout=f)
		f=open("test.out","r")
		regEx(f)
		f.close()
if __name__ == "__main__":
	f=open("test.out","w")
	comando_y_argumentos = ['cbmc',sys.argv[1],'--function',sys.argv[2],'--show-properties']
	call(comando_y_argumentos,stdout=f)
	f=open("test.out","r")
	readProperties(f)
	f.close()