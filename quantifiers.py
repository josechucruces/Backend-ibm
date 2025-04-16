##buscar palabras que tengan el tamaño de 4 a 6 letras 

words = "ala casa arbol leon cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print (matches)