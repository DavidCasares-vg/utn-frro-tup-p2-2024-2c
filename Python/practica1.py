class Persona:
    def __init__(self, nombre, edad):
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

print(persona1)
print(persona2)
