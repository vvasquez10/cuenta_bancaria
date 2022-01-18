"""
La clase CuentaBancaria debe tener un balance. Cuando se crea una nueva instancia de CuentaBancaria, si se da un monto, el balance
de la cuenta debe establecerse inicialmente en ese monto; de lo contrario, el balance debe comenzar en $0. La cuenta también debe tener 
una tasa de interés, guardada como decimal (es decir, 1% se guardaría como 0,01), que debe proporcionarse al crear la instancia. 
(Sugerencia: cuando se utilizan valores predeterminados en los parámetros, ¡el orden de los parámetros es importante!).

La clase también debe tener los siguientes métodos:

depósito(self, amount): aumenta el balance de la cuenta en el monto dado
retiro(self, amount): disminuye el balance de la cuenta en el monto dado si hay fondos suficientes; si no hay suficiente dinero, 
imprime el mensaje: "Fondos insuficientes: cobrando una tarifa de $5", y resta $5
mostrar_info_cuenta(self)imprime en la consola: por ejemplo, "Balance: $100"
generar_interés(self): aumenta el balance de la cuenta por el balance actual * la tasa de interés 
(siempre que el balance sea positivo) 
"""

class CuentaBancaria:

    cuentas = []

    def __init__(self, tasa_interes, balance=0): 
        self.balance = balance
        self.tasa_interes = tasa_interes
        CuentaBancaria.cuentas.append(self)   

    def deposito(self, amount):
        self.balance += amount 
        print("Deposito realizado correctamente.")
        return self

    def retiro(self, amount):
        if self.balance < amount:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            if self.balance >= 5: self.balance -= 5             
        else:
            self.balance -= amount 
            print("Retiro realizado correctamente.")
        return self

    def mostrar_info_cuenta(self):
        print("Balance:",self.balance, "- Tasa de interés:", self.tasa_interes)
        return self

    def generar_interés(self):
        if CuentaBancaria.balancePositivo(self.balance):
            self.balance += (self.balance*self.tasa_interes)
        return self
    
    @staticmethod
    def balancePositivo(balance):
        if balance>0: return True
        else: return False
    
    @classmethod
    def muestraInstancias(cls):
        for i in CuentaBancaria.cuentas:
            cls.mostrar_info_cuenta(i)
       

