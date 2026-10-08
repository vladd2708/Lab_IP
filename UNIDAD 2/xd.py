import tkinter as tk
from tkinter import messagebox

# ---------------------------------------
# Función para realizar la operación
# ---------------------------------------
def calcular():
    # Obtener los datos de las cajas de texto
    numero1 = entrada1.get()
    numero2 = entrada2.get()

    # Validar que los números sean correctos
    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
    except ValueError:
        messagebox.showerror("Error", "Introduce números válidos.")
        return

    # Obtener la operación seleccionada
    operacion = opcion.get()

    # Validar que se haya seleccionado una operación
    if operacion == "":
        messagebox.showerror("Error", "Selecciona una operación.")
        return

    # Realizar la operación
    if operacion == "suma":
        resultado = numero1 + numero2

    elif operacion == "resta":
        resultado = numero1 - numero2

    elif operacion == "multiplicacion":
        resultado = numero1 * numero2

    elif operacion == "division":
        # Evitar división entre cero
        if numero2 == 0:
            messagebox.showerror(
                "Error",
                "No se puede dividir entre cero."
            )
            return

        resultado = numero1 / numero2

    # Mostrar el resultado
    caja_resultado.delete(0, tk.END)
    caja_resultado.insert(0, str(resultado))


# ---------------------------------------
# Función para limpiar los campos
# ---------------------------------------
def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    caja_resultado.delete(0, tk.END)
    opcion.set("")


# ---------------------------------------
# Función para salir del programa
# ---------------------------------------
def salir():
    ventana.destroy()


# ---------------------------------------
# Crear ventana principal
# ---------------------------------------
ventana = tk.Tk()
ventana.title("Calculadora básica")
ventana.geometry("400x350")


# ---------------------------------------
# Título
# ---------------------------------------
titulo = tk.Label(
    ventana,
    text="Calculadora básica",
    font=("Arial", 18)
)
titulo.pack(pady=10)


# ---------------------------------------
# Primera caja de texto
# ---------------------------------------
tk.Label(ventana, text="Primer número:").pack()

entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)


# ---------------------------------------
# Segunda caja de texto
# ---------------------------------------
tk.Label(ventana, text="Segundo número:").pack()

entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)


# ---------------------------------------
# Botones de radio
# ---------------------------------------
tk.Label(ventana, text="Selecciona una operación:").pack(pady=5)

opcion = tk.StringVar()
opcion.set("")

radio_suma = tk.Radiobutton(
    ventana,
    text="Suma",
    variable=opcion,
    value="suma"
)
radio_suma.pack()

radio_resta = tk.Radiobutton(
    ventana,
    text="Resta",
    variable=opcion,
    value="resta"
)
radio_resta.pack()

radio_multiplicacion = tk.Radiobutton(
    ventana,
    text="Multiplicación",
    variable=opcion,
    value="multiplicacion"
)
radio_multiplicacion.pack()

radio_division = tk.Radiobutton(
    ventana,
    text="División",
    variable=opcion,
    value="division"
)
radio_division.pack()


# ---------------------------------------
# Caja para mostrar el resultado
# ---------------------------------------
tk.Label(ventana, text="Resultado:").pack(pady=5)

caja_resultado = tk.Entry(ventana)
caja_resultado.pack()


# ---------------------------------------
# Botones principales
# ---------------------------------------
boton_calcular = tk.Button(
    ventana,
    text="Calcular",
    command=calcular
)
boton_calcular.pack(pady=10)

boton_limpiar = tk.Button(
    ventana,
    text="Limpiar",
    command=limpiar
)
boton_limpiar.pack()

boton_salir = tk.Button(
    ventana,
    text="Salir",
    command=salir
)
boton_salir.pack(pady=5)


# ---------------------------------------
# Mantener abierta la ventana
# ---------------------------------------
ventana.mainloop()