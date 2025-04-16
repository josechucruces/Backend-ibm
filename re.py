## regex101.com es una web para expresiones regulares 
## se usan para validar como en este caso mails 

## para poder utilizar expresiones regulares hay que importar el modulo re
import re

def validar_email(email):
    # Expresión regular para validar el email
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(patron, email):
        return True
    else:
        return False

emails = ["usuario@example.com", "correo@dominio", "otro.email@dominio.co", "email_invalido@"]

for e in emails:
    if validar_email(e):
        print(f"✅ '{e}' es un correo válido.")
    else:
        print(f"❌ '{e}' no es válido.")





## por ejemplo para buscar un patron un texto se usa asi :

##decalramos el patron que buscamos
pattern = "Hola"

## aqui declaramos el texto en el que hay que buscarlo
text= "Hola mundo que pasa por ahi ?"

## Aqui recogemos la variable para saber si es tru que esa palabra esta en ese texto
result = re.search(pattern, text)
print(result)


## search() , start() con esos patrones hace cositas 

pattern = "r[a-z]d"  ## Aqui podemos buscar un patron en el texto que tenga primero la letra r y detras una letra que sea de la a a la z y detras una d
text= "Hola mundo perrod que pasa por ahi ?"
result = re.search(pattern, text)
print(result)

#si usamos el metodo start o end dice donde empieza el patron y donde acaba 
print(result.start())

text =" Me gusta Python, Python es lo maximo, aunque no creas , hay que buscar Python para aprender mas"
pattern = "Python"
matches = re.findall(pattern, text)
## Esto lo que imprimos cuantas veces sale, si la lista que crea en matches tienen 4 elementos es que lo ha encontrado 4 veces
print(len(matches))


##Y aqui muestro iternado por el resultado de la budsqueda y mostrando donde salen lo que encuentran 
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())
 
 
    
## Y hay un metodo para SUSTITUIR una palabra que busquemos por otra:

text = "hola , mundo! Hola de nuevo, Hola otra vez."
pattern = "Hola"
replacement = "Adios"

new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print(new_text)
matches = re.findall(pattern, text)


# utilizacion del punto para sustuir por cualequier letra, si coincide una palabra que tenga una H despues una letra cualquiera y despues la , te la encontrara
text = "hola , mundo! Hola de nuevo, Hola otra vez."
pattern = "H.la"
matches = re.findall(pattern, text)
print(matches)

#buscar un caracter en concreto, por ejemplo un punto , hay que poner \ y depues el caracter, en este caso el punto \. 
text = "hola , mundo! Hola de nuevo, Hola otra vez."
pattern = "\."
matches = re.findall(pattern, text)
print(matches)

#buscar los numeros , una d y despues el numero que buscar
text = "hola , mundo! Mi numero de telefon es 67456153, Hola otra vez."
pattern = "d3"
matches = re.findall(pattern, text)
print(matches)

# y se puede buscar un telefono por ejemplo con sus caracteristicas:
text = "hola , mundo! Mi numero de telefon es +34 674561532, Hola otra vez."
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
if found: print (f"Encontre el numero de telefono : {found.group()}")

## ^  es para el comienzo de una cadena, y para acabar una cadena es con $
## por ejemplo para buscar que acabe algo en @gmail.com se pone :

text = "hola , mundo! Mi mail es paco@gmail.com y el telefon es +34 674561532, Hola otra vez."
pattern = r"@gmail.com$"
found = re.search(pattern, text)




## para buscar los archivos que acaban en txt por ejemplo :
# pattern = r"txt$"

files = "file1.txt file2.pdf midu-of.wep secret.txt"
pattern = r".txt$"
valid = re.search(pattern, files)
