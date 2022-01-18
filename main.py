from Cuenta import CuentaBancaria

c1 = CuentaBancaria(0.05, 500)
c2 = CuentaBancaria(0.04)
c3 = CuentaBancaria(0.03, 1200)

c1.mostrar_info_cuenta()
c1.generar_interés()
c1.mostrar_info_cuenta()

c2.mostrar_info_cuenta()
c2.deposito(400)
c2.mostrar_info_cuenta()

print("AHORA SE MUESTRA EL RESUMEN DE CUENTAS DE NUESTRO BANCO:")
CuentaBancaria.muestraInstancias()
