class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        if self.lado1 >= self.lado2 and self.lado1 >= self.lado3:
            return self.lado1
        elif self.lado2 >= self.lado1 and self.lado2 >= self.lado3:
            return self.lado2
        else:
            return self.lado3

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

    def __str__(self):
        return (f'Lado mayor: {self.lado_mayor()}, 'f'Tipo de triángulo: {self.tipo_triangulo()}')

triangulo = Triangulo(5, 5, 5)

print(triangulo)
