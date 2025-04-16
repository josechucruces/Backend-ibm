print ("*** Anexar informacion a un Archivo")
       
nombre_archivo= 'mi_archivo.txt'

with open(nombre_archivo, 'a') as archivo:
    #Anexar info al archivo
    archivo.write ("\nAnexando mas lineas \n")
    
print (" se ha anexado info al archivo {nombre_archivo}")

