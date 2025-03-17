# Programa principal de la calculadora: convierte infix a postfix y calcula resultados.

from infix_to_posfix import infix2posfix  # Para convertir expresiones.
from Pos2Valor import pos2Value  # Para evaluar resultados.

def main():
    """Ejecuta la calculadora con varias expresiones infix."""
    # Lista de expresiones a probar (usar espacios para claridad).
    expresiones = [
        "5 * (6 + 2) - 12 / 4",
        "4 - 3 ^ 2 / 3 + 7 * ( 1 - 2 )",
        "2 * ( 2 ^ 3 * 2 - 6 / ( 4 - 2 ) - 10 ) - 2",
        "2 ^ 4 / ( 4 * 1 ) + log ( 110 - 10 ) ^ 2",
        '2 + asin ( 1.7071 - 1 ) + 3',
        '2 + sin ( 45 ) ^ 3',
        '2 * 10^ ( 0 + 2 ) ^ 3',  # Inversa de log
        '2 * log ( 1 + 2 * 3 ) ^ 3',
        '10^ ( log ( 100 ) )',    # Debe dar 100
        'e^ ( ln ( 5 ) )',        # Debe dar 5
        '2 * e^ ( 1 )',           # Debe dar 2 * e
    ]
    
    print("Calculadora: infix a postfix y resultado\n")
    
    for infix in expresiones:  # Procesamos cada expresión.
        postfix = infix2posfix(infix)  # Convertimos a postfix.
        resultado = pos2Value(postfix)  # Calculamos el resultado.
        print(f"Infix: {infix}")  # Mostramos la expresión original.
        print(f"Postfix: {postfix}")  # Mostramos la conversión.
        print(f"Resultado: {resultado}")  # Mostramos el valor.
        print('-' * 70)  # Línea separadora.

if __name__ == '__main__':
    main()  # Iniciamos el programa.