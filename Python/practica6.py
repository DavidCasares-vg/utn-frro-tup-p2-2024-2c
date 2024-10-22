class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_nota(self, nota):
        self.nota = nota

    def get_nombre(self):
        return self.nombre

    def get_nota(self):
        return self.nota

    def imprimir(self):
        print(self) 

    def resultado(self):
        if self.nota >= 6:
            return f'{self.nombre} ha aprobado con una nota de {self.nota}.'
        else:
            return f'{self.nombre} no ha aprobado con una nota de {self.nota}.'

    def __str__(self):
        return f'Nombre: {self.nombre}, Nota: {self.nota}'


alumno1 = Alumno('Juan', 7.5)
alumno2 = Alumno('María', 4.0)

alumno1.imprimir()
print(alumno1.resultado())

alumno2.imprimir()
print(alumno2.resultado())
