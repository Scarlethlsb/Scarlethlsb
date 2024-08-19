class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = salario
    
    def aumentar_sueldo(self, porcentaje):
        aumento = self.sueldo * porcentaje / 100
        self.sueldo += aumento
        print(f"El salario de {self.nombre} ha sido aumentado en {porcentaje}%. Nuevo salario: {self.sueldo}")
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.sueldo}")

nombre = input("Ingrese el nombre del empleado: ")
edad = int(input("Ingrese la edad del empleado: "))
salario = float(input("Ingrese el salario del empleado: "))

empleado = Empleado(nombre, edad, salario)

empleado.mostrar_informacion()
empleado.aumentar_sueldo(float(input("Ingrese el porcentaje de aumento: ")))

#Este ejercicio refuerza el uso del principio de encapsulamiento 
# al proteger los datos del empleado (nombre, edad y salario) y 
# gestionar sus cambios a través de métodos específicos. 
# La clase Empleado define un comportamiento claro para los objetos que representa, 
# cumpliendo con el principio de cohesión.