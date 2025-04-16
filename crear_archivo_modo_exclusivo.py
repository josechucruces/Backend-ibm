print ('*** Abrir un archivo en modo exclusivo')

nombre_archivo = 'mi_archivo.txt'

try: 
    with open (nombre_archivo, 'x') as archivo:
        archivo.write("Escribimos en el archivo en modo exclusivo")
    print(f"El archivo ya lo hemos creado se llama : {nombre_archivo}")
except FileExistsError:
    print(f"El archivo : {nombre_archivo} ya existe")
    print("Detalle del error {e}")