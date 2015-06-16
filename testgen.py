from subprocess import call
import sys

if __name__ == "__main__":
    comando_y_argumentos = ['cbmc',sys.argv[1],'--function',sys.argv[2],'--unwind',sys.argv[3]]
    call(comando_y_argumentos)
