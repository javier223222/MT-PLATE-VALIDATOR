import tkinter as tk
from tkinter import messagebox

# Funciones para validar el formato
def es_letra(c):
    return 'A' <= c <= 'Z'

def es_numero(c):
    return '0' <= c <= '9'

def maquina_de_turing(placa):
    estado = 'q0'
    posicion = 0

    while True:
        if estado == 'q0':
            if posicion < len(placa) and es_letra(placa[posicion]):
                estado = 'q1'
                posicion += 1
            else:
                estado = 'q_reject'
        
        elif estado == 'q1':
            if posicion < len(placa) and es_letra(placa[posicion]):
                estado = 'q2'
                posicion += 1
            else:
                estado = 'q_reject'
        
        elif estado == 'q2':
            if posicion < len(placa) and es_letra(placa[posicion]):
                estado = 'q3'
                posicion += 1
            else:
                estado = 'q_reject'
        
        elif estado == 'q3':
            if posicion < len(placa) and placa[posicion] == '-':
                estado = 'q4'
                posicion += 1
            else:
                estado = 'q_reject'
        
        elif estado == 'q4':
            if posicion < len(placa) and es_numero(placa[posicion]):
                estado = 'q5'
                posicion += 1
            else:
                estado = 'q_reject'
        
        elif estado == 'q5':
            if posicion < len(placa) and es_numero(placa[posicion]):
                estado = 'q6'
                posicion += 1
            else:
                estado = 'q_reject'
        
        elif estado == 'q6':
            if posicion < len(placa) and es_numero(placa[posicion]):
                estado = 'q7'
                posicion += 1
            else:
                estado = 'q_reject'
        
        elif estado == 'q7':
            if posicion < len(placa) and placa[posicion] == '-':
                estado = 'q8'
                posicion += 1
            else:
                estado = 'q_reject'
        
        elif estado == 'q8':
            if posicion < len(placa) and es_letra(placa[posicion]):
                estado = 'q_accept'
            else:
                estado = 'q_reject'
        
        elif estado == 'q_accept':
            return True
        
        elif estado == 'q_reject':
            return False

# Función para verificar la placa al presionar el botón
def verificar_placa():
    placa = entrada_placa.get().strip().upper()
    if maquina_de_turing(placa):
        resultado_texto.set("✓ Placa válida")
        resultado_label.config(fg="#00C853")  # Verde para válido
        entrada_placa.config(highlightbackground="#00C853", highlightcolor="#00C853")
    else:
        resultado_texto.set("✘ Placa inválida")
        resultado_label.config(fg="#D50000")  # Rojo para inválido
        entrada_placa.config(highlightbackground="#D50000", highlightcolor="#D50000")
        messagebox.showwarning("Formato Incorrecto", "Por favor, ingresa la placa en el formato LLL-NNN-L (ej. ABC-123-D)")

# Función para actualización en tiempo real del mensaje de ayuda
def actualizar_ayuda(event):
    placa = entrada_placa.get().upper()
    if len(placa) <= 3:
        ayuda_texto.set("Formato: LLL-NNN-L")
    elif len(placa) == 4 and placa[3] != '-':
        ayuda_texto.set("Usa '-' después de las letras")
    elif len(placa) > 4 and len(placa) <= 7:
        ayuda_texto.set("Ingresa los números (NNN)")
    elif len(placa) == 8 and placa[7] != '-':
        ayuda_texto.set("Usa '-' después de los números")
    elif len(placa) > 8 and len(placa) <= 9:
        ayuda_texto.set("Ingresa la última letra (L)")
    else:
        ayuda_texto.set("")

# Configuración de la interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("Validador de Placas")
ventana.geometry("400x350")
ventana.config(bg="#e0e5ec")

# Fondo degradado y sombras para efecto neumórfico
background = tk.Canvas(ventana, width=400, height=350, bg="#e0e5ec")
background.pack(fill="both", expand=True)
background.create_oval(-100, -100, 500, 200, fill="#f7f9fc", outline="")
background.create_oval(0, 250, 500, 600, fill="#d1d9e6", outline="")

# Título
titulo = tk.Label(ventana, text="Validador de Placas", font=("Helvetica", 20, "bold"), bg="#e0e5ec", fg="#3E4C59")
titulo.place(x=100, y=20)

# Entrada de texto para la placa
entrada_label = tk.Label(ventana, text="Ingresa la placa:", bg="#e0e5ec", font=("Helvetica", 12))
entrada_label.place(x=50, y=100)

entrada_placa = tk.Entry(ventana, font=("Helvetica", 14), justify="center", highlightthickness=2, relief="flat")
entrada_placa.place(x=50, y=130, width=300)
entrada_placa.bind("<KeyRelease>", actualizar_ayuda)

# Ayuda en tiempo real
ayuda_texto = tk.StringVar()
ayuda_label = tk.Label(ventana, textvariable=ayuda_texto, font=("Helvetica", 10, "italic"), fg="#757575", bg="#e0e5ec")
ayuda_label.place(x=50, y=160)
ayuda_texto.set("Formato: LLL-NNN-L")

# Botón para verificar la placa
verificar_btn = tk.Button(
    ventana, text="Verificar", font=("Helvetica", 14, "bold"), bg="#FF5722", fg="white",
    command=verificar_placa, relief="flat", bd=0
)
verificar_btn.place(x=150, y=200, width=100, height=40)

# Etiqueta para mostrar el resultado
resultado_texto = tk.StringVar()
resultado_texto.set("")
resultado_label = tk.Label(ventana, textvariable=resultado_texto, font=("Helvetica", 14), bg="#e0e5ec")
resultado_label.place(x=50, y=260)

# Iniciar la aplicación
ventana.mainloop()

