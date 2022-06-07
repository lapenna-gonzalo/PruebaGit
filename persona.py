class Persona:
    especie = "humano"  # credito = "clientes" true!!!

    def __init__(self, nombre, apellido, trabajo):
        self.nombre = nombre
        self.apellido = apellido
        self.trabajo = trabajo

    def hablar(self):
        print(
            f"hola soy {self.nombre}, mi apellido es {self.apellido} y mi trabajo es {self.trabajo}")

    def saludar_trabajo(self, trabajo):
        if trabajo == "programador":
            print("que buen laburo")
            
# prueba para git            
print("sadsdasd")