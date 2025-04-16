print("Vamos a leer un archivo con Python")

#seleccionamos que archivo leemos
nombre_archivo = "mi_archivo.txt"

#Aqui leemos el archivo con readlines
with open (nombre_archivo, 'r') as archivo:
    #Leer todas las lineas del archivo
    lineas = archivo.readlines()
    for linea in lineas:
        # Con el metodo strip lo que hace es que quita la separacion entre lineas en la lista 
        print(linea.strip())
    
# Leer con el metodo read, que es diferente, regresa todas las lineas de un solo golpe, si es todo el archivo de golpe esto es lo mejor
print ( "Leyendo el archivo con el metodo read")
with open (nombre_archivo, 'r') as archivo:
    print (archivo.read())