"""
Este script contiene errores comunes que violan las normas PEP 8
"""
class Operacionesbasicas:
    """
    Costructor de operaciones
    """
    def __init__(self):
        """
        Constructor de objeto
        """
        self.resultado = 0

    def sumar(self, a, b):
        """
        Esta función suma dos números
        """
        self.resultado = a + b

    def restar(self, a, b):
        """
        Esta función resta dos números
        """
        self.resultado = a - b

    def obtener_resultado(self):
        """
        Obterer resultado
        :return:  number
        """
        return self.resultado


class CalculadoraPromedio:
    """
    Constructor de Calculadora promedio
    """
    def __init__(self, valores):
        """
        Constructor de Calculadora promedio
        """
        self.valores = valores


    def calcular_promedio(self):
        """
        metodo para calcular promedio
        """
        return sum(self.valores) / len(self.valores)


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = Operacionesbasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio_calculado = calculadora_promedio.calcular_promedio()
    print(f"El promedio de los números es: {promedio_calculado}")
