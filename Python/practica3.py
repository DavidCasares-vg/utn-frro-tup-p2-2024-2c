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

    def es_mayor_de_edad(self):
        if self.edad is not None:
            if self.edad >= 18:
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'


persona1 = Persona('Juan', 30)
persona2 = Persona('María', 16)
persona3 = Persona('Carlos', 18)

print(f'{persona1}: Es mayor de edad? {persona1.es_mayor_de_edad()}')
print(f'{persona2}: Es mayor de edad? {persona2.es_mayor_de_edad()}')
print(f'{persona3}: Es mayor de edad? {persona3.es_mayor_de_edad()}')
