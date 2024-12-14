from datos_listas import calcular_tiempo_ejecucion
#from datos_pilas import funcion_entrada_quick
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox

def cargar_archivo():
    # Abre el cuadro de diálogo para seleccionar un archivo
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    if archivo:
        archivo_seleccionado.set(archivo)  # Guarda la ruta del archivo en la variable

def enviar_info():
    nombre_archivo = archivo_seleccionado.get()
    estructura_seleccionada = opcion_estructura.get()  # Obtiene la selección del Combobox

    if not nombre_archivo:
        messagebox.showerror("Error", "Por favor, seleccione un archivo.")
        return

    try:
        # Llama a la función correspondiente según la estructura seleccionada
        if estructura_seleccionada == "Listas":
            ruta_resultado = calcular_tiempo_ejecucion(nombre_archivo)
        elif estructura_seleccionada == "Pilas":
            #ruta_resultado = funcion_entrada_quick(nombre_archivo) #DESCOMENTAR ESTO
            ruta_resultado = calcular_tiempo_ejecucion(nombre_archivo)
        else:
            raise ValueError("Estructura de datos no válida seleccionada.")

        # Mostrar mensaje de éxito con la ruta del archivo generado
        messagebox.showinfo(
            "Éxito",
            f"Los resultados se han generado exitosamente en: {ruta_resultado}"
        )
    except Exception as e:
        # Mostrar mensaje de error en caso de fallo
        messagebox.showerror(
            "Error",
            f"Ocurrió un error al procesar el archivo: {str(e)}"
        )

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Procesamiento de Encuestas")
ventana.geometry("450x400")
ventana.resizable(False, False)

# Encabezado
frame_encabezado = tk.Frame(ventana, pady=10)
frame_encabezado.pack()
texto_inicial = tk.Label(frame_encabezado, text="Procesamiento de Encuestas", font=("Arial", 16, "bold"))
texto_inicial.pack()
subtexto_inicial = tk.Label(frame_encabezado, text="Complete los campos para procesar la encuesta", font=("Arial", 10))
subtexto_inicial.pack()

# Entrada para cargar archivo
frame_archivo = tk.Frame(ventana, pady=10)
frame_archivo.pack(fill="x", padx=20)
texto_archivo = tk.Label(frame_archivo, text="Seleccione un archivo:", anchor="w")
texto_archivo.pack(fill="x")
archivo_seleccionado = tk.StringVar()
campo_archivo = tk.Entry(frame_archivo, textvariable=archivo_seleccionado, width=40, state="readonly")
campo_archivo.pack(side="left", pady=5, padx=5)
boton_cargar = tk.Button(frame_archivo, text="Cargar Archivo", command=cargar_archivo, bg="#2196F3", fg="white")
boton_cargar.pack(side="left", pady=5, padx=5)

# Selección de la estructura de datos
frame_estructura = tk.Frame(ventana, pady=10)
frame_estructura.pack(fill="x", padx=20)
texto_estructura = tk.Label(frame_estructura, text="Seleccione la estructura de datos:", anchor="w")
texto_estructura.pack(fill="x")
opcion_estructura = tk.StringVar()
combobox_estructura = Combobox(frame_estructura, textvariable=opcion_estructura, state="readonly", values=["Listas", "Pilas"])
combobox_estructura.current(0)  # Por defecto selecciona "Listas"
combobox_estructura.pack(pady=5)

# Botón de enviar
frame_boton = tk.Frame(ventana, pady=20)
frame_boton.pack()
boton = tk.Button(frame_boton, text="Obtener Resultados", command=enviar_info, width=20, bg="#4CAF50", fg="white")
boton.pack()

# Iniciar la interfaz
ventana.mainloop()
    