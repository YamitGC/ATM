# ATM PYTHON

#### Este programa simula un cajero automarico en python con su menú interactivo desde consola.


## Estructuras de datos

`usuarios`:**(Diccionario)** almacena la base de datos de los clientes.

`historial`:**(Lista)** Registra cada transacción realizada durante la ejecución del programa.

`usuario_actual`:**(variable global)** variable que guarda los datos del usuario.

## Funcionalidades

- **Autenticación del usuario**: Validacion mediante número de tarjeta y PIN(máximo 3 intentos).

- **Gestion de datos**: Consultar el saldo disponible.

- **Transacciones monetarias**:

     - **Retirar dinero**: Validación de fondos suficientes antes de procesar.

     - **Depositar dinero**: Incremento de saldo en la cuenta activa.

     - **Transferir dinero**: Envío de dinero entre cuentas registradas en el sistema.

- **Historial de movimientos**: Registro detallado de cada operación realizada durante la sesión.

- **Interfaz limpia**: Funciones para mantener una interfaz limpia sin tanto caché inservible.


## Lógica de las Funciones Principales


A continuacion el paso a paso técnico del código:

### 1. Sistema de Inicio de Sesión (`iniciar_sesion`)

1. Solicita credenciales.
2. Compara la entrada con el diccionario `usuarios`.
3. Si hay coincidencia, asigna el diccionario del usuario a `usuario_actual`.
4. Si falla 3 veces, el sistema simula un bloqueo de tarjeta y te devuelve al menú del cajero.

-------------------------------------------------------------------------------------------------------------------------------

### 2. Control de Transacciones

Todas las funciones financieras (`retirar`, `depositar`, `transferir`) realizan una verificación de integridad:

- **Entrada**: Monto deseado.
- **Validacion**: Se comprueba si el monto es menor o igual al saldo disponible.
- **Actualización**: Se modifica el saldo directamente en el diccionario global y se añade un registro a la lista `historial`.

-------------------------------------------------------------------------------------------------------------------------------

### 3. Requisitos

- **Lenguaje**: Python 3.x    
- **Módulos**: `os` (Incluido en la libreria estándar).

-------------------------------------------------------------------------------------------------------------------------------

### 4. Ejecución

``` Bash
python main.py
```




            

