#crear el archivo
nombre_archivo = 'mi_archivo.txt'

#Este metodo es igual que el de abajo pero no hay que cerrar el open
with open(nombre_archivo, 'w') as archivo:
    archivo.write("Hola como estas")
    archivo.write("\nEstoy agregando texto al archivo con buenas practicas")

# abrir el archivo en modo escritura de peor manera, es lo mismo de arriba pero se supone que no es tan buena practica 

# archivo = open(nombre_archivo, 'w')
# archivo.write("Hola como estas")
# archivo.write("\nEstoy agregando info al arhivo")
# archivo.close()



       
print(f'se creo el archivo : {archivo}')

