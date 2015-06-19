from subprocess import call
import sys, re

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
		comando_y_argumentos = ['python','testgen.py',sys.argv[1],sys.argv[2],sys.argv[3],l]
		call(comando_y_argumentos)

if __name__ == "__main__":
	f=open("test.out","w")
	comando_y_argumentos = ['cbmc',sys.argv[1],'--function',sys.argv[2],'--show-properties']
	call(comando_y_argumentos,stdout=f)
	f=open("test.out","r")
	readProperties(f)
	f.close()