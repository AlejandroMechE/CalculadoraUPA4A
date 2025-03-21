from Pila import Pilas  
import math  

def operador(element):
    """Verifica si un token es un operador o función."""
    operadores = {'+', '-', '*', '/', '^', 'log', 'ln', 'sin', 'cos', 'tan', 
                  'asin', 'acos', 'atan', 'e^', '10^', 'pi'}
    return element in operadores

def operar(element, pila):
    """Realiza la operación indicada con los operandos de la pila."""
    
    # Handling constant 'pi'
    if element == 'pi':  
        return math.pi  

    # Unary operators
    if element in {'log', 'ln', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'e^', '10^'}:
        if pila.get_size() < 1:
            print("Error: faltan operandos para función unaria.")
            return None  
        A = float(pila.pop())
        if element == 'sin': return math.sin(math.radians(A))
        elif element == 'cos': return math.cos(math.radians(A))
        elif element == 'tan': return math.tan(math.radians(A))
        elif element == 'asin': return math.degrees(math.asin(A))
        elif element == 'acos': return math.degrees(math.acos(A))
        elif element == 'atan': return math.degrees(math.atan(A))
        elif element == 'log': return math.log10(A) if A > 0 else None  # log(A) must have A > 0
        elif element == 'ln': return math.log(A) if A > 0 else None  
        elif element == 'e^': return math.exp(A)  
        elif element == '10^': return 10 ** A  

    # Binary operators
    if pila.get_size() < 2:
        print("Error: faltan operandos para operador binario.")
        return None
    
    B = float(pila.pop())
    A = float(pila.pop())

    if element == '+': return A + B
    elif element == '-': return A - B
    elif element == '*': return A * B
    elif element == '/': return A / B if B != 0 else None  # Prevent division by zero
    elif element == '^': return A ** B
    else:
        print(f"Error: operador desconocido {element}")
        return None  

def pos2Value(posfix):
    """Calcula el valor de una expresión postfix."""
    pila = Pilas()  
    lista = posfix.split()  
    
    for element in lista:
        if not operador(element):  
            try:
                pila.push(float(element))
            except ValueError:
                print(f"Error: '{element}' no es válido.")
                return None
        else:  
            resultado = operar(element, pila)
            if resultado is None:
                return None  
            pila.push(resultado)
    
    if pila.get_size() == 1:  
        return pila.pop()
    else:
        print("Error: expresión postfix incorrecta.")
        return None  
