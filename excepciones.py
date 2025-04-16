print("Manejo de excepciones")

def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        print(resultado)  
    except ZeroDivisionError: 
        print("Has divido por 0, no se puede dividir asi")
    except TypeError:
        print("Estas operando con caracter no numero")
    
    ### Para manejar todos errores se hace asi :
    ### except Exception as e:
    ###    print("Ocutrrio un error")
        

dividir(10,2)
dividir(10,0)
