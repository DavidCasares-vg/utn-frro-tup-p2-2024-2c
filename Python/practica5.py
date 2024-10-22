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

    @staticmethod
    def get_mayor(persona1, persona2):
        if persona1.edad is not None and persona2.edad is not None:
            if persona1.edad > persona2.edad:
                return persona1
            else:
                return persona2
        elif persona1.edad is not None:
            return persona1
        elif persona2.edad is not None:
            return persona2
        else:
            return None

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'

persona1 = Persona('Juan', 30)
persona2 = Persona('María', 25)
persona3 = Persona('Carlos', 40)


mayor1 = Persona.get_mayor(persona1, persona2)
mayor2 = Persona.get_mayor(persona2, persona3)

print(f'Entre {persona1} y {persona2}, el mayor es: {mayor1}')
print(f'Entre {persona2} y {persona3}, el mayor es: {mayor2}')
