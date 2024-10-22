class Persona:
    def __init__(self, nombre=None, edad=None):
        self.nombre = nombre
        self.edad = edad

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'


persona1 = Persona('Juan', 30)
persona2 = Persona('María', 25)
persona3 = Persona()  # Sin parámetros

persona3.set_nombre('Carlos')
persona3.set_edad(40)

print(persona1)
print(persona2)
print(persona3)
