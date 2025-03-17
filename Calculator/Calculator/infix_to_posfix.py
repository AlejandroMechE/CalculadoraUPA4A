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
        '+': 1,  # Suma
        '-': 1,  # Resta
        '*': 2,  # Multiplicación
        '/': 2,  # División
        '^': 3,  # Potencia
        '(': 0,  # Paréntesis de apertura
        'log': 4, 'ln': 4, 'sin': 4, 'cos': 4, 'tan': 4,  # Funciones trigonometricas
        'asin': 4, 'acos': 4, 'atan': 4, 'e^': 4, '10^': 4
    }
    return prioridades.get(op, 0)

def infix2posfix(infix):
    """Convierte una expresión infix a postfix usando una pila."""
    # Divide la expresión en tokens (números, operadores, paréntesis, etc.).
    tokens = re.findall(r'[+\-*/^()]|e\^|10\^|[a-zA-Z]+|\d+\.?\d*', infix)
    
    pila = Pilas()  # Pila para operadores.
    P = []  # Lista para la expresión postfix.
    
    for valor in tokens:
        if is_operand(valor):  # Si es un número, lo añadimos directamente.
            P.append(valor)
        elif valor == '(':  # Apilamos paréntesis de apertura.
            pila.push(valor)
        elif valor == ')':  # Desapilamos hasta el '(' correspondiente.
            while not pila.is_empty() and pila.get_top() != '(':
                P.append(pila.pop())
            if not pila.is_empty() and pila.get_top() == '(':
                pila.pop()
        else:  # Si es operador o función, manejamos prioridad.
            while (not pila.is_empty() and pila.get_top() != '(' and 
                   prioridades(pila.get_top()) >= prioridades(valor)):
                P.append(pila.pop())
            pila.push(valor)
    
    # Vaciamos la pila al final.
    while not pila.is_empty():
        if pila.get_top() != '(':
            P.append(pila.pop())
    
    return ' '.join(P)  # Unimos los tokens con espacios.