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

    def es_mayor_que(self, otra_persona):
        if self.edad is not None and otra_persona.edad is not None:
            if self.edad > otra_persona.edad:
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'

persona1 = Persona('Juan', 30)
persona2 = Persona('María', 25)
persona3 = Persona('Carlos', 40)

print(f'{persona1} es mayor que {persona2}? {persona1.es_mayor_que(persona2)}')
print(f'{persona2} es mayor que {persona3}? {persona2.es_mayor_que(persona3)}')
print(f'{persona3} es mayor que {persona1}? {persona3.es_mayor_que(persona1)}')
