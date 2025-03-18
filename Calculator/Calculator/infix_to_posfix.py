# Convierte expresiones matemáticas de infix (ej. "2 + 3") a postfix (ej. "2 3 +").

from Pila import Pilas  # Importamos la clase Pilas para manejar operadores.
import re  # Importamos re para dividir la expresión en tokens.

def is_operand(n):
    """Revisa si un token es un número (operando)."""
    try:
        float(n)
        return True
    except ValueError:
        return False

def prioridades(op):
    """Asigna prioridad a operadores y funciones (mayor número = mayor prioridad)."""
    prioridades = {
        '+': 1,  #
        '-': 1,  
        '*': 2,  
        '/': 2,  
        '^': 3,  
        '(': 0,  
        'log': 4, 'ln': 4, 'sin': 4, 'cos': 4, 'tan': 4,  
        'asin': 4, 'acos': 4, 'atan': 4, 'e^': 4, '10^': 4
    }
    return prioridades.get(op, 0)

def infix2posfix(infix):
    """Convierte una expresión infix a postfix usando una pila."""
    
    tokens = re.findall(r'[+\-*/^()]|e\^|10\^|[a-zA-Z]+|\d+\.?\d*', infix)
    
    pila = Pilas() 
    P = [] 
    
    for valor in tokens:
        if is_operand(valor):  
            P.append(valor)
        elif valor == '(':  
            pila.push(valor)
        elif valor == ')': 
            while not pila.is_empty() and pila.get_top() != '(':
                P.append(pila.pop())
            if not pila.is_empty() and pila.get_top() == '(':
                pila.pop()
        else:  
            while (not pila.is_empty() and pila.get_top() != '(' and 
                   prioridades(pila.get_top()) >= prioridades(valor)):
                P.append(pila.pop())
            pila.push(valor)
    
    
    while not pila.is_empty():
        if pila.get_top() != '(':
            P.append(pila.pop())
    
    return ' '.join(P) 