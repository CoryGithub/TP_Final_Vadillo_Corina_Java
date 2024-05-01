from datetime import date
from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        self._nombre_titular = nombre_titular
        self._dni_titular = dni_titular
        self._fecha_nacimiento = fecha_nacimiento
        self._saldo = saldo
    
    @abstractmethod
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado {monto} a la cuenta de {self._nombre_titular}, su saldo actual es de : {self.obtener_saldo ()} ")
        else:
            print("El monto a depositar debe ser positivo")

    @abstractmethod
    def extraer(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto
            print (f"se ha extraido {monto} de la cuenta de {self._nombre_titular}, su saldo actual es de  {self.obtener_saldo()}") #aca conviene usar getter y setter
        else:
            print ("No posee saldo para realizar esta operacion")


    def obtener_saldo(self):
        return self._saldo
    
    def obtener_un_titular(self):
        return self._nombre_titular
    
    def _calcular_edad(self):
        fecha_actual = date.today()
        edad = fecha_actual - self._fecha_nacimiento
        return edad.days // 365
    
    def obtener_edad(self):
        return self._calcular_edad()
class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0, limite_extraccion=500):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion
        
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado {monto} a la cuenta de {self._nombre_titular}, su saldo actual es de : {self.obtener_saldo ()} ")
        else:
            print("El monto a depositar debe ser positivo")
    
    def extraer(self, monto):
        if monto <= self.obtener_saldo() and monto <= self._limite_extraccion:
            super().extraer(monto)
        else:
            if monto > self._limite_extraccion:
                print("Usted no puede extraer ese monto")
            else:
                print("Usted no posee suficiente saldo para realizar la operacion")

class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0, tasa_de_interes=0.001):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_de_interes = tasa_de_interes
    
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado {monto} a la cuenta de {self._nombre_titular}, su saldo actual es de : {self.obtener_saldo ()} ")
        else:
            print("El monto a depositar debe ser positivo")
    
    def extraer(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto
            print(f"Se ha extraido {monto} de la cuenta de {self._nombre_titular}, su saldo actual es de {self.obtener_saldo()}")
        else:
            print("No posee saldo suficiente para realizar esta operacion")
    
    def calcular_interes(self):
        interes = self._saldo * self._tasa_de_interes
        return interes
    


cuenta1 = CuentaAhorro("Cosme", 88888888, date(1998, 8, 3), 2000)
cuenta2 = CuentaCorriente("Homero", 55555555, date(1991, 2, 4), 500)
print("Cuenta 1:")
print("Saldo:", cuenta1.obtener_saldo())
cuenta1.depositar(1000)
print("Saldo:", cuenta1.obtener_saldo())
cuenta1.extraer(500)
print("Saldo:", cuenta1.obtener_saldo())
interes_cuenta1 = cuenta1.calcular_interes()
print("Interés acumulado:", interes_cuenta1)


print("\nCuenta 2:")
print("Saldo:", cuenta2.obtener_saldo())
cuenta2.depositar(1500)
print("Saldo:", cuenta2.obtener_saldo())
cuenta2.extraer(1000)
print("Saldo:", cuenta2.obtener_saldo())
interes_cuenta2 = cuenta1.calcular_interes()
print("Interés acumulado:", interes_cuenta2)
