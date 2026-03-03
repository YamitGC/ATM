import os 

# Diccionario usuarios para organizar los usuarios del cajero.

usuarios = {
    "12345678": {"pin": "5588", "nombre": "saeb", "saldo": 2155000},
    "87654321": {"pin": "1234", "nombre": "Juan", "saldo": 500000}
}
# Lista vacia que guarda un registro de todas las operaciones de un usuario.
historial = []

# Variable que guarda los datos del usuario
usuario_actual = None

# Funcion menu que muestra toda la interfaz grafica del menu por consola 
def menu():
    while True:
        print("--------CAJERO AUTOMATICO---------\n")
        print("SELECCIONE SU OPERACION")
        print("1.Iniciar sesion")
        print("2.Consultar saldo")
        print("3.Retirar dinero")
        print("4.Depositar dinero")
        print("5.Transferir dinero")
        print("6.Ver movimientos")
        print("7.Cerrar sesion")
        print("8.Salir")

        opcion = int(input("Ingresa una opcion (1-8): "))

        if opcion == 1:
            iniciar_sesion()
        elif opcion == 2:
            consultar_saldo()
        elif opcion == 3:
            retirar_dinero()
        elif opcion == 4:
            depositar_dinero()
        elif opcion == 5:
            transferir_dinero()
        elif opcion == 6:
            ver_movimientos()
        elif opcion == 7:
            cerrar_sesion()
        elif opcion == 8:
            print("Saliendo del cajero...")
            break
        else:
            print("Opcion invalida. Ingrese una opcion correcta (1-8)")


def limpiar_pantalla():
    os.system('clear')


def iniciar_sesion():
    limpiar_pantalla()
    global usuario_actual
    intentos = 0

    while intentos < 3:
        tarjeta = input("Ingresa tu número de tarjeta: ")
        pin = input("Ingresa tu PIN: ")

        if tarjeta in usuarios and usuarios[tarjeta]["pin"] == pin:
            usuario_actual = usuarios[tarjeta]
            print(f"Bienvenido {usuario_actual['nombre']}!")
            return True
        else:
            intentos += 1
            print(f"Datos incorrectos. Intento {intentos} de 3")

    print("Tarjeta bloqueada.")
    return False


def consultar_saldo():
    limpiar_pantalla()
    print(f"Tu saldo es: ${usuario_actual['saldo']}")

def retirar_dinero():
    limpiar_pantalla()
    monto = int(input("¿Cuánto quieres retirar?: "))

    if monto > usuario_actual["saldo"]:
        print("Saldo insuficiente.")
    else:
        usuario_actual["saldo"] -= monto
        historial.append(f"Retiro: -${monto}")
        print(f"Retiro exitoso. Saldo actual: ${usuario_actual['saldo']}")

def depositar_dinero():
    limpiar_pantalla()
    monto = int(input("¿Cuánto quieres depositar? "))
    usuario_actual["saldo"] += monto
    historial.append(f"Deposito: +${monto}")
    print(f"Deposito exitoso. Saldo actual: ${usuario_actual['saldo']}")

def transferir_dinero():
    limpiar_pantalla()
    destino = input("Ingresa el número de tarjeta destino: ")

    if destino not in usuarios:
        print("Cuenta destino no encontrada.")
        return

    monto = int(input("¿Cuánto quieres transferir? "))

    if monto > usuario_actual["saldo"]:
        print("Saldo insuficiente.")
    else:
        usuario_actual["saldo"] -= monto
        usuarios[destino]["saldo"] += monto
        historial.append(f"Transferencia a {destino}: -${monto}")
        print(f"Transferencia exitosa. Saldo actual: ${usuario_actual['saldo']}")

def ver_movimientos():
    limpiar_pantalla()
    if len(historial) == 0:
        print("No hay movimientos.")
    else:
        print("--- Historial ---")
        for movimiento in historial:
            print(movimiento)

def cerrar_sesion():
    limpiar_pantalla()
    global usuario_actual
    usuario_actual = None
    print("Sesión cerrada. Hasta luego!")

if __name__ == "__main__":
    menu()