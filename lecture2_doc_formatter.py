import fileinput
import sys
import time

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

def format_file(filename):
    replaceAll(filename,"A","a")
    replaceAll(filename,"B","b")
    replaceAll(filename,"C","c")
    replaceAll(filename,"D","d")
    replaceAll(filename,"E","e")
    replaceAll(filename,"F","f")
    replaceAll(filename,"G","g")
    replaceAll(filename,"H","h")
    replaceAll(filename,"I","i")
    replaceAll(filename,"J","j")
    replaceAll(filename,"K","k")
    replaceAll(filename,"L","l")
    replaceAll(filename,"M","m")
    replaceAll(filename,"N","n")
    replaceAll(filename,"O","o")
    replaceAll(filename,"P","p")
    replaceAll(filename,"Q","q")
    replaceAll(filename,"R","r")
    replaceAll(filename,"S","s")
    replaceAll(filename,"T","t")
    replaceAll(filename,"U","u")
    replaceAll(filename,"V","v")
    replaceAll(filename,"W","w")
    replaceAll(filename,"X","x")
    replaceAll(filename,"Y","y")
    replaceAll(filename,"Z","z")
    replaceAll(filename,"."," ")
    replaceAll(filename,","," ")
    replaceAll(filename,":","")
    replaceAll(filename,";","")
    replaceAll(filename,"'","")
    replaceAll(filename,"\""," ")
    replaceAll(filename,"/"," ")
    replaceAll(filename,"\\"," ")
    replaceAll(filename,"!","")
    replaceAll(filename,"?","")
    replaceAll(filename,"\xe2\x80\x99","")
    replaceAll(filename,"-"," ")

def main():
    input_select = input("lecture2_doc_formatter.py\nPlease enter the document name to format:")
    start_time = time.time() * 1000
    format_file("extra_distance_docs/" + input)
    end_time = time.time() * 1000
    print ("Time elapsed: %s milliseconds" % (end_time - start_time))

main()
input("Press return to exit...")
