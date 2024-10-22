class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: División por cero no es permitida."

    def __str__(self):
        return (f'Suma: {self.suma()}\n'
                f'Resta: {self.resta()}\n'
                f'Multiplicación: {self.multiplicacion()}\n'
                f'División: {self.division()}')

calculadora = Calculadora(10, 5)

print(calculadora)
